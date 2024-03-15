init python:  

    class FrontDoor(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)
            self.locked = True

            self.name = "Front Door"
            self.locationverbs = ["Enter","Go"]
            self.otherlocationname = "Hallway"
            self.entermessage = "You walk into back into the hallway." 

    #class Nick(NPC): 

    class MarkandAllison(NPC):
        def __init__(self):
            NPC.__init__(self)
    
            self.nameisproper = True
            self.isnpc=True
            self.canaccessinventory = False
            self.inventory = []
            self.who_color = '#0099cc'
            self.trashable = False
            self.name = "Mark and Allison"
            self.talkedcount = 0

            self.locationverbs = ["Talk"]

        @Verb #OnTalk
        @AvoidIfSay
        def OnTalk(self):
            if self.talkedcount == 0:
                smartsay("Mark", "Hey how is it going? I hope you enjoyed the Coding Proficiency Demo")
                smartsay("You", "What are you talking about?")
                smartsay("Allison", "You know the Coding Proficiency Demo with only 3 rooms that you are currently in? Did you manage to find both coin bags?")
                smartsay("Allison", "The first one is easy to find but the second one not so much!")
                coinbag = None
                for item in inventoryitems:
                    if item.name == "Coin Bag":
                        coinbag = item
                if coinbag is None:
                    smartsay("You", "No I didnt even find one of them...or at least I didnt take it, because its rude to take perfectly good money thats just sitting around")
                    smartsay("Allison", "I guess thats a fair point")
                elif coinbag.containedgold < 800:
                    smartsay("You", "Well I found a weird one in a plant but I didnt find another one... or at least I didnt take it.")
                    smartsay("Allison", "Wow nice job that one is tricky to find")
                elif coinbag.containedgold <1200:
                    smartsay("You", "Of course I took the one in my room, but what do you mean there is another one?")
                    smartsay("Allison", "I'll give you a hint its in the hallway!")
                else:
                    smartsay("You", "Obviously I got both of them. It was easy.")
                    smartsay("Mark", "Nice Job!")
                    smartsay("Allison", "Great work!")
                smartsay("Allison", "Well anyway regardless of that-")
                smartsay("You", "Are we still gonna ignore the thing about the Coding Proficiency Demo???")
                smartsay("Allison", "-I really hope you enjoyed!")
                smartsay("Mark", "We know it doesnt look like a whole lot but I encourage you to look at the code on the github and check out all the intricacies")
                smartsay("Nick", "Yeah I really put a lot of work into this")
                smartsay("You", "Wait who are you and how did you get into my house...err apartment? Whatever this is...")
                smartsay("Nick", "I created you")
                smartsay("Nick", "Or at least your speech and your ability to interact with this world")
                smartsay("You", "Wha-")
                smartsay("Nick", "So anyways, feel free to take a look at the code, and keep in mind, that if this looks like a lot of code for the amount of content,")
                smartsay("Nick", "it probably is! But thats not the point, the point is that the code should be quite flexible, dynamic, and fast.")
                smartsay("Nick", "It was written, to the best of my ability with two purposes in mind. To be efficient and to be make future additions as easy as possible")
                smartsay("Nick", "And what I mean by this is that the code should be fast, there are even some parts (especially with the UI) that exist")
                smartsay("Nick", "just to speed the game up as much as possible, the main example being the seperateintolines(text) function, which, ill admit")
                smartsay("Nick", "took a while to do and maybe could have done better than the guess and check method I implemented but I simply could not find any")
                smartsay("Nick", "way to mathmatically calculate the size of the text rather than to repeatedly draw and guess and check it. I dont believe renpy")
                smartsay("Nick", "offers a way to do that. Oh and if you didnt catch why this function makes the program faster, its because it allows me to use")
                smartsay("Nick", "a VPgrid displayable to display the text as opposed to just a normal view, which is only possible because the text is split into lines.")
                smartsay("Nick", "Oh and as for why this should be easy to expand on, with a lot of the technically complex functions done, such as moving objects to")
                smartsay("Nick", "different scopes and the UI elements allowing you to only show specific categories at once (such as favorites), its actually quite easy")
                smartsay("Nick", "to add more of those categories and more objects simply by inheriting from the large amount of base objects and defining a few properties")
                smartsay("Nick", "and any desired \"override\" behavior for verbs, that is, having the verb do something it wouldnt generically do")
                smartsay("Nick", "and then you could of course, still call the generic verb afterwords, or, even just write an \"OnAfter*verb*\" function that would be called")
                smartsay("Nick", "after the verb is finished automatically! And if you want any more insight like this again, please look at the code. Ive commented and made notes")
                smartsay("Nick", "on a lot of it and in some cases left depracted or unused code commented out so you can see my coding process. Oh and some implemented features")
                smartsay("Nick", "may not have shown up in this demo and those would be in the code too!")
                smartsay("Nick", "And one last thing, this is my very first project written in python, and my first time using renpy, so this project is both me learning both of those")
                smartsay("Nick", "while also showing off my general coding skills, because at the end of the day python is just another programming language.")
                smartsay("Nick", "And with my prior experince in C#, java, lua, and a few other languages, it was fairly easy to translate that to this! And hopefully it shows.")
                smartsay("Nick", "Thats all I got, I hope you enjoyed!")
                smartlog("Nick then leaves")
                smartsay("Mark", "What a great guy...")
                smartsay("Allison", "Yeah...")
                smartsay("You", "*insert my (your) thoughts on the situation here*")
                smartsay("You", "Ok guess ill just pretend that didnt happen...")
            elif self.talkedcount == 1:
                smartsay("You", "so uhh, remember that guy who just came in here and started talking about some coding thing earlier?")
                smartsay("Mark", "Nope")
                smartsay("Allison", "No idea who you are talking about")
            elif self.talkedcount == 2:
                smartsay("You", "You sure you dont remember?")
                smartsay("Mark", "Yup")
                smartsay("Allison", "Positive")
            elif self.talkedcount == 3:
                smartsay("You", "But like, are you really su-")
                smartsay("Mark", "Man you are crazy")
                smartsay("Allison", "I think we would remember something like that")
            else:
                smartsay("You", "...")
                smartsay("Mark", "...")
                smartsay("Allison", "...")
            self.talkedcount += 1


    class Couch(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)

            self.simplename = "Couch"
            self.name = "Couch" 
            self.maxpeople = 3
            self.currentpeople = 2 

            self.locationverbs = ["Go","Examine","Sit","Wait"]
            self.objectsontop = [MarkandAllison()]

    class CoffeeTable(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)

            self.simplename = "Table"
            self.name = "Table" 

            self.locationverbs = ["Go","Examine"]

    class TV(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)

            self.simplename = "TV"
            self.name = "TV" 
            self.ison = True

            self.locationverbs = ["Go","Examine","Turn Off"]

        def OnExamine(self):
            if self.ison:
                smartlog("Its a nice 48' tv. It is currently on")
            else:
                smartlog("Its a nice 48' tv. It is currently off")

 

    class LivingRoom(InteractionArea):
        def __init__(self):
            InteractionArea.__init__(self)

            self.simplename = "LivingRoom"
            self.name = "Living Room"
            self.locationverbs = ["Go","Hide Furniture In Menu"]
            self.currentverbs = ["Go","Hide Furniture In Menu"]
            self.interactionlocations = [FrontDoor(),Couch(),CoffeeTable(),TV()]

    class Oven(InteractionLocation,Container):
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)
            self.simplename = "Oven"
            self.name = "Oven" 
            self.displayname = "Oven"
            self.objectsinside = []

            self.locationverbs = ["Go","Examine"]
            self.currentverbs = ["Go","Examine"]

    class Apple(InteractionObject,Cloneable):
        def __init__(self):
            InteractionObject.__init__(self)
            Cloneable.__init__(self)
            self.name = "Apple" 
            self.displayname = "Apple"
            self.pluralname = "Apples"

            self.locationverbs = ["Examine","Take","Eat"]
            self.currentverbs = ["Examine","Take"]
            self.inventoryverbs = ["Examine","Eat","Drop"]

    class Fruitbowl(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)
            self.name = "Fruit Bowl" 
            self.displayname = "Fruit Bowl"

            self.locationverbs = ["Examine","Take Fruit"]
            self.currentverbs = ["Examine","Take Fruit"]
            self.takecount = 0
            self.baseapple = Apple() 

        @Verb #OnTakeFruit
        def OnTakeFruit(self):
            if self.takecount <1:
                smartlog("You take an apple")
            elif self.takecount <4:
                smartlog("You take another apple")
            elif self.takecount <7:
                smartlog("You take another apple...wait how many apples are in here?")
            elif self.takecount <11:
                smartlog("You just keep taking apples...")
            elif self.takecount <21:
                smartlog("They just dont stop coming")
            else:
                smartlog("This is complete and utter insanity")
            self.takecount += 1
            MoveToInventory(self.baseapple.clone())

    class Chair(InteractionLocation):
        def __init__(self, identifier = ""):
            InteractionLocation.__init__(self)
            self.name = "Chair"
            if identifier != "":
                self.identifier = identifier
            self.maxpeople = 1
            self.currentpeople = 0 

            self.locationverbs = ["Go","Examine", "Sit"]

    class Counter(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)
            self.simplename = "Counter"
            self.name = "Counter" 
            self.displayname = "Counter"
            self.objectsontop = [Fruitbowl()]
            self.objectsinarea = [Chair(identifier = "Chair1"),Chair(identifier = "Chair2"),Chair(identifier = "Chair3")]

            self.locationverbs = ["Go","Examine"]
            self.currentverbs = ["Go","Examine"]

    class Pantry(InteractionLocation,Container):
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)
            self.simplename = "Pantry"
            self.name = "Pantry" 
            self.displayname = "Pantry"
            self.objectsinside = []

            self.locationverbs = ["Go","Examine","Open"]
            self.currentverbs = ["Go","Examine","Open"]

    class Fridge(InteractionLocation,Container):
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)
            self.simplename = "Fridge"
            self.name = "Fridge" 
            self.displayname = "Fridge"
            self.objectsinside = []

            self.locationverbs = ["Go","Examine","Open"]
            self.currentverbs = ["Go","Examine","Open"]  

    class TrashCan(InteractionLocation,Container):   
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)
            self.name = "Trash" 
            self.displayname = "Trash"
            self.objectsinside = []

            self.locationverbs = ["Examine","Throw Away","Empty","Open"]  

    class Sink(InteractionLocation):
        def __init__(self):
            InteractionLocation.__init__(self)
            Container.__init__(self)
            self.name = "Sink" 
            self.displayname = "Sink"
            self.objectsunder = [TrashCan()]

            self.locationverbs = ["Go","Examine","Wash Hands"]
            self.currentverbs = ["Go","Examine","Wash Hands"] 


    class Kitchen(InteractionArea):
        def __init__(self):
            InteractionArea.__init__(self)

            self.simplename = "Kitchen"
            self.name = "Kitchen"
            self.locationverbs = ["Go","Hide Furniture In Menu"]
            self.currentverbs = ["Go","Hide Furniture In Menu"]
            self.interactionlocations = [Oven(),Counter(),Pantry(),Fridge(),Sink()]

    class LivingRoom_HallwayConnector(LocationConnector):
        def __init__(self):
            LocationConnector.__init__(self)

            self.name = "Hallway"
            self.locationverbs = ["Enter","Go"]
            self.otherlocationname = "Hallway"
            self.entermessage = "You walk into back into the hallway."

    class Connector(InteractionArea):
        def __init__(self):
            InteractionArea.__init__(self)

            self.simplename = "Connector"
            self.name = "Connector"
            self.locationverbs = ["Go","Hide Furniture In Menu"]
            self.currentverbs = ["Go","Hide Furniture In Menu"]
            self.interactionlocations = [LivingRoom_HallwayConnector()]

    class MainRoom(Location):
        def __init__(self):
            Location.__init__(self)
            
            self.simplename = "MainRoom"
            self.name = "Main Room"
            self.displayname = "Main Room"
            self.interactionareas = [LivingRoom(),Kitchen(),Connector()]
            self.defaultinteractionarea = self.interactionareas[2]
