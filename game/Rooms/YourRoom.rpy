init python:
    class YourRoom_Bed(InteractionLocation): 
        def __init__(self):     
            InteractionLocation.__init__(self)
            self.simplename = "Bed"
            self.name = "Bed" 
            self.displayname = "Bed"

            self.size = "King"
            self.hassheets = True
            self.sheetscolor = "Brown"
            self.hasmatresscover = True
            self.matresscovercolor = "White"
            #self.hasmatressprotector = False
            #self.matressprotectorcolor = "Pink"
            self.pillowcount = 1
            self.pillowcolor = "White"
            self.pilloworganization = "Neat"
            self.bedmade = True
            self.topmostsheetscolor = "Brown"
            self.topmostmatresscolor = "White"

            self.canlaydown = True

            self.locationverbs = ["Go","Examine","Sleep"]
            self.currentverbs = ["Go","Examine","Sleep"]
            
    class YourRoom_Candle(InteractionObject):
        def __init__(self):
            InteractionObject.__init__(self)
            self.simplename = "Candle"
            self.name = "Candle" 
            self.displayname = "Candle"
            self.islit = False

            self.locationverbs = ["Examine","Light"]
            self.currentverbs = ["Examine","Light"]
            
    
    class Tunic(InteractionObject,Wearable):
        def __init__(self):
            InteractionObject.__init__(self)
            Wearable.__init__(self)

            self.simplename = "Tunic"
            self.name = "Tunic" 
            self.displayname = "Brown Tunic"
            self.color = "Brown"
            self.showcolor = True

            self.locationverbs = ["Examine","Take"]
            self.currentverbs = ["Examine","Take"]

    class LinenPants(InteractionObject,Wearable):
        def __init__(self):
            InteractionObject.__init__(self)
            Wearable.__init__(self)

            self.simplename = "LinenPants"
            self.name = "Linen Pants" 
            self.displayname = "Linen Pants"
            self.color = "Brown"
            self.plural = True

            self.locationverbs = ["Examine","Take"]
            self.currentverbs = ["Examine","Take"]
    
    class WoolSocks(InteractionObject,Wearable):
        def __init__(self):
            InteractionObject.__init__(self)
            Wearable.__init__(self)

            self.simplename = "WoolSocks"
            self.name = "Wool Socks" 
            self.displayname = "Wool Socks"
            self.color = "White"
            self.plural = True

            self.locationverbs = ["Examine","Take"]
            self.currentverbs = ["Examine","Take"]

            
    class YourRoom_Dresser(InteractionLocation,Container):
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)

            self.simplename = "Dresser"
            self.name = "Dresser" 
            self.displayname = "Dresser"
            self.objectsinside = [Tunic(),LinenPants(),WoolSocks()]
            self.objectsontop = [YourRoom_Candle(),CoinBag(1078)]
            self.isopen = False

            self.locationverbs = ["Go","Examine","Open"]
            self.currentverbs = ["Go","Examine","Open"]

    class YourRoom_Door(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)

            self.name = "Door"
            self.locationverbs = ["Exit","Go"]
            self.otherlocationname = "Hallway"
            self.article = "the "


    class YourRoom_Everything(InteractionArea):
        def __init__(self):
            InteractionArea.__init__(self)

            self.simplename = "Everything"
            self.name = "Everything"
            self.displayname = "Everything"
            self.locationverbs = ["Go","Hide Furniture In Menu"]
            self.currentverbs = ["Go","Hide Furniture In Menu"]
            self.interactionlocations = [YourRoom_Bed(),YourRoom_Dresser(),YourRoom_Door()]
        
    class YourRoom(Location):
        def __init__(self):
            Location.__init__(self)
            
            self.simplename = "YourRoom"
            self.name = "Your Room"
            self.displayname = "Your Room"
            self.interactionareas = [YourRoom_Everything()]
            self.defaultinteractionarea = self.interactionareas[0]


