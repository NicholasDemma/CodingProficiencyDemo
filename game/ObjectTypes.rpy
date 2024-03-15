init -1 python:
    from enum import Enum

    #these are releveant when the object is in a location if its in your inventory these are meaningless, though inside would be fine
    class relativelocation(Enum):
        none = 0
        inside = 1
        ontop = 2
        under = 3
        inarea = 4

    class relativelocationlists(Enum):
        none = 0
        objectsinside = 1
        objectsontop = 2
        objectsunder = 3
        objectsinarea = 4


    class scope(Enum):
        none = 0
        inventory = 1
        location = 2

    class pose(Enum):
        standing = 0
        sitting = 1
        layingdown = 2

    class ItemTooltip(object):    
        @dispatch (str)
        def __init__(self,tooltip):
            self.identifier = ""
            self.tooltip = tooltip
            self.icon = "defaulttooltip.png"

        @dispatch (str,str)
        def __init__(self,tooltip,icon):
            self.identifier = ""
            self.tooltip = tooltip
            self.icon = icon

        @dispatch (str,str,str)
        def __init__(self,tooltip,icon,identifier):
            self.identifier = identifier
            self.tooltip = tooltip
            self.icon = icon

    class ViewSortIcon(object):
        def __init__(self,icon,tooltip,headertext,viewliststr):
            self.icon = icon
            self.tooltip = tooltip
            self.headertext = headertext
            self.viewliststr = viewliststr

    #Object Inheritance Types
    #important philosophy
    #if a property is changed that would cause the object to need to update its displayname or spacing text, then the object itself's getter setter
    #should handle calling setdisplayname
    class DisplayObject(object):
        
        @property
        def displayspacing(self):
            #say("","getter method called")
            return self._displayspacing

        @displayspacing.setter
        def displayspacing(self,num):
            #smartlog("Spacing updated on " + self.name+" to "+str(self.displayspacing))
            self._displayspacing = num
            self.setdisplayname()

        @property
        def count(self):
            return self._count

        @count.setter
        def count(self,num):
            self._count = num
            self.setdisplayname()

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self,obj):
            if self._parent is not None:
                self._parent.setdisplayname()
            self._parent = obj
            if self._parent is not None:
                self._parent.setdisplayname()
            self.setspacing()
            self.setdisplayname()

        @property
        def scope(self):
            return self._scope

        @scope.setter
        def scope(self,scop):
            self._scope = scop
            if hasattr(self,"OnScopeChanged"):
                self.OnScopeChanged(scop)

        @property
        def isvisible(self):
            return self._isvisible

        @isvisible.setter
        def isvisible(self,bool):
            if not self.flag("ishidden"):
                self._isvisible = bool
            else:
                return
        
        def setdisplayname(self):
            #smartlog("","Changing display of "+self.name + " display spacing is "+str(self.displayspacing))
            displayname = ""
            #smartlog("The spacing on " + self.name+" is "+str(self.displayspacing))
            spacingtext = ""
            for i in range(0,self.displayspacing):
                spacingtext += "      "
            #for tooltip in self.beforetooltips:
                #spacingtext = spacingtext[0:-4]
            #spacingtext = spacingtext +"|" 
            if not self.ininventory:
                if hasattr(self,"relativelocation"):
                    if self.relativelocation == relativelocation.ontop:
                        spacingtext = spacingtext+"↑"
                    elif self.relativelocation == relativelocation.under:
                        spacingtext = spacingtext+"↓"
                    elif self.relativelocation == relativelocation.inarea:
                        spacingtext = spacingtext+""
                    else: self.spacingtext = spacingtext+"⟵"

            if hasattr(self,"iscontainer") and len(self.objectsinside) > 0 and not self.issecretcontainer:
                if self.isopen:
                    spacingtext = spacingtext+"v"
                else:
                    spacingtext = spacingtext+">"

            self.spacingtext = spacingtext

            if self.flag("isinteractionarea") or self.flag("isinteractionlocation") or (self.flag("isineractionobject") and not self.flag("ininventory")):
                if self.playerpresent:
                    displayname = displayname + "{color=000}"+string.capwords(self.name)+"{/color}"
                else:
                    displayname = displayname + "{color=fff}"+string.capwords(self.name)+"{/color}"
     
            elif hasattr(self,"iswearable"):
                displayname = displayname + ProcessText("(=if this.showcolor:(=this.color=) =)(=this.name!C=)(=if this.isworn: (worn)=)",self)
            else:
                displayname = displayname + string.capwords(self.name)

            if self.count >1:
                displayname = displayname +" x"+ str(self.count)
            elif hasattr(self,"containedgold") and self.goldknown:
                if self.containedgold > 0:
                    displayname = displayname + " (" +str(self.containedgold)+ " gold)"
                else:
                    displayname = displayname + " (empty)"

            #else: displayname = displayname + ProcessText("(=this.name=)",self)

            self.displayname = displayname

        def setspacing(self):
            if self.parent is not None and not isinstance(self.parent,Location):
                self.displayspacing = self.parent.displayspacing + 1         
            return
        
        #removes a tooltip by identifier, checks both the beforetooltips and aftertooltips. Returns the index of the removed tooltip or -1 if nothing removed
        def removetooltip(self,identifier):
            index = 0
            for tooltip in self.beforetooltips:
                if tooltip.identifier == identifier:
                    del self.beforetooltips[index]
                    return index
                index += 1
            index = 0 
            for tooltip in self.aftertooltips:
                if tooltip.identifier == identifier:
                    del self.aftertooltips[index]
                    return index
                index += 1
            return -1

        #this returns true if this object has a boolean property "flagname" and that flag is true or false otherwise
        def flag(self,flagname):
            if hasattr(self,flagname) and getattr(self,flagname) == True:
                return True
            return False

        def hasattr(self,attributename):
            return hasattr(self,attributename)
                
        def __init__(self):
            if not hasattr(self,"fullyinitialized"): #this check just prevents us from setting these default values multiple times and thus possibly saving some time
                #if we are inheriting multiple objects that in turn inherit from display object (a common case)
                self.name = ""
                self.simplename = ""
                self.displayname =""
                self.spacingtext = ""
                self.isvisible = True
                #self.parentvisible = True #if this is false, then isvisible has to be false
                self.childrenvisible = True #change this when the object changes its own visibility, and use this whenever its parent object updates visiblity
                self.locationverbs = []
                self.currentverbs = []
                self._displayspacing = 0
                self._count = 1
                self._parent = None
                self.cancombine=True #if this is true we can combine and stack the item where ever it is, or else it cant be combined
                self.incontainer = False
                self.ininventory = False
                self.beforetooltips = []
                self.aftertooltips = []
                self.isfavorite = False #starts unfoavorited
                self.listlocation = None #this will be set at initialization of what list the object is in relative to its parent in location
                self.scope = scope.none #by default we assume all objects start nowhere. Initialize can set them to start in the inventory
                self.favoritelistin = None #starts not in a any favorites list
                self.isnpc = False
                self.article = "the "
                #global locationitems
                self.scopelist = None #this will be if the object is in the inventory or a location
                self.fullyinitialized = True

        #this copy override is here because some variables need to keep their references while others should absolutely not, so we can pick and choose here
        #note that this does NOT place the object anywhere visible. It must be moved after
        def __copy__(self):
            #smartlog("copying")
            cls = self.__class__
            result = cls.__new__(cls)
            result.__dict__.update(self.__dict__)
            result.beforetooltips = self.beforetooltips.copy()
            result.aftertooltips = self.aftertooltips.copy()

            return result
        


    #this is for any item that the take verb can be used on to get infinite items from (or possibly a limit, if you choose) as long as it takes a copy, its cloneable
    class Cloneable(DisplayObject):
        #idnum = 0

        def __init__(self):
            DisplayObject.__init__(self)
            self.id = 0
            self.iscloneable = True
            self.isoriginal = True

        #clones itself appropriately, and uses related cloning properties. The clone object is counted as being in no scope by default
        def clone(self, trashable = True):
            result = copy.copy(self) #calls DisplayObject__copy__
            global clonedobjectid
            clonedobjectid += 1
            result.id = clonedobjectid
            result.isoriginal = False
            result.scope = scope.none
            result.listlocation = None
            result.favoritelistin = None
            if trashable:
                result.trashable = True
            return result

    #a container is an object that can have other objects INSIDE of it, if they are ontop of it or around it, They are something else.
    class Container(DisplayObject):
        @property
        def isopen(self):
            return self._isopen

        @isopen.setter
        def isopen(self,bool):
            if self.fullyinitialized:
                self._isopen = bool
                self.setdisplayname()

        @property
        def issecretcontainer(self):
            return self._issecretcontainer

        @issecretcontainer.setter
        def issecretcontainer(self,bool):
            if self.fullyinitialized:
                self._issecretcontainer = bool
                if not self._issecretcontainer:
                    #it is no longer a secret container
                    if self.isopen:
                        self.currentverbs.append(self.closeverb)
                    else:
                        self.currentverbs.append(self.openverb)
                else:
                    #it is now a secret container. Remove those verbs
                    scopeoptions = list(scop.name for scop in scope)
                    scopeoptions[0] = "current"
                    for scop in scopeoptions:
                        if hasattr(self,scop+"verbs"): 
                            vlist = getattr(self,scop+"verbs")
                            if self.closeverb in vlist: vlist.remove(self.closeverb)
                            if self.openverb in vlist: vlist.remove(self.openverb)
                self.setdisplayname()

        def __init__(self):
            self.iscontainer = True
            self._isopen = False
            self.objectsinside = []
            self._issecretcontainer = False
            self.openverb = "Open"
            self.closeverb = "Close"
            self.openmsg = ""
            self.closemsg = ""

        def lastindexinscope(self):
            if self.objectsinside:
                return self.scopelist.index(self.objectsinside[-1])
            return self.scopelist.index(self)

    
    class Wearable(DisplayObject):
        @property
        def isworn(self):
            #say("","getter method called")
            return self._isworn

        @isworn.setter
        def isworn(self,boo):
            #say("","it is set. lol this is inherited xd")
            self._isworn = boo
            self.setdisplayname()

        def __init__(self):
            DisplayObject.__init__(self)
            self.iswearable = True
            self.iscolorable = True
            self.isdesignable = True
            self.hasdesign = False
            self.design = ""
            self.hascolor = False
            self.color = ""
            self.clothingtype = ""
            self.clothingname = ""
            self.ishat = False
            self.isneckware = False
            self.isshirt = False
            self.isbra = False
            self.isgloves = False
            self.ispants = False
            self.issocks = False
            self.isshoes = False
            self.wornverbs = []

            self.showcolor = False
            self._isworn = False
            self.plural = False

            self.inventoryverbs = ["Drop","Wear","Examine"]
            self.wornverbs = ["Remove","Examine"]

    class Location(DisplayObject):
        def __init__(self):
            DisplayObject.__init__(self)

            self.isready = False
            self.defaultinteractionarea = None
            self.interactionareas = []
            self.volume = 3000
            self.flattenedlist = [] #this property will only be messed with when changing rooms. This is where we can store stuff.
            self.favorites = []

    class InteractionArea(DisplayObject):
        @property 
        def playerpresent(self):
            #smartlog("{color=ff0}player present getter{/color}")
            return self._playerpresent

        @playerpresent.setter
        def playerpresent(self,boo):
            if boo:
                #playerpresent   
                #if player.mostspecificlocation == self:
                    #self.beforetooltips.append(ItemTooltip("You are here","playerheretooltip.png","playerpresent"))
                    #self.locationverbs.remove("Go")
                if not self.childrenvisible:
                    OnShowFurnitureInMenu(self)
            else:
                pass
                #self.removetooltip("playerpresent")
                #self.locationverbs.insert(0,"Go")
            self._playerpresent = boo
            self.setdisplayname()

        
        def __init__(self):
            DisplayObject.__init__(self)

            self.isinteractionarea = True
            self.puddlevolume = 0 
            self.avoidablevolume = 0
            self._playerpresent = False
            self.puddleavoidable = False
            #self.showfurniture = False #Not needed as this is a container now
            self.interactionlocations = []
            self.objectsinarea= [] #Objects that are in the area but not at any specific interaction location.
            self.canlaydown = True

        #attempts to get the last child of this object in the order they would appear in the view lists. So if there is none the object itself is the last child
        def getLastChild(self) -> 'object':
            if self.objectsinarea:
                return self.objectsinarea[-1]
            elif self.interactionlocations:
                return self.interactionlocations[-1].getLastChild()
            return self

        #def lastindexinscope(self,scope):
            #if scope == scope.


    
    class InteractionLocation(DisplayObject):
        @property 
        def playerpresent(self):
            #smartlog("{color=ff0}player present getter{/color}")
            return self._playerpresent
            #smartlog("","player present getter")

        @playerpresent.setter
        def playerpresent(self,boo):
            #smartlog("{color=ff0}updating " +self.name+"{/color}")
            if boo:
                #playerpresent
                #if player.mostspecificlocation == self:
                    #self.beforetooltips.append(ItemTooltip("You are here","playerheretooltip.png","playerpresent"))
                    #self.locationverbs.remove("Go")
                if self.flag("iscontainer") and not self.flag("isopen"):
                    Open(self, log = False)
                if self.parent != None:
                    self.parent.playerpresent = True
            else:
                if self.parent != None:
                    self.parent.playerpresent = False
                #self.removetooltip("playerpresent")
                #self.locationverbs.insert(0,"Go")
            self._playerpresent = boo
            self.setdisplayname()


        def __init__(self):
            DisplayObject.__init__(self)

            self.isinteractionlocation = True
            self.objectsontop = [] #Objects that have been set on top of this object
            self.objectsunder = [] #Objects that are under this object
            self.objectsinarea= [] #objects in the general vicinity of this interaction location
            self._playerpresent = False

            self.puddlevolume = 0 
            self.avoidablevolume = 0
            self.puddleavoidable = False

        #attempts to get the last child of this object in the order they would appear in the view lists (farthest down). So if there is none the object itself is the last child
        def getLastChild(self) -> 'object':
            #objects in area is farthest
            if self.objectsinarea:
                return self.objectsinarea[-1]
            elif self.objectsunder:
                return self.objectsunder[-1]
            elif self.objectsontop:
                return self.objectsontop[-1]
            #contained items would be nearest (if this is a container)
            elif self.flag("iscontainer") and self.objectsinside:
                return self.objectsinside[-1]
            return self

        def lastindexontop(self):
            if self.objectsontop:
                return self.scopelist.index(self.objectsontop[-1])
            if self.flag("iscontainer"):
                return Container.lastindexinscope()
            return self.scopelist(self)

        def lastindexunder(self):
            if self.objectsunder:
                return self.scopelist.index(self.objectsunder[-1])
            return self.lastindexontop()

        def lastindexinarea(self):
            if self.objectsinarea:
                return self.scopelist.index(self.objectsinarea[-1])
            return self.lastindexunder(self)

        def lastindexinscope(self,scope):
            if scope == scope.inside:
                return Container.lastindexinscope(self)
            elif scope == scope.ontop:
                return self.lastindexontop()
            elif scope == scope.under:
                return self.lastindexunder()
            elif scope == scope.inarea:
                return self.lastindexunder()
            return -1
   
    class InteractionObject(DisplayObject):
        @property 
        def playerpresent(self):
            #smartlog("{color=ff0}player present getter{/color}")
            return self._playerpresent

        @playerpresent.setter
        def playerpresent(self,boo):
            if boo:
                #playerpresent
                #if player.mostspecificlocation == self:
                    #self.beforetooltips.append(ItemTooltip("You are here","playerheretooltip.png","playerpresent"))
                    #self.locationverbs.remove("Go")
                if self.flag("iscontainer") and not self.flag("isopen"):
                    OnOpen(self)
                if self.parent != None:
                    self.parent.playerpresent = True
            else:
                if self.parent != None:
                    self.parent.playerpresent = False
                #self.removetooltip("playerpresent")
                #self.locationverbs.insert(0,"Go")
            self._playerpresent = boo
            self.setdisplayname()

        def __init__(self):
            DisplayObject.__init__(self)

            self.isinteractionobject = True
            self.inventoryverbs = []
            self.ininventory = False
            self.displayname = ""
            self.displaycolor = ""  
            self.playerpresent = False   
            self.trashable = True

    class NoneItem(DisplayObject):
        def __init__(self,name):
            DisplayObject.__init__(self)
            self.isnothing = True

            self.name=name
            self.displayname = name     
            self.currentverbs = []
            self.wornverbs = []
            self.cantclick = True

    class LocationConnector(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)
            self.islocationconnector = True
            self.otherlocationname = ""
            self.locked = False
            self.type = "door"

            self.lockedmessage = "its locked"
            self.entermessage = ""

    class NPC(InteractionObject):
        def __init__(self):
            InteractionObject.__init__(self)

            self.nameisproper = True
            self.isnpc=True
            self.canaccessinventory = False
            self.inventory = []
            self.who_color = '#0099cc'
            self.trashable = False

    class CoinBag(InteractionObject):
        @property
        def containedgold(self):
            return self._containedgold

        @containedgold.setter
        def containedgold(self,gold):
            self._containedgold = gold
            self.setdisplayname()


        def __init__(self,gold):
            InteractionObject.__init__(self)

            self.simplename = "CoinBag"
            self.name = "Coin Bag" 
            self.displayname = "Coin Bag"
            self.goldknown = False #order matters
            self.containedgold = gold  #order matters
            self.playerlooted = False

            self.locationverbs = ["Examine","Take"]
            self.currentverbs = ["Examine","Take"]
            self.inventoryverbs = ["Examine","Drop"]

        # def OnScopeChanged(self,scope):
        #     if scope == scope.inventory:
        #         self.goldknown = True
        #         self.setdisplayname()

        def OnAfterExamine(self):
            self.goldknown = True
            self.setdisplayname()

        @Verb #OnTake
        def OnTake(self):
            global inventoryitems
            for item in inventoryitems:
                if item.name == "Coin Bag":
                    if self.containedgold != 0:
                        smartlog("You take the "+str(self.containedgold) +" gold and add it to your own gold bag")
                        item.containedgold += self.containedgold
                        self.containedgold = 0
                        self.playerlooted = True
                    else:
                        if self.playerlooted:
                            smartlog("You already took the gold from this one...")
                        else:
                            smartlog("Nothing in here. Darn.")
                    return
            #player has no gold bag yet
            MoveToInventory(self)
            self.goldknown = True
            self.setdisplayname()
            phrase = ""
            if self.containedgold >1000:
                phrase = "thats a pretty hefty sum of gold!"
            elif self.containedgold > 500:
                phrase = "not too bad"
            elif self.containedgold > 200:
                phrase = "an alright amount"
            elif self.containedgold > 0:
                phrase = "not too much, but better than nothing"
            else:
                phrase = "it would have been better if there was actually gold in there...but I guess at least you got the bag"
            smartlog("You take the gold bag and all of its contents. "+str(self.containedgold)+" gold, "+phrase)
        
        @Verb #OnExamine
        def OnExamine(self):
            smartlog("Examine "+self.name)
            smartlog( "its a coin bag with "+str(self.containedgold)+" gold.")
    
 
