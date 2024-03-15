init python:
    class ARCustom1():
        def __init__(self):
            self.Examine = {
                "Examine_Bed" : "Its a (=self.size=) size bed. It is (=self.topmostmatresscolor=) with (=self.topmostsheetscolor=) sheets (=if self.bedmade:and it has been made. Nice and cozy=)(=if not self.bedmade:but it is not made and kind of messy=).",
                "Examine_Wearable" : "Its (=if self.plural:a pair of =)(=if not self.plural:a =)(=self.name=). (=if self.plural:they are =)(=if not self.plural:it is =)(=self.color=).",
                "Examine_Candle" : "its a wax candle. You have read many books at night with the light from this candle. (=if self.islit:It is currently lit and illuminating your dresser and the surrounding area=)(=if not self.islit:It is not lit=).",
                "Examine_Dresser" : "Its a plain wooden dresser. This is where you keep your clothes.",
                "Examine_Oven" : "Its just a plain old oven with a stovetop. Its not currently on and you dont feel like turning it on.",
                "Examine_Counter": "A nice granite counter. Its a nice place to eat.",
                "Examine_Pantry": "This is where you and your roomates keep various cereals, snackfoods, pastas, sodas, and other, well, food. What else did you expect?",
                "Examine_Fridge": "This is a state of the art smartfridge! Complete with touchscreen, icecube dispenser, and other smartfridge stuff...although none of that stuff works right now... \noh and if you were wondering, the freezer is at the bottom.",
                "Examine_Tunic" : "Its a (=self.name=). it is (=self.color=). What, why shouldnt I be able to own a tunic?",
                "Examine_Sink" : "Its a kitchen sink. Great for washing your hands or the dishes.",
                "Examine_Chair" : "Its a chair. You can sit on it.",
                "Examine_Chair1" : "This is where you would normally sit.",
                "Examine_Chair2" : "This is where Mark would normally sit.",
                "Examine_Chair3" : "This is where Allisson would normally sit.",
                "Examine_Couch" : "Ah the living room couch. A good place to watch TV",
                "Examine_Table" : "Its one of those tables you put between your TV and your couch, its very low to the ground. Perfect for putting drinks on"
                    
            }

            self.Empty = {
                "Empty_Trash" : "You take all of the garbage out and put it in the trashcan in the garage.",
                "Empty_any" : "You empty the (=self.name=)"
            }

            self.Go = {
                "Go_any" : "You walk over to (=self.article=)(=self.displayname=)"
            }
            
            self.LayDown = {
                "LayDown_any" : "You lay down on the (=self.name=) for a quick rest..."
            }

            self.Light = {
                "Light_any" : "You light the (=self.name=). It is now illuminating the area around it"
            }

            self.Locked = {
                "Locked_FrontDoor": "You dont really feel like going outside... Sometimes you wonder if there is anything beyond the 3 rooms you currently can or feel like going to... Wait what?",
                "Locked_any" : "its locked"
            }

            self.Extinguish = {
                "Extinguish_any" : "You extinguish the flame on the (=self.name=). The light fades away."
            }
            self.Sit = {
                "Sit_Couch" : "You take a seat next to your two roomates",
                "Sit_any" : "You sit on the (=self.name=)"
            }

            self.Take = {
                "Take_any" : "You take the (=self.name=)"
            }

            self.Drop = {
                "Drop_any" : "You drop the (=self.name=)"
            }

            self.Wear = {
                "Wear_any" : "You put on the (=self.name=)"
            }
            self.Remove = {
                "Remove_any" : "You take off the (=self.name=)"
            }
