################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)



################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#0099cc'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#888888'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#66c1e0'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "DejaVuSans.ttf"

## The font used for character names.
define gui.name_text_font = "DejaVuSans.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "DejaVuSans.ttf"

## The size of normal dialogue text.
define gui.text_size = 33

## The size of character names.
define gui.name_text_size = 45

## The size of text in the game's user interface.
define gui.interface_text_size = 33

## The size of labels in the game's user interface.
define gui.label_text_size = 36

## The size of text on the notify screen.
define gui.notify_text_size = 24

## The size of the game's title.
define gui.title_text_size = 75


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 360
define gui.name_ypos = 0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(6, 6, 6, 6)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 60

## The vertical position of the skip indicator.
define gui.skip_ypos = 15

## The vertical position of the notify screen.
define gui.notify_ypos = 68

## The spacing between menu choices.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 15

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 210

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"

################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30

python early:
    import multipledispatch
    from multipledispatch import dispatch
    import random
    import copy
    import traceback
    import time
    import threading
    import ctypes
    import keyboard
    import string
    
    #this function is currently unused as its use of eval on a string that (potentially in the future) could be user created. Thus potentially allowing users to run malicious code
    #however, this function is perfectly safe to run on any strings that you can be sure were programmed by a developer, which is currently all of them
    #this function is slated to become completly obsolete by the "ProcessText" function in the commands file. It will do kind of the same thing, except it is slated to do more
    #and never run the eval function, instead opting to take keywords and use those to decide what to do, so it would be perfectly safe
    #this function takes a string and parses it so that text between '{=' '}' (or whatever parsechar and parsecharclose are set to) is put into an eval function, turned into a 
    #string and reinserted back into the string that the function recieved. This is done repeatedly for every instance of the parsechar and parsecharclose characters found
    #example "{=somefunctionhere(\"a value\")}, wow what a great value!" lets say somefunctionhere("a value") returns "4000". eval_parser("{=somefunctionhere(\"a value\")} wow what 
    # a great value!") would return "4000, wow what a great value!"
    @dispatch(str)
    def eval_parser(parsestr) -> str:
        parsechar = "{"
        parsecharclose = "}"
        if (parsechar+"=") in parsestr and parsecharclose in parsestr:
            startindex = parsestr.index(parsechar+"=")+2 # +2 because length of '{=' is 2
            endindex = parsestr.index(parsecharclose,startindex)
            if startindex < endindex:
                #say("","start " + str(startindex)+"| end "+str(endindex))
                #say("",parsestr[0:startindex])
                evalstr = parsestr[startindex:endindex:]
                #use of eval is TEMPORARY do NOT use this in final release as users could supply malicious code, instead just let the text run only the functions you want it to run
                evaluated = str(eval(evalstr))
                finalstr = parsestr[0:startindex-2:] + evaluated + parsestr[endindex+1:len(parsestr):] #start of parsestring + evaluatedstring + everything after evaluated string
                return (eval_parser(finalstr))
            else: return "something went wrong here..."
        else: return parsestr

    @dispatch(str,object)
    def eval_parser(parsestr,scopeobject) -> str:
        #return str(scopeobject.capacity)
        parsechar = "{"
        parsecharclose = "}"
        numopen = 0
        numclose =  0
        shouldshow = False
        if (parsechar+"=if") in parsestr:
            startindex = parsestr.index(parsechar+"=if")+4 # +4 because length of '{=if' is 4
            strtosearch = parsestr[startindex:len(parsestr)]
            strsofar = ""
            numopen = 1
            numparenthesisopen = 0
            inparameters = False
            parameterstr = ""
            parameters = []
            sections = []
            for c in strtosearch:
                if c == ' ':
                    pass
                elif c == '.':
                    #we have reached a breaking point. The '.' is not neccessary to remember so we can mark everything before this as being part of a single section (variable, or object, or func)
                    sections.append(strsofar)
                    strsofar = ""
                elif c == '(':
                    inparameters = True
                    numparenthesisopen += 1
                elif c == ',':
                    #we have finished a parameter, we can go onto a new one now
                    if inparameters:
                        parameters.append(parameterstr)
                        parameterstr = ""
                elif c == ')':
                    #we have finished a parameter, we can go onto a new one now
                    if inparameters:
                        parameters.append(parameterstr)
                        parameterstr = ""
                elif c == ':':
                    #if we are here we have have a string with no spaces and a variable amount of '.'s
                    sections.append(strsofar)
                    #currentobject can be either an object, a property of some value (true, false, string, num), or a function
                    currentobject = scopeobject
                    if len(sections) == 1:
                        currentobject = globals()[sections[0]]
                    elif len(sections) == 2:
                        if sections[0] == "self" or sections[0] == "this":
                            currentobject = getattr(scopeobject,sections[1])
                        else:
                            currentobject = globals()[sections[0]]
                            currentobject = getattr(currentobject,sections[1])
                    else:
                        #length is 3 or more
                        if sections[0] == "self" or sections[0] == "this":
                            currentobject = scopeobject
                        else:
                            currentobject =  globals()[sections[0]]
                        for i in range(1, len(sections)-1):
                            currentobject = getattr(currentobject,sections[i])
                    #now our currentobject has cycled through all of the .'s and is either a value or an object or a function
                    #if it is a string
                    #say("",str(parsestr)[0])
                    if type(currentobject) == str: #and (currentobject == "True" or currentobject == "true"):
                        say(""," its a string???" + currentobject)
                        shouldshow = True
                    elif type(currentobject) == bool:
                        say(""," it is literally a bool")
                        shouldshow = currentobject
                    elif type(currentobject) == int and currentobject != 0:
                        say(""," its a number not equal to zero???")
                        shouldshow = True
                    elif callable(currentobject):
                        say(""," it is a function!")
                        #insert code here to handle if what we are left with is a function
                    elif isinstance(currentobject, type):
                        say(""," This is an object???")

                elif c == '{':
                    numopen+=1
                elif c == '}':
                    numopen-=1        
                else:
                    strsofar+=c
                    if inparameters:
                        parameterstr+=c

        return "should we show it? " + str(shouldshow)
    @dispatch (str)
    def smartsay(what, *args, **kwargs):
        smartsay("",what, *args, **kwargs)

    @dispatch (int)
    def smartsay(what, *args, **kwargs):
        smartsay("",str(what), *args, **kwargs)

    @dispatch (str,object)
    def smartsay(what,scopeobject, *args, **kwargs):
        smartsay("",what, scopeobject, *args, **kwargs)

    @dispatch (int,object)
    def smartsay(what, *args, **kwargs):
        smartsay("",what, scopeobject *args, **kwargs)

    @dispatch (str,str)
    def smartsay(who, what, *args, **kwargs):
        smartsay(who,what,object(), *args, **kwargs)

    @dispatch (str,int)
    def smartsay(who, what, *args, **kwargs):
        smartsay(who, str(what),object(), *args, **kwargs)
    
    @dispatch (str,int,object)
    def smartsay(who, what,scopeobject, *args, **kwargs):
        smartsay(who, str(what),scopeobject, *args, **kwargs)

    #currently the way we play sound when characters are talking
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            #smartlog("Section shown!")
            renpy.sound.play("characterblip.mp3")
        elif event == "slow_done":
            #smartlog("done")
            #renpy.restart_interaction()
            renpy.sound.stop()

    @dispatch (str,str,object)
    def smartsay(who, what,scopeobject, *args, background = "", **kwargs):
        global sayingthings 
        global gettinginput
        if gettinginput: return #if we are already saying things then we do not want to say things again as that would pop open another window on top of the existing one
        global lastwho
        texttolog = ""
        if lastwho != who and not textlog_firstline:
            texttolog = "\n"+who + ": " + ProcessText(what,scopeobject)
        else: 
            texttolog = ProcessText(what,scopeobject)
        smartlog(texttolog)
        lastwho = who
        global sayingthings      
        if background != "":
            globals()["whatboxbackground"] = background
        global whatsize
        if "what_color" not in kwargs or what_color is None or what_color == "":
            what_color = "#000000"
        #caret = Text("|",size = whatsize, color = what_color)
        #caret = At(caret,blinking) #apply transform to our caret
        sayingthings = True #this will make it so that our game knows we are saying things and other UI functions can respond accordingly
        gettinginput = True
        #say(who,what, ctc = caret, **kwargs)
        #renpy.show_screen("sayhidebutton")
        say(who,what, callback = beepy_voice, **kwargs)
        global sayfadingout
        global sayfaded
        #if we ended while fading out then since we closed the window we can then say instead of fading out we will just start faded
        if sayfadingout:
            sayfadingout=False
            sayfaded = True
        sayingthings = False
        gettinginput = False
        if background != "":
            global whatboxdefaultbackground
            globals()["whatboxbackground"] = whatboxdefaultbackground

    

    #this function will take an array of inputs and run it through the processtext command before printing it. Possibly with a scope object that can be used for the "self" keyword
    @dispatch (str)
    def smartlog(what, *args, **kwargs):
        smartlog("",what, *args, **kwargs)

    @dispatch (int)
    def smartlog(what, *args, **kwargs):
        smartlog("",str(what), *args, **kwargs)

    @dispatch (str,object)
    def smartlog(what,scopeobject, *args, **kwargs):
        smartlog("",what, scopeobject, *args, **kwargs)

    @dispatch (int,object)
    def smartlog(what, *args, **kwargs):
        smartlog("",what, scopeobject *args, **kwargs)

    @dispatch (str,str)
    def smartlog(who, what, *args, **kwargs):
        smartlog(who,what,object(), *args, **kwargs)

    @dispatch (str,int)
    def smartlog(who, what, *args, **kwargs):
        smartlog(who, str(what),object(), *args, **kwargs)
    
    @dispatch (str,int,object)
    def smartlog(who, what,scopeobject, *args, **kwargs):
        smartlog(who, str(what),scopeobject, *args, **kwargs)
    
    textlogref = None
    @dispatch (str,str,object)
    def smartlog(who, what,scopeobject, *args, **kwargs):
        global game_guienabled
        global textlogref
        global textlogready
        global Debug
        if Debug:
            if game_guienabled:
                if textlogref is None:
                    textlogref = globals()["textlog"]
                if not textlogready:
                    globals()["textlogready"] = True
                if globals()["textlog_firstline"]:
                    textlogref.append("")
                    textlogref.append(">"+ProcessText(what,scopeobject))
                    globals()["textlog_firstline"] = False
                else:
                    textlogref.append(ProcessText(what,scopeobject))

                scrollbar = renpy.get_displayable("game_gui","textlog")
                scrollbar.yadjustment.value = scrollbar.yadjustment.range+10000
        else:
            if game_guienabled:
                if textlogref is None:
                    textlogref = globals()["textlog"]
                if not textlogready:
                    prepareGUI()
                    globals()["textlogready"] = True                  
                    alltextlines = seperateintolines(">"+ProcessText(what,scopeobject))
                    global FirstLinetext
                    globals()["FirstLinetext"]  = alltextlines[0]
                    del alltextlines[0]
                    globals()["textlog_firstline"] = False
                    for line in alltextlines:
                        textlogref.append(line)
                elif globals()["textlog_firstline"]:
                    textlogref.append("")
                    alltextlines = seperateintolines(">"+ProcessText(what,scopeobject))
                    globals()["textlog_firstline"] = False
                    for line in alltextlines:
                        textlogref.append(line)
                else:
                    alltextlines = seperateintolines(ProcessText(what,scopeobject))
                    for line in alltextlines:
                        textlogref.append(line)
                scrollbar = renpy.get_displayable("game_gui","textloggrid")
                scrollbar.yadjustment.value = scrollbar.yadjustment.range+10000


        h = renpy.character.HistoryEntry()
        h.who = ""
        h.what = "> " + ProcessText(what,scopeobject) 
       
        h.what_args = []

        if renpy.game.context().rollback:
            h.rollback_identifier = renpy.game.log.current.identifier
        else:
            h.rollback_identifier = None

        _history_list.append(h)

        while len(_history_list) > renpy.config.history_length:
            _history_list.pop(0)

    #this function takes a string then according to the length of the textlogGUI window size and the actual size of drawn text (tested by drawing text out side of the screen)
    #and then checking how big that is as I could not find a mathmatical approach to do this so I just had to use guess and check) in a way that each line is just big enough
    #to fit in the available space. This allows us to display each line sperately as opposed to in a single text display with an unpredicatable height as it could have any
    #number of lines. Since the height will now be guaranteed the same for each text object we can then use a vpgrid to display all of them and a vpgrid requires everything
    #to be the same height or it wont work and its significantly faster than displaying more than a few screens worth of text using a number of unpredictably sized Text 
    #displayables. this is significantly faster in the long run when you want to be able to have a lot of text display in the main log. The more text the faster this becomes
    #in comparison to not doing it this way. Although this function could absolutely be optimized I attempt to algorithmically speed it up by starting with a base number of
    #characters to check based on the length of the 10 most common characters in the english language and how big those are on average. This number is calculated in prepareGUI
    def seperateintolines(text):
        #DO NOT PUT smartlog STATEMENTS IN HERE AS THEY WILL CAUSE AN INFINITE LOOP
        Maxchars = 20
        alllines = []
        textlogGUI = renpy.get_displayable("game_gui","textlogframe")
        testingGUI = renpy.get_displayable("test_gui","testing")
        global currentavglinelength 
        avglen = currentavglinelength 
        availablespace = textlogGUI.window_size[0]-16
        partstring = text
        wholestring =  partstring
        maxruns = 5000
        #textlogref.append("i recieved this: "+text)
        #textlogref.append("wholestring is: "+wholestring)
        while len(partstring) >0 and maxruns>0:
            #textlogref.append("Whats left "+partstring)
            #if it starts with a space remove it
            if partstring[0]==" ":
                partstring = partstring[1:]
                wholestring = wholestring[1:]
            #if it has a new line, go up to it as there is no reason to look past it
            newlinefound = False
            if partstring.find("\n") != -1:
                #do something about it
                indexofnew = partstring.find("\n")
                partstring = partstring[0:indexofnew]
                newlinefound = True
            #check if the rest is small enough to print right away
            testingGUI.set_text(partstring)
            lengthoftest = testingGUI.size()[0]
            if lengthoftest<=availablespace:
                #we can fit the rest in one go. so we do, then we continue the loop.

                alllines.append(partstring)
                #two cases here. New line found witch means that most likely there is more to this loop. or else it wasnt found. That means we can just break
                if newlinefound:
                    wholestring = wholestring[len(partstring)+1:]
                    partstring = wholestring
                    continue
                else:
                    break
            #there is no longer a newline in our string, but it could still come up. For now mark it as unfound
            newlinefound = False
            #the rest is not small enough to print, so if the part is bigger than the avglen then make it that, or else, its already as small as it can be
            if len(partstring) >= avglen:
                partstring = partstring[0:avglen]
                testingGUI.set_text(partstring)
                lengthoftest = testingGUI.size()[0]

            #textlogref.append("We lookin at " +partstring)
            if lengthoftest < availablespace and not newlinefound:
                #textlogref.append("bigger")
                nomoreleft = False
                while lengthoftest < availablespace and not nomoreleft and maxruns>0:
                    maxruns-=1
                    #textlogref.append(partstring)
                    #smartlog("Size is "+str(lengthoftest))
                    indexofspace = wholestring.find(" ",len(partstring))
                    if indexofspace != -1 and (indexofspace - len(partstring)) < Maxchars:
                        #check if a newline would be in that area
                        indexofnew = wholestring.find("\n",len(partstring),indexofspace)
                        if indexofnew != -1:
                            #if there is a newline, do not add it. Mark that we found one and go up to it but dont add it
                            partstring = partstring + wholestring[len(partstring):indexofnew]
                            newlinefound = True
                            #also break because we dont want to add anymore
                            break
                        else:
                            #if not, we can add up to the next space  
                            partstring = partstring + wholestring[len(partstring):indexofspace]
                    else:
                        #no more spaces in whole string. That means we just add the rest of it to string and mark that we hit the end
                        #textlogref.append("no more spaces?")
                        trystring = partstring + wholestring[len(partstring):]
                        testingGUI.set_text(trystring)
                        lengthoftest = testingGUI.size()[0]
                        #try doing that and then check if the string fits
                        if lengthoftest <= availablespace:
                            #the string fit great. We are now done
                            partstring = trystring
                            nomoreleft = True
                            break
                        #it didnt fit. 
                        wholestringlength = len(wholestring)        
                        partstringlength = len(partstring)
                        newlinefound = wholestring[partstringlength] == "\n"
                        testingGUI.set_text(partstring)
                        lengthoftest = testingGUI.size()[0]
                        #while we need to make it bigger and can add and the next index isnt a new line
                        while lengthoftest < availablespace and wholestringlength > partstringlength and not newlinefound:                         
                            partstring = partstring + wholestring[partstringlength]
                            partstringlength += 1
                            testingGUI.set_text(partstring.replace("!","l").replace(".","l").replace("?","n"))
                            lengthoftest = testingGUI.size()[0]
                            newlinefound = wholestring[partstringlength] == "\n"
                            #textlogref.append("length is"+str(lengthoftest))
                        if newlinefound:
                            #we found a newline so we should just break and let the program handle it
                            break
                        #no newline found so
                        if lengthoftest>availablespace:
                            partstring = partstring[0:-1]
                        break

                    testingGUI.set_text(partstring)
                    lengthoftest = testingGUI.size()[0]
                #now its more so now we remove one
                indexofspace = partstring.rfind(" ")
                if nomoreleft: 
                    alllines.append(partstring)
                    break           
                elif not newlinefound and (len(partstring) - indexofspace) < Maxchars:
                    #last add made it too big so this one undos that and makes it just right
                    partstring = partstring[0:indexofspace]
                elif newlinefound:
                    #we found a newline and there is more. Check if whatever we added made it too big and if it did then remove some stuff 
                    testingGUI.set_text(partstring)
                    lengthoftest = testingGUI.size()[0]
                    if lengthoftest > availablespace:
                        #too big, remove the last space
                        partstring = partstring[0:partstring.rfind(" ")] 
                        #mark this as false again because its no longer in the string and its also not the very next character so we know there will be more stuff on the next line other than it
                        newlinefound = False
            else:
                #textlogref.append("smaller") #we need to make it smaller
                nospacesleft = False
                while lengthoftest > availablespace and maxruns>0:
                    maxruns-=1
                    #textlogref.append(partstring)
                    #smartlog("Size is "+str(lengthoftest))
                    indexofspace = partstring.rfind(" ")
                    if indexofspace  != -1 and (len(partstring)-indexofspace) < Maxchars:
                        partstring = partstring[0:indexofspace]
                    else:
                        #no spaces, or the distance between this and the next space is more than Maxchars length
                        #remove characters one by one until it fits
                        while lengthoftest > availablespace:
                            partstring = partstring[0:-1]
                            testingGUI.set_text(partstring)
                            lengthoftest = testingGUI.size()[0]
                    testingGUI.set_text(partstring)
                    lengthoftest = testingGUI.size()[0]

            alllines.append(partstring)
            #textlogref.append("its good!")
            if len(wholestring) > len(partstring):
                #if the whole is greater than the part, remove the part from the whole
                if newlinefound:
                    wholestring = wholestring[len(partstring)+1:]
                    partstring = wholestring
                else:
                    wholestring = wholestring[len(partstring):]
                    partstring = wholestring
            else:
                partstring = wholestring
                wholestring = ""
            maxruns-=1
        return alllines

    #prepare the GUI by calculating aproximately how many characters should be able to fit length wise based on a calculation of the length of the 10 most common english
    #characters found in the "mostusedletters" list
    def prepareGUI():
        global textlogref
        if textlogref is None:
            textlogref = globals()["textlog"]
        global currentavgcharlength
        textlogGUI = renpy.get_displayable("game_gui","textlogframe")
        testingGUI = renpy.get_displayable("test_gui","testing")
        #textlogref.append(str(dir(textlogGUI)))
        #renpy.show_screen("chooseobjects",str(dir(textlogGUI)),"nothing",None)
        #renpy.show_screen("chooseobjects",str(textlogGUI.window_size[0]),"nothing",None)
        availablespace = textlogGUI.window_size[0]-16
        #textlogref.append("Available space is "+str(availablespace))
        global textlogtextsize
        mostusedletters = ["e","a","r","i","o","t","n","s","l","c"]
        totalsize = 0
        for letter in mostusedletters:
            testingGUI.set_text(letter)
            totalsize = totalsize + testingGUI.size()[0]
        avglength = int(totalsize / 10)
        currentavglinelength = int(availablespace/avglength)
        globals()["currentavglinelength"] = currentavglinelength  #avg length of a single character based on the 10 most popular english letters
        textlogready = True
        #textlogref.append("We prepared it!")
        #textlogref.append("it is "+str(globals()["currentavglinelength"]))


default textlogready = False
default currentavglinelength  = 0       
default textlog_firstline = False
define gui_leftmargin = 5
default lastwho = ""