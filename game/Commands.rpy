python early:

    #Text processing function. 
    #This text processing function is originally from Quest Text adventures written for Visual basic and currently partially translated by me to work in python
    #this and processtext and the other functions that this calls and that those call and so on and so fourth are originally from quest but translated and modified me to work in python
    #and for my own needs
    def ProcessText(text,scopeobject) -> str:
        #data = NewDictionary()
        #dictionary add (data, "fulltext", text)
        if scopeobject is None:
            if Game.textprocesserthis is not None:
                scopeobject = Game.textprocesserthis
        text = ProcessTextSection("",text, scopeobject)
        return text #(Replace(Replace(text, "@@@open@@@", "{"), "@@@close@@@", "}"))

    #beforetext is currently just used as a reference for our autocapitalize string command
    #taken from quest
    def ProcessTextSection(beforetext,text,scopeobject) -> str:
        containsUnprocessedSection = False
        closeind = 0
        openind = 0
        processopen = "(="
        processopenlength = 2
        processclose = "=)"
        processcloselength = 2
        openind = text.find(processopen)
        #say("","openind: "+str(openind))
        if openind >= 0:
            nestCount = 1
            searchStart = openind + processopenlength
            finished = False
            while not finished:
                nextOpen = text.find(processopen,searchStart)
                nextClose = text.find(processclose,searchStart)
                if nextClose > 0 :
                    if nextOpen > 0 and nextOpen < nextClose:
                        nestCount = nestCount + 1
                        searchStart = nextOpen + processopenlength
                    else :
                        nestCount = nestCount - 1
                        searchStart = nextClose + processcloselength
                        if nestCount == 0:
                            close = nextClose
                            containsUnprocessedSection = True
                            finished = True
                else :
                    finished = True
            if containsUnprocessedSection :
                #say("","openind: "+str(type(openind)))
                #say("","close: "+str(type(close)))
                section = text[openind+processopenlength:close] #Mid(text, openind + 1, close - openind - 1)
                #say("","text is \""+text+"\".initial before text is:\""+text[0:openind] +"\"") 
                textbeforeopen = text[0:openind]
                value = ProcessTextCommand(beforetext + textbeforeopen, section, scopeobject)
                #say("","Value: "+value)
                #say("","Openind: "+str(openind))
                text =  textbeforeopen + value + ProcessTextSection(beforetext + text[0:openind] + value,text[close+processcloselength:],scopeobject) #Left(text, openind - 1) + value + ProcessTextSection(Mid(text, close + 1), data)
        return (text)

    #Taken from quest
    def ProcessTextCommand(beforetext,section,scopeobject) -> str:
        if section.startswith("if"): #(StartsWith(section, "if ")) {
            return (ProcessTextCommand_If(beforetext, section, scopeobject))
        # else if (StartsWith(section, "object:")) {
        #   return (ProcessTextCommand_Object(section, data))
        # }
        # else if (StartsWith(section, "command:")) {
        #   return (ProcessTextCommand_Command(Mid(section, 9), data))
        # }
        # else if (StartsWith(section, "page:")) {
        #   return (ProcessTextCommand_Command(Mid(section, 6), data))
        # }
        # else if (StartsWith(section, "exit:")) {
        #   return (ProcessTextCommand_Exit(section, data))
        # }
        # else if (StartsWith(section, "once:")) {
        #   return (ProcessTextCommand_Once(section, data))
        # }
        # else if (StartsWith(section, "random:")) {
        #   return (ProcessTextCommand_Random(section, data))
        # }
        # else if (StartsWith(section, "rndalt:")) {
        #   return (ProcessTextCommand_RandomAlias(section, data))
        # }
        # else if (StartsWith(section, "img:")) {
        #   return (ProcessTextCommand_Img(section, data))
        # }
        # else if (StartsWith(section, "counter:")) {
        #   return (ProcessTextCommand_Counter(Mid(section, 9), data))
        # }
        # else if (StartsWith(section, "select:")) {
        #   return (ProcessTextCommand_Select(section, data))
        # }
        else:
            #if its not a command, then there is no reason to nest anymore and we can assume we are at the bottom nesting
            return TryProcessTextObject(beforetext,section,scopeobject)

    #partially taken from quest but also heavily modified by me, especially the string commands part and using an object in scope
    def TryProcessTextObject(beforetext, section,scopeobject,forif = False) ->str or bool: 
        #this takes the string representation of an object (either global, global.something, this, this.something, global.something.something... or this.something.something...)
        #and will parse out all of the dots until all we are left with is an object that may or may not exist. If it exists it returns its string representation
        #the forif property determines if this should return a True or False value or if can return any string (it would return True if it found it or false if not)
        #enter here assuming we are at the bottom of nesting
        #smartlog("","trying to process it "+section)
        #first we check if there is a string command at the end that we should not use to find the object but rather as a command to do something to the
        #resulting string that the object will produce
        stringcommand = "a" #a is set as the default string command because this string command is "autocapatilize"
        nameused = False
        nameisproper = False
        #return ":3"
        if section[-2]=="!":
            #smartlog("Found !"+section[-1:])
            stringcommand = section[-1]
            section = section[0:-2]
            #smartlog("Section is "+section)
            #return "bklah"

        currentobject = None
        dot = section.find(".") #instr(section, ".")
        if dot == -1 :
            #nodots
            objectname = section
            if objectname == "self" or objectname == "this":
                currentobject = scopeobject
            try :
                currentobject =  globals()[objectname]
            except:
                pass
            if currentobject != None:
                if (callable(currentobject)):
                    #object is a function do some stuff
                    pass
                else:
                    return str(currentobject)    
            #could not be resolved to any sort of object  
            if forif:
                return False
            else:
                return section  
            #return ("{" + ProcessTextSection(section, scopeobject) + "}")
        #there was a dot
        else:
            #there was a dot
            #smartlog("","there was a dot")
            currentobject = None
            objectname = section[0:dot] #Left(section, dot - 1)
            dot2 = section.find(".",dot+1)
            if dot2 > 0:
                #still more dots
                attributename = section[dot+1:dot2] #Mid(section, dot + 1)
            else:
                #no more dots  
                attributename = section[dot+1:] 

                #smartlog("Attribute name is "+attributename) 
                dot = -1   
            if objectname == "self" or objectname == "this":
                currentobject = scopeobject
                #smartlog("object name is "+currentobject.name) 
            else :
                try :
                    currentobject =  globals()[objectname]
                except:
                    pass
            if currentobject == None:
                #no base object found
                if forif:
                    return False
                else:
                    return section
                #return ("(=" + ProcessTextSection(section, scopeobject) + "=)")
            #based off of name.property name.property.property.
            try:
                if attributename == "name":
                    nameused = True
                    nameisproper =  currentobject.flag("nameisproper")
                currentobject = getattr(currentobject,attributename)
            except:
                #that attributename is not valid. Therefore the whole object is not valid
                if forif:
                    return False
                else:
                    return section
            while dot > 0:
                try:
                    #currentobject = getattr(currentobject,attributename)
                    dot = dot2 
                    dot2 = section.find(".",dot+1)
                    if dot2 > 0:
                        #still more dots
                        attributename = section[dot+1:dot2] #Mid(section, dot + 1)
                    else:
                        #no more dots  
                        attributename = section[dot+1:]
                        dot = -1
                    if attributename == "name":
                        nameused = True
                        nameisproper =  currentobject.flag("nameisproper")
                    currentobject = getattr(currentobject,attributename)   
                except:
                    #an exception occured. We didnt get to finish doing all of the dots so set the object to none
                    currentobject = None
                    dot = -1
            if currentobject is None :
                #no object found, assume raw text with {=} included
                #return ("{" + ProcessTextSection(section, scopeobject) + "}")
                #idk why I would do this yet, just gonna return false for now
                if forif:
                    return False
                else:
                    return section

            else:
                if forif:
                    return bool(currentobject)
                #the object existed
                #TODO at some point check if this is a function and if so run that function and returns results
                #smartlog("The object existed")
                objectstring = str(currentobject)
                #This stuff is all me
                if stringcommand != "":
                    #there was a string command! We will now perform some string operation on the resulting object string
                    if stringcommand == "a": #autocapitalize. This is the "default command" (it will always run unless specified not to) 
                        #This will make the word capatilized if its at the start of a sentence or lowercase if its not. It will not affect names of anything marked with
                        #"nameisproper". Add functionality as is needed.
                        #say("",objectstring+". nameused? "+str(nameused)+". nameisproper?"+str(nameisproper))
                        if nameused and nameisproper:
                            #propernoun. Assume its alreadyh capatalized.
                            #objectstring = objectstring.capitalize()
                            pass
                        else:   
                            #not a propernoun. Capitalize as needed. 
                            #smartsay("beforetext before removeal is:\""+beforetext +"\"")
                            #since "{" and "}" are special characters whats in them doesnt actually count as text that will be dispalyed so we can ignore them
                            indexofopen = beforetext.find("{")
                            while indexofopen != -1:
                                beforetext = beforetext[0:indexofopen] + beforetext[beforetext.find("}")+1:]
                                indexofopen = beforetext.find("{")  
                            #then we find where the last period is 
                            periodindex = beforetext.rfind(".")
                            #we start at the index after it (and if its -1 consequentially this means we start at 0, which is perfect)
                            checkspace = beforetext[(periodindex+1):]
                            #smartsay("beforetext is:\""+beforetext +"\".checkspace is:\""+checkspace+"\" contains letters?" +str(any(c.isalpha() for c in checkspace)))
                            if any(c.isalpha() for c in checkspace):
                                #checkspace contains at least one alphabetical letter. That means there is at least one letter between the current word
                                #and the start of the sentence hence we should not capitalize this word
                                objectstring = objectstring.lower()
                            else:
                                objectstring.capitalize()
                            #smartsay("No crash 3")
                    elif stringcommand == "n": #this is the do nothing command.
                        pass
                    elif stringcommand == "l": #make the whole string lowercase
                        objectstring = objectstring.lower()
                    elif stringcommand == "c": #capitalize just the first letter BUT also make every other letter lowercase
                        objectstring = objectstring.capitalize()
                    elif stringcommand == "C": #capitalize every word
                        objectstring = s = ' '.join(word[0].upper() + word[1:] for word in objectstring.split())
                    elif stringcommand == "u": #capitalize the first letter but also dont mess with casing on other letters
                        objectstring = objectstring[0].upper() + objectstring[1:]
                    elif stringcommand == "U": #make the whole string uppercase
                        objectstring = objectstring.upper()
                    else:
                        smartlog("I dont recognize that command \""+stringcommand+"\"")

                return objectstring
        #         if (HasAttribute(object, attributename)) {
        #             type = TypeOf(object, attributename)
        #             switch (type) {
        #             case ("string", "int", "double") {
        #                 return (ToString(GetAttribute(object, attributename)))
        #             }
        #             case ("boolean") {
        #                 result = GetAttribute(object, attributename)
        #                 if (result) {
        #                 return ("true")
        #                 }
        #                 else {
        #                 return ("false")
        #                 }
        #             }
        #             default {
        #                 return ("(" + type + ")")
        #             }
        #             }
        #         }
        #         else {
        #             return ("")
        #     }
        #     }
        # }

    #from quest
    def ProcessTextCommand_If(beforetext, section,data) ->str:
        #return "if called"
        command = section[3:]#Mid(section, 4)
        #return command
        colon = command.find(":")#Instr(command, ":")
        if (colon == -1) :
            return ("(=if " + command + "=)")
        else :
            text = command[colon+1:]#Mid(command, colon + 1)
            condition = command[0:colon]#Left(command, colon - 1)
            #if (not game.text_processor_this = null) condition = Replace(condition, "this", game.text_processor_this.name)
            operator = condition.find("<=")
            if operator >= 0:
                operatorlength = 2

            elif condition.find(">=") >= 0:
                operator = condition.find(">=")
                operatorlength = 2

            elif condition.find("!=") >= 0:
                operator = condition.find("!=")
                operatorlength = 2

            elif condition.find("<") >= 0:
                operator = condition.find("<")
                operatorlength = 1

            elif condition.find(">") >= 0:
                operator = condition.find(">")
                operatorlength = 1
            #support for == and =
            elif condition.find("==") >= 0:
                operator = condition.find("==")
                operatorlength = 2

            elif condition.find("=") >= 0:
                operator = condition.find("=")
                operatorlength = 1

            #for the "not" keyword and if we are just trying to evaluate a single flag          
            else:         
                usingnot = False
                if condition.startswith("not"): #if (StartsWith(condition, "not ")) {
                    usingnot = True
                    condition = condition[4:]#Mid(condition, 5)
                #say("","no operator found. The condition is \""+condition+"\"")
                result = TryProcessTextObject(beforetext,condition,data,forif = True)
                #return "result is "+str(result)
                #the result was interpreted
                #say("","text is: "+text)
                if usingnot:
                    if not result:
                        return ProcessTextSection(beforetext,text, data)
                    else:
                        return ""
                else:
                    if result:
                        return ProcessTextSection(beforetext,text, data)
                    else:
                        return ""


            #an operator (other then not) was found! Do the operator stuff
            if operator >=0:
                return "operator found! But this is not implemented yet!"
            #     lhs = Left(condition, operator - 1)
            #     rhs = Mid(condition, operator + operatorlength)
            #     op = Mid(condition, operator, operatorlength)
            #     dot = Instr(lhs, ".")
            #     if (dot = 0) {
            #         objectname = ""
            #         attributename = ""
            #         if (HasInt(game, lhs)) {
            #         objectname = "game"
            #         attributename = lhs
            #         }
            #         else {
            #         return ("@@@open@@@if " + command + "@@@close@@@")
            #         }
            #     }
            #     else {
            #         objectname = Left(lhs, dot - 1)
            #         attributename = Mid(lhs, dot + 1)
            #     }
            #     object = ObjectForTextProcessor(objectname)
            #     if (object = null) {
            #         return ("@@@open@@@if " + command + "@@@close@@@")
            #     }
            #     else if (not HasAttribute(object, attributename)) {
            #         return ("@@@open@@@if " + command + "@@@close@@@")
            #     }
            #     else {
            #         value = GetAttribute(object, attributename)
            #         if (TypeOf(value) = "object") {
            #         value = value.name
            #         }
            #         if (op = "=") {
            #         if (ToString(value) = rhs) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #         else if (op = "<>") {
            #         if (not ToString(value) = rhs) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #         else if (op = ">") {
            #         if (ToDouble(ToString(value)) > ToDouble(rhs)) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #         else if (op = "<") {
            #         if (ToDouble(ToString(value)) < ToDouble(rhs)) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #         else if (op = ">=") {
            #         if (ToDouble(ToString(value)) >= ToDouble(rhs)) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #         else if (op = "<=") {
            #         if (ToDouble(ToString(value)) <= ToDouble(rhs)) {
            #             return (ProcessTextSection(text, data))
            #         }
            #         else {
            #             return ("")
            #         }
            #         }
            #     }
            #     }
            # }