        
init python:      
    class YourRoom_Door2(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)

            self.name = "Door to your room"
            self.locationverbs = ["Enter","Go"]
            self.otherlocationname = "Your Room"

    class Roommate1Door(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)
            #if its a 2 or more word proper name make sure capitalization is proper because proper names ignore capitalization or uncapitalization in most cases
            self.name = "Mark's door"
            self.nameisproper = True
            self.locationverbs = ["Enter","Go"]
            self.locked = True
            self.otherlocationname = ""
  
    class Roommate2Door(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)

            self.name = "Alisson's door"
            self.locationverbs = ["Enter","Go"]
            self.nameisproper = True
            self.locked = True
            self.otherlocationname = ""
            
    
    class Hallway_CoinBag(CoinBag):
        def __init__(self):
            CoinBag.__init__(self,327)
            self.isvisible = False
            self.hasbeenininventory = False

        @Verb #OnExamine
        def OnExamine(self):
            if self.scope != scope.inventory and not self.hasbeenininventory:
                if self.containedgold > 0:
                    self.examinestring = "What is that even doing there...and why is there "+str(self.containedgold)+" gold in it???"
                else:
                    self.examinestring = "What is that even doing there..."
                smartlog(self.examinestring)
            else:
                smartlog( "its a coin bag with "+str(self.containedgold)+" gold.")
                
        def OnScopeChanged(self,scop):
            if scop == scope.inventory:
                self.hasbeenininventory = True

  
    class Hallway_PottedPlant(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)
            self.simplename = "PottedPlant"
            self.name = "Potted Plant" 
            self.displayname = "Potted Plant"
            self.objectsontop = [Hallway_CoinBag()]
            self.issecretcontainer = True

            self.locationverbs = ["Go","Examine"]
            self.currentverbs = ["Go","Examine"]

            self.examinecount = 0

        @Verb #OnExamine
        def OnExamine(self):
            smartlog("Examine "+self.name)
            if self.examinecount == 0:
                smartlog("it seems like just a normal potted plant...")
            elif self.examinecount == 1:
                smartlog("but there is something off about it...")
            elif self.examinecount == 2:
                smartlog("Maybe if you keep on looking at it you might figure something out...")
            elif self.examinecount == 3:
                smartlog("or not.")
            elif self.examinecount == 4:
                smartlog("But you kept on doing it anyway and your persistence rewards you! There was nothing wrong with the plant but there was a pouch full of gold tucked among the greenery!")
                self.objectsontop[0].isvisible = True
            else:
                smartlog("Ah alas that is all there is to see for real. You wont find anything else here.")
            self.examinecount += 1

    class Hallway_LivingRoomConnector(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)

            self.name = "Living Room"
            self.locationverbs = ["Enter","Go"]
            self.otherlocationname = "Main Room"
            self.entermessage = "You walk into the living room! Or, rather, the livingroom/frontroom/kitchen..."

    class Hallway_Everything(InteractionArea):
        def __init__(self):
            InteractionArea.__init__(self)

            self.simplename = "Everything"
            self.name = "Everything"
            self.displayname = "Everything"
            self.locationverbs = ["Go","Hide Furniture In Menu"]
            self.currentverbs = ["Go","Hide Furniture In Menu"]
            self.interactionlocations = [Roommate1Door(),Roommate2Door(),YourRoom_Door2(),Hallway_PottedPlant(),Hallway_LivingRoomConnector()]
        
    class Hallway(Location):
        def __init__(self):
            Location.__init__(self)
            
            self.simplename = "Hallway"
            self.name = "Hallway"
            self.displayname = "Hallway"
            self.interactionareas = [Hallway_Everything()]
            self.defaultinteractionarea = self.interactionareas[0]
