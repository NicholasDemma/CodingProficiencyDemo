init python:

    #These object categories are to define what an
    ObjectCategories = {
    "Wearable" : ["Tunic","LinenPants","WoolSocks"]
    }

    #These are to define what ARFormat an object will use. For example, any object in the object category "Wearable" will check if its worn first and then its color
    #in that order in their ARStrings and matched against the corresponding properties on the object. For each tuple the first item is the property name
    #and the second item is the default value to match if the ARString did not contain anything at that index
    ARFormats = {
        "Wearable" : [("isworn",False),("color","any")]
    }


    def SayActionResponse(Verb,VerbObject):
        #first we want to loop through the current AR set and get all valid matches and put them into lists of add ons and list of main says
        ActionResponses = []
        ActionResponsesPriorities = []
        ActionResponseAddOns = [[] for i in range(5)] # the *5 means we have room for 5 arrays of addons in this array
        ActionResponseAddOnsPriorities = [[] for i in range(5)]
        HighestAddOnNumber = 0
        HighestARPriority = 0
        HighestARAddonPriority = [0,0,0,0,0]
        #this will look at the players current set of actions responses (ActionResponseType) and the Verb (ActionResponseType.Verb) and get all AR's for that verb
        VerbARMessages = getattr(player.ActionResponseType,Verb,None)
        objectidentifier = VerbObject.simplename
        if hasattr(VerbObject,"identifier"):
            objectidentifier = VerbObject.identifier

        if VerbARMessages is not None:
            for AR in VerbARMessages.keys():
                #smartlog("VerbObject is "+objectidentifier)
                #smartlog("\nDoing something for " + AR,VerbObject)
                #split the string by underscores first (Action Response Parts, ARPs)
                ARPs = AR.split("_")
                #check if the key pertains to verb we are currently trying to get the response for
                if(ARPs[0]==Verb):
                    #Verb is good, check the object name (remove white spaces)
                    #smartlog("its a verb! second part is "+ARPs[1] +". the passed object is "+VerbObject.name.replace(" ",""))
                    ARPriority = 1 #this number determines how specific the action response is to our situation by counting the amount of exact matches and general matches
                    #with exact matches having higher priorities so they will get picked over things with more general matching
                    if(ARPs[1] != objectidentifier):
                        #object is not good, try to check if it can be found in an object category
                        #ARPs[1] is now our key
                        if  ARPs[1] == "any":
                            #this is a very general match.
                            ARPriority -= .5 
                        elif ARPs[1] not in ObjectCategories:
                            #the key was not in object categories
                            continue
                        else:
                            #the key was in object categories
                            #smartlog("it was in object categories!"+objectidentifier+".APRS "+ARPs[1])
                            #ObjectCategories[ARPs[1]] is a list
                            if objectidentifier not in ObjectCategories[ARPs[1]]:
                                continue
                            else: #the key was in a list therfore we are looking at a general match
                                #smartlog("general match!")
                                ARPriority -= .5
                    #We found it! This object is good and something we could be looking for
                    #smartlog("We found it!")
                    for ARFormat in ARFormats.keys() :
                        if ARPs[1]==ARFormat or ARPs[1] in ObjectCategories[ARFormat]:
                            #We found a match! This is the format we have to use
                            #First we remove the first two elements from our ARPs as they are not useful to us anymore
                            del ARPs[0:2]
                            #The rest of them are useful though! So now we will scan over all of them
                            ARPIndex = -1
                            for ARFP in ARFormats[ARFormat]:
                                #Make sure that the current ARP has something in place for this! If not we can count it as default
                                ARPIndex += 1
                                VerbObjectProperty = getattr(VerbObject,ARFP[0],None)
                                if VerbObjectProperty is None:
                                    #The Object that we are trying to print a message for didnt have the property. This should never happen.
                                    #smartlog("Something went wrong! "+ VerbObject+ " has no property \""+ ARFP[0]+ "\"")
                                    break
                                if len(ARPs)>ARPIndex:
                                    #smartlog("Something was in place!")
                                    #Check if it is a digit or has a number
                                    if any(char.isdigit() for char in ARPs[ARPIndex]):
                                        #smartlog("It had a number.")
                                        if ARFP[1] == "any" or ARFP[1] == VerbObjectProperty:
                                            #This is still a match, just a non-specific match
                                            #smartlog("Nonspecific match")
                                            ARPriority += .5 
                                        else:
                                            #smartlog("This is not a match!")
                                            break
                                    else:                                       
                                        #There is not a number! This is legit
                                        #smartlog("This is not a number! This is legit")
                                        #smartlog("The ARP for " + ARFP[0] +" is "+ ARPs[ARPIndex])
                                        if ARPs[ARPIndex] == "any":
                                            #smartlog("It was any. Nonspecific match")
                                            ARPriority += .5 
                                        else:
                                            if ARPs[ARPIndex] == VerbObjectProperty:
                                                #smartlog("Perfect match!")
                                                ARPriority += 1 
                                else:
                                    #smartlog("There exists nothing for "+ARFP[0])
                                    #smartlog("VerbObjectPropertyIs "+VerbObjectProperty)
                                    if ARFP[1] == "any" or ARFP[1] == VerbObjectProperty:
                                        #This is still a match, just a non-specific match
                                        #smartlog("Nonspecific match")
                                        ARPriority += .5 
                                    else:
                                        #smartlog("This is not a match!")
                                        break                        
                            continue
                    #Ok we made it through! Now we have checked everything in the pants category so nothing is left. At this point it now matches perfectly
                    #so we can add it to our list of canidates to possibly print.
                    if "AddOn" not in AR:
                        #this is not an add on. Add it to our possible selection of action responses
                        ActionResponses.append(AR)
                        ActionResponsesPriorities.append(ARPriority)
                        if ARPriority > HighestARPriority:
                            HighestARPriority = ARPriority
                    else:
                        #this is an addon
                        addonindex = AR.find("AddOn")
                        #smartlog("Checking if numbered...")
                        if AR.find("_",addonindex) != -1:
                            #smartlog("This is a numbered addon!")
                            addonnumber = AR[addonindex+5:AR.find("_",addonindex) ]
                        else:
                            addonnumber = AR[addonindex+5:]
                        if addonnumber=="":
                            addonnumber = "1"
                        #smartlog("Addonnumber of "+AR+" is "+addonnumber)
                        if HighestAddOnNumber < int(addonnumber):
                            HighestAddOnNumber = int(addonnumber)                      
                        ActionResponseAddOns[int(addonnumber)-1].append(AR)
                        ActionResponseAddOnsPriorities[int(addonnumber)-1].append(ARPriority)
                        #smartlog("Appended "+AR + " to ARAddOns "+str(int(addonnumber)-1))
                        #smartlog(ActionResponseAddOns[int(addonnumber)-1][0])
                        #smartlog(ActionResponseAddOns[int(addonnumber)][0])
                        #We must now compare the highest ARAddonPriority for this specific AddOnNumber (addonnumber-1 because 0 indexed lists)
                        #smartlog("Addon number is "+str(addonnumber))
                        if ARPriority>HighestARAddonPriority[int(addonnumber)-1]:
                            HighestARAddonPriority[int(addonnumber)-1] = ARPriority
                        #smartlog(AR + " With priority " + str(ARPriority),VerbObject)                   
        else:
            #no attributes for this verb found
            smartlog("This verb has no uses or dosent exist!")
            return
        if len(ActionResponses) == 0:
            smartlog("You cant do that with "+VerbObject.name)
            return

        #Ok we made it through the loop, now our possible actionresponse lists, ARPrio, ARAddons, ARaddonsPrios lists are all filled out, now
        #we can use these priorities to actually decide what to spit out
        #We must choose at least choose 1 Normal Action Response, so we will for now just choose the one with the highest priority
        #smartlog("Here is a key of possible action responses!")
        #ARnum = 0
        #for AR in ActionResponses:
        #    smartlog("Key: "+AR+". Priority: "+str(ActionResponsesPriorities[ARnum]))
        #    ARnum+=1
        #We already know what the highest ARPriority is (We have been keeping track) so we can simply use that. If more than one result has this same
        #highest priority, pick one at random for the time being. First we remove everything without the highest result
        #smartlog("Highest priority is "+str(HighestARPriority))
        #smartlog("At index 0 is " + ActionResponses[0]+ " With prio "+str(ActionResponsesPriorities[0]))
        #smartlog("At index 1 is " + ActionResponses[1]+ " With prio "+str(ActionResponsesPriorities[1]))
        #smartlog("At index 2 is " + ActionResponses[2]+ " With prio "+str(ActionResponsesPriorities[2]))
        index = 0
        while index < len(ActionResponses):
            #smartlog("Looking at index "+str(index)+"..."+ActionResponses[index]+ " with priority "+str(ActionResponsesPriorities[index]))
            if ActionResponsesPriorities[index] < HighestARPriority:
                #smartlog("Deleting "+ActionResponses[index] + " At index "+ str(index)+ " with priority "+str(ActionResponsesPriorities[index]))
                del ActionResponses[index]
                del ActionResponsesPriorities[index]
                index -=1
            index +=1
        ChosenAR = ""
        if len(ActionResponses) == 1:
            #We trimmed the list down to 1 item! We can output that for sure
            ChosenAR = ActionResponses[0]
        else:
            #list still has multiple items. Pick one at random
            randomAR = random.randrange(len(ActionResponses))
            #smartlog("Generated a random number! "+str(randomAR))
            ChosenAR = ActionResponses[randomAR]

        #Now we have chosen an action response, now we can choose any number of AddOns (1 per addon number)
        ChosenARAddons = []
        AddNum = 0
        #smartlog("Choosing Addons. Highest Addonnumber is "+str(HighestAddOnNumber))
        #smartlog("At num 0 index 0 is "+ActionResponseAddOns[0][0])
        #smartlog("At num 0 index 1 is "+ActionResponseAddOns[0][1])
        #smartlog("At num 1 index 0 is "+ActionResponseAddOns[1][0])
        #smartlog("At num 1 index 1 is "+ActionResponseAddOns[1][1])
        while AddNum < HighestAddOnNumber:
            index = 0
            #smartlog("AddNum is "+str(AddNum))
            while index < len(ActionResponseAddOns[AddNum]):
                #smartlog("Index is "+str(index))
                #smartlog("At index "+str(index)+" is "+ActionResponseAddOns[AddNum][index])
                if ActionResponseAddOnsPriorities[AddNum][index] < HighestARAddonPriority[AddNum]:
                    #of all the addons for the current AddNum we are looking at, this one has a lower priority then the highest, delete it
                    #smartlog("Delet")
                    #smartlog("Deleting "+ActionResponseAddOns[AddNum][index])
                    del ActionResponseAddOns[AddNum][index]
                    del ActionResponseAddOnsPriorities[AddNum][index]
                    index -=1
                index +=1
            #now we are through and can pick an Addon for this addonnum from the remaining addons
            randomnum = random.randrange(len(ActionResponseAddOns[AddNum]))
            ChosenARAddons.append(ActionResponseAddOns[AddNum][randomnum])
            AddNum+=1
        #smartlog("We chose addons successfully!")
        #We have chosen all of them. Time to Combine this all into one string.
        ARMessage =  VerbARMessages[ChosenAR]
        for ARAddon in ChosenARAddons:
            ARMessage = ARMessage + " " +  VerbARMessages[ARAddon]
        smartlog(ARMessage,VerbObject)

init -10 python:
    #make sure this is defined before any verbs are defined. Verb can also be found in individual objects in the form of verb overrides
    #Call all verbs from here with their verbstring
    #this is our wrapper for all verbs
    def Verb(func):
        def verbcalled(*args, **kwargs):
            globals()["textlog_firstline"] = True
            returnvalue = False
            #check if there is something we want to run before as well
            #smartlog("First kwarg is "+str(kwargs[0]))
            #hasovveride is a variable from a function that we know has to call this or be present on the stack somewhere
            #if args:#if args has more than zero arguments we can assume this is NOT an override. This is because every verb will always inititally
            global sayingthings
            #smartlog("Are we saying things? "+str(sayingthings))
            #smartlog("Function has say? "+str(hasattr(func,"hassay")))
            if not sayingthings or not hasattr(func,"avoidifsay"): #dont call the function if we are saying things and the function has the property "hassay" (from our UsesSay decorator). This is the inverse.
                #smartlog("pfffts we arent saying things or hassay")
                returnvalue = func(*args, **kwargs)
                #Check if the object has its own thing function it wants to run after the function and if so do it
                tryafterverbstring = "OnAfter"+func.__name__[2:].replace(" ","")
                if hasattr(args[0],tryafterverbstring):
                    #we are calling an override verb
                    afterverbfunc = getattr(args[0],tryafterverbstring)
                    #because it is an override the first parameter would be the object itself, and we dont want what would be self so we remove it
                    afterverbfunc(*(args[1:]), **kwargs)
                return returnvalue
            else:
                smartlog("You cant do that while talking to someone.")
        return verbcalled

    #Use this wrapper to prevent a verb from being called when you are talking or if the verb could call smartsay. if it has say and something is already being said 
    #this is ESPECIALLY important If an object could *potentially* use smartsay then its probably safest to just mark it with this. However if you dont its up to 
    #you to make sure the function still  works properly because while say is running all smartsay statements are skipped entirely, but any other statements 
    #both before and after them in a function are still run. This could lose the player out on valuable dialogue and possibly break things
    #@AvoidIfSay MUST come over @Verb or it wont work
    def AvoidIfSay(fun):
        def wrapped(*args, **kwargs):
            return fun(*args, **kwargs)

        wrapped.avoidifsay = True
        return wrapped

init python:
    @Verb #OnCheck
    def OnCheck(obj):
        pass

    @Verb #OnClose
    def OnClose(obj):
        Close(obj)

    @Verb #HideStuff
    def OnHideStuff(obj):
        Close(obj,log = False)

    def Close(obj, log = True):
        if log:
            smartlog("Closing "+obj.name)

        #we will always let it be closed
        obj.isopen = False
        if obj.objectsinside:
            def MakeInvisible(obj):
                obj.isvisible = False
            DoSomethingForAllList(obj.objectsinside,MakeInvisible)

        obj.currentverbs.insert(obj.currentverbs.index(obj.closeverb),obj.openverb)
        obj.currentverbs.remove(obj.closeverb)

    @Verb #OnOpen
    def OnOpen(obj):
        Open(obj)

    @Verb #ShowStuff
    def OnShowStuff(obj):
        Open(obj,log = False)

    def Open(obj, log = True):
        if log:
            smartlog("Opening "+obj.name)

        #but if it has nothing inside of it then it shouldnt be able to be opened now
        if obj.objectsinside:
            #it has stuff in it
            obj.isopen = True
            def MakeVisible(obj):
                if obj.parent.flag("isopen"):
                    obj.isvisible = True

            DoSomethingForAllList(obj.objectsinside,MakeVisible)
            obj.currentverbs.insert(obj.currentverbs.index(obj.openverb),obj.closeverb)
            obj.currentverbs.remove(obj.openverb)
        else:
            if log:
                smartlog("There is nothing in it...")
        

    @Verb #OnDrop
    def OnDrop(obj):
        DropItem(obj)
        SayActionResponse("Drop",obj)
        #style.rebuild()
        #textlogGUI = renpy.get_displayable("game_gui","textloggrid")
        #newstyle = Style(default)
        #newstyle.background = "FF0000"
        #style.__setattr__("uio_button",newstyle)
        #smartlog(str(newstyle.background))
        #smartlog(str(dir(style)))
        #style.rebuild()

    @Verb #OnTake
    def OnTake(obj):
        if "Take" not in obj.currentverbs:
            smartlog("you cant take that")
            return
        #smartlog("You take the "+obj.name)
        MoveToInventory(obj)
        SayActionResponse("Take",obj)

    @Verb #OnEat
    def OnEat(obj):
        if obj.count>1 and not keyboard.is_pressed('shift'):
            obj.count -=1
            obj.ids.pop()
            smartlog("You eat the "+obj.name.lower())
        else:
            if obj.count>1:
                smartlog("You eat all the "+obj.name.lower()+"s")
            else:
                smartlog("You eat the "+obj.name.lower())
            DeleteItem(obj)
    #returns true if it was worn, false if not

    @Verb #OnEnter
    @AvoidIfSay
    def OnEnter(obj):
        if OnGo(obj):
            if not obj.locked:
                DeselectObject(obj)
                if obj.entermessage == "":
                    smartlog("You go through the "+obj.type+" and into "+obj.article+"(=self.otherlocationname=)",obj)
                else:
                    smartlog(obj.entermessage)
                SetCurrentLocation(obj.otherlocationname)
            else:
                SayActionResponse("Locked",obj)

    @Verb #OnEmpty
    def OnEmpty(obj):
        if obj.objectsinside:
            for obj2 in obj.objectsinside:
                DeleteItem(obj2)
            SayActionResponse("Empty",obj)
        else:
            smartlog("Its already empty")


    @Verb #OnExamine
    def OnExamine(obj):
        smartlog("Examine "+obj.name)
        SayActionResponse("Examine",obj)

    #exit and enter are basically the same verb just with a different alias
    @Verb #OnExit
    @AvoidIfSay
    def OnExit(obj):
        OnEnter(obj)
        
    @Verb #OnExtinguish
    def OnExtinguish(obj):
        SayActionResponse("Extinguish",obj)
        obj.islit = False
        obj.currentverbs.insert(obj.currentverbs.index("Extinguish"),"Light")
        obj.currentverbs.remove("Extinguish")

    @Verb #OnGo
    def OnGo(obj)->bool: #returns if we succeeded in going there or not
        if obj.scope == scope.location and player.mostspecificlocation != obj:
            if player.pose != pose.standing:
                #on stand up and any other pose changing verbs currently assume the player is the target, but in the future NPCs may also be able to use these verbs
                #(and maybe other verbs too!) but for now assume player so we dont need a field dictating who is doing the verb, nor do we need it for any verbs
                OnStandUp(player.mostspecificlocation)
            global player
            player.mostspecificlocation.removetooltip("playerpresent")
            player.mostspecificlocation.currentverbs.insert(0,"Go")
            player.mostspecificlocation = obj
            if isinstance(obj, InteractionArea):
                if player.current_IA != obj.parent:
                    player.current_IA.playerpresent = False
                    player.current_IA = obj
                    obj.playerpresent=True

                if player.current_IL is not None:
                    player.current_IL.playerpresent = False
                    player.current_IL = None

                if player.current_IO is not None:
                    player.current_IO.playerpresent = False
                    player.current_IO = None

            elif isinstance(obj, InteractionLocation):
                if player.current_IA != obj.parent:
                    player.current_IA.playerpresent = False
                    player.current_IA = obj.parent
                    player.current_IA.playerpresent=True

                if player.current_IL is not None and player.current_IL!=obj:
                    player.current_IL.playerpresent = False
                player.current_IL = obj
                obj.playerpresent=True

                if player.current_IO is not None:
                    player.current_IO.playerpresent = False
                    player.current_IO = None

            elif isinstance(obj, InteractionObject):
                if player.current_IA != obj.parent.parent:
                    player.current_IA.playerpresent = False
                    player.current_IA = obj.parent.parent
                    player.current_IA.playerpresent=True

                if player.current_IL is not None and player.current_IL!=obj.parent:
                    player.current_IL.playerpresent = False
                player.current_IL = obj.parent
                player.current_IL.playerpresent = True
        
                if player.current_IO is not None and player.current_IO!=obj:
                    player.current_IO.playerpresent = False
                player.current_IO = obj
                obj.playerpresent = True
            if "Go" in player.mostspecificlocation.currentverbs:
                player.mostspecificlocation.currentverbs.remove("Go")
            player.mostspecificlocation.beforetooltips.append(ItemTooltip("You are here","playerheretooltip.png","playerpresent"))
            SayActionResponse("Go",obj)
            return True
        elif player.mostspecificlocation == obj:
            #we were already here. Thats fine though, we just return true still
            return True
        return False

    @Verb #OnHideFurnitureInMenu
    def OnHideFurnitureInMenu(IA):
        smartlog("Hiding furniture in "+IA.name)
        def MakeInvisible(obj):
            obj.isvisible = False
            #smartlog(obj.name+" is visible: "+str(obj.isvisible))

        IA.childrenvisible = False
        DoSomethingForAllChildren(IA,MakeInvisible)

        IA.currentverbs.insert(IA.currentverbs.index("Hide Furniture In Menu"),"Show Furniture In Menu")
        IA.currentverbs.remove("Hide Furniture In Menu")
        #if you dont change the variable it will not save it, inserting and removing DOES NOT COUNT
        #IA.currentverbs=IA.currentverbs

    @Verb #OnShowFurnitureInMenu
    def OnShowFurnitureInMenu(IA):
        smartlog("Showing furniture in "+IA.name)
        def MakeVisible(obj):
            #smartlog(obj.name+" is visible: "+str(obj.isvisible))
            makevisible = True
            parent = obj.parent

            if hasattr(obj,"relativelocation") and obj.relativelocation == relativelocation.inside:
                if not parent.flag("isopen"):
                    makevisible = False

            while hasattr(parent,"parent"):
                if not parent.childrenvisible:
                    makevisible = False
                parent = parent.parent

            if makevisible:
                obj.isvisible = True

        IA.childrenvisible = True
        DoSomethingForAllChildren(IA,MakeVisible)

        IA.currentverbs.insert(IA.currentverbs.index("Show Furniture In Menu"),"Hide Furniture In Menu")
        IA.currentverbs.remove("Show Furniture In Menu")
        #if you dont change the variable it will not save it, inserting and removing DOES NOT COUNT
        #IA.currentverbs=IA.currentverbs

    @Verb #OnLayDown
    def OnLayDown(obj) ->bool: #returns if we could lay down or not
        if OnGo(obj):
            #smartlog("we did it we went there (or were already there)")
            if player.pose != pose.layingdown:
                player.pose = pose.layingdown
                SayActionResponse("LayDown",obj)
                if "Lay Down" in obj.currentverbs:
                    obj.currentverbs.remove("Lay Down")
        else:
            smartlog("You cant go there so you cant lay there")
            return False
        return True

    @Verb #OnLight
    def OnLight(obj):
        SayActionResponse("Light",obj)
        obj.islit = True
        obj.currentverbs.insert(obj.currentverbs.index("Light"),"Extinguish")
        obj.currentverbs.remove("Light")

    @Verb #OnPrintInfo
    def OnPrintInfo(obj):
        smartlog("Printing info for \""+obj.name+"\"")
        smartlog(obj.name+" is visible: "+str(obj.isvisible))
        smartlog("\n")
        for item in locationitems:
            smartlog("Doing "+item.displayname)
            for property, value in vars(item).items():
                smartlog("Property: "+property+"| value: "+str(value).replace("[","("))
                #setattr(item,property,value)

    @Verb #OnRemove
    def OnRemove(obj)->bool:
        #smartlog("We called global remove!")
        TakeOffItem(obj)
        SayActionResponse("Remove",obj)

    @Verb #OnSit
    def OnSit(obj) ->bool: #returns if we could sit or not
        if obj.currentpeople<obj.maxpeople:
            if OnGo(obj):
                #smartlog("we did it we went there")
                obj.currentpeople += 1
                player.pose = pose.sitting
                SayActionResponse("Sit",obj)
                obj.currentverbs.remove("Sit")
            else:
                smartlog("You cant go there so you cant sit there")
                return False
        return True

    #You might think with there being a sit verb you might need an "unsit" verb but really every varb that changes the players pose will do the "unsitting
    #or "unlaying down" or "unstanding" for them. However its worth noting that standing is our intermediate pose and most poses will be entered from standing up
    @Verb #OnStandUp
    def OnStandUp(obj):
        if player.pose == pose.sitting:
            obj.currentpeople -= 1
            obj.currentverbs.append("Sit")
        elif player.pose == pose.layingdown:
            obj.currentverbs.append("Lay Down")
        player.pose = pose.standing
        smartlog("You stand up from the "+obj.name.lower())
      

    @Verb #OnSleep
    def OnSleep(obj):
        smartlog("How long will you sleep for? (Type the time in minutes and hit enter, 0 to cancel)")
        global gettinginput
        global verbsenabled
        gettinginput = True
        verbsenabled = False
        input = renpy.input("",multiline=False, pixel_width = renpy.get_physical_size()[0]*.6 - 30)
        verbsenabled = True
        gettinginput = False
        if (input.lstrip("-").isnumeric()):
            numinput = int(input)
            if numinput == 0:
                smartlog("You decide not to sleep")
            elif numinput>0:
                couldlaydown = OnLayDown(obj)
                #smartlog("are we even here")
                if couldlaydown:
                    smartlog("You sleep for " +input+" minutes")
            else:
                smartlog("You sleep for "+input+" minutes...and get sent back into the past. Nope that's not how it works.")
        else:
            smartlog("Thats...not a number")

    @Verb #Talk
    @AvoidIfSay
    def OnTalk(obj):
        #smartsay(obj.name,"Yeah I can talk so what?", who_color ="#b65036de")
        #smartsay(obj.name,"Yeah I can talk so what?", who_color = obj.who_color , what_color = "#b65036de", background = "#b65036de")
        smartsay(obj.name,"Yeah I can talk so what? Also this is a test a very cool test a very very very very very great testtttt *does a little dance*")

    @Verb #Throw Away
    def OnThrowAway(obj):
        GetSecondObject(obj,"Trash what? (hold shift and click to trash entire stack)","trashable",Trash)

    def Trash(location,obj):
        MoveItemToRelativeLocationInObject(obj,location,relativelocation.inside, canmoveall = True)
        if keyboard.is_pressed('shift') and obj.count > 1:
            smartlog("You throw away the "+obj.pluralname.lower())
        else:
            smartlog("You throw away the "+obj.name.lower())

    
    @Verb #Turn On
    def OnTurnOn(obj):
        obj.ison = True
        smartlog("You turn on the "+obj.name)
        obj.currentverbs.remove("Turn On")
        obj.currentverbs.append("Turn Off")

    @Verb #Turn Off
    def OnTurnOff(obj):
        smartlog("You turn off the "+obj.name)
        obj.ison = False
        obj.currentverbs.remove("Turn Off")
        obj.currentverbs.append("Turn On")

    @Verb #Wash Hands
    def OnWashHands(obj):
        smartlog("You wash your hands with some soap and water. All nice and clean now.")

    @Verb #Wear
    def OnWear(obj)->bool:
        #smartlog("We called global wear!")
        if TryWearItem(obj):
            SayActionResponse("Wear",obj)  

    #utility function
    def GetSecondObject(firstobj,prompt,requiredproperty, callback, *callbackargs ,suggestionlist = "",tryitemtext = "(=self.name=) ", doesntworktext="that wont work..."):
        #This function opens up a dialogue box asking the player to click on another item to use with the firstobj item, it sets our UI up to 
        #make the callback once we click on something
        #smartlog("Entered get second object")
        renpy.show_screen("chooseobjects",prompt,suggestionlist,None)
        #disable the use of verbs 
        globals()["verbsenabled"] = False
        globals()["choosingobject"] = True 
        globals()["choosingobjectprompt"] = prompt
        globals()["choosingobjectsuggestionlist"] = suggestionlist
        globals()["choosingobjectrequiredproperty"] = requiredproperty
        globals()["choosingobjectcallback"] = callback
        globals()["choosingobjectcallbackarguments"] = [firstobj,*callbackargs]
        globals()["choosingobjecttryitemtext"] = tryitemtext
        globals()["choosingobjectdoesntworktext"] = doesntworktext
        
