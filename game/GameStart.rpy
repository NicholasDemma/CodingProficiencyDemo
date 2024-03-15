label start:
       
    #scene color "#202020ff"
    $ renpy.profile_screen("game_gui",show = True, update = True, time=True, debug=False)
    #$ renpy.profile_screen("test_gui",show = True, update = True, time=True, debug=True)
    image backgroundcolor = "#2c2c2c"
    scene backgroundcolor
    show color "#707070ff"
    show screen test_gui
    #define e = Character(None, image="eileen", kind=bubble)
    default locationlist = [YourRoom(),Hallway(),MainRoom()] 

    python:
        #essential start operations go here
        #also dont define any classes in this python code as they will break on closing and reopening the game as these lines will not be run again
        #this is bad
        #class Player:
        #   pass

        startinglocation = locationlist[0]
        SetCurrentLocation(startinglocation)

        readablelist = []
        for item in locationitems:
            readablelist.append(item.name+":"+str(item.displayspacing))
        smartlog("All location items are "+str(readablelist).replace("[","("))
        #reset the textlog before showing to the player
        textlog.clear()  
        game_guienabled = True
        gameready = True
        if keyboard.is_pressed('ctrl'): #this is here simply because the first time the keyboard module is used it does not work, but everytime after it does
            pass
        UpdateStyles()
        global inventoryitems
        global wornitems
        globals()["inventoryview1list"] = inventoryitems
        globals()["inventoryview2list"] = wornitems
    jump gamestart

    label gamestart: 
        #$ renpy.stop_predict_screen("game_gui")
        
        $ renpy.show_screen("game_gui")
        $ InitializeGUI()
        $ renpy.checkpoint()
        
        jump gameloop
 
    label gameloop:

    $ renpy.retain_after_load()
    
    $ input = renpy.input("",multiline=False, pixel_width = renpy.get_physical_size()[0]*.6 - 30)
    $ renpy.checkpoint()
 
    jump gameloop

    hide screen game_gui
    show black with Dissolve(3)
    return