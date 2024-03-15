#Contain Game UI, Player Object, Basic Global variables including inventory, items, and current location as well as some base functions that are used in game setup
#and to manipulate these global variables

transform cd_transform:
    # This is run before appear, show, or hide.
    xalign 0.5 yalign 0.5 alpha 0.0

    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

# style heading_button is button

# style heading_button_text:
#     #size header_textsize

# style interactiveobject_button is button

# style interactiveobject_button_text:
#     #size 25

default interactiveobject_textsize = 23
default verb_textsize = 20
default guiheader_textsize = 28
default tooltiptextsize = 20
default textlogtextsize = 30
default interactiveobject_spacing = 0
default textlog = []
default game_guienabled = False
default Debug = False
default FirstLinetext = ""
default viewheaderspacing = 10

default UIbackgroundcolor = "#4e515a" #"#4e515a"
default UIoutlinecolor = "#FFFFFF" #"#FFFFFF"
default AllTextColor = "#FFFFFF" #"#FFFFFF"
default HeaderTextColor = AllTextColor
default BodyTextColor = AllTextColor
default ViewIconOutlineColor = "#000000"
default textlogheight = 970
default sayingthings = False
default gettinginput = False

style sio_button is button: #selected inventory object button
    background "#929292ff"
    top_margin -15 + 5
    bottom_margin -15 + 5

style uio_button is button:
    background "#4e515a"
    top_margin -15 + 5
    bottom_margin -15 + 5

init python:
    def UpdateStyles():
        global UIbackgroundcolor
        renpy.register_style_preference("text", "decorated", style.uio_button, "background", UIbackgroundcolor)
        renpy.register_style_preference("text", "decorated", style.uio_button, "top_margin", -15 + 5)
        renpy.register_style_preference("text", "decorated", style.uio_button, "bottom_margin", -15 + 5)
        renpy.set_style_preference("text", "decorated")
    
    config.keymap['dismiss'].append('alt_mouseup_1')
    config.keymap['button_select'].append('alt_mouseup_1')
    #config.keymap['dismiss'].append('ctrl_mouseup_1')
    #config.keymap['button_select'].append('ctrl_mouseup_1')

style svi_button is button: #selected view icon
    background "#929292ff"
    xmargin -4
    ymargin -4

style uvi_button is button: #unselected view icon
    background "#636363"
    xmargin -4
    ymargin -4


style verb_button is frame
    #xsize 100
    #ysize 50

screen test_gui():
    fixed:
        ypos -1000
        text "" size textlogtextsize id "testing"


screen game_gui():
    zorder 3
    hbox:
        #leftside textlog gui and input graphics (it doesnt actually get input though)
        vbox:
            xpos gui_leftmargin
            #textlog
            xsize .6
            frame:
                #xpos gui_leftmargin
                ypos 5
                xsize 1.0          
                background UIoutlinecolor
                right_margin 9
                yfill True
                #python:
                    #textlogheight = 20#renpy.get_physical_size()[0]-110
                ysize textlogheight
                #bottom_margin 111
                
                if not Debug:
                    frame id "textlogframe":
                        background UIbackgroundcolor
                        yfill True
                        xfill True
                        xmargin -5
                        ymargin -5
                        vpgrid id "textloggrid":
                                cols 1
                                spacing 0
                                mousewheel True
                                scrollbars "vertical"
                                xmaximum 1.0
                                xfill True
                                xalign 0.0
                                frame: 
                                    background "#4e515a00"
                                    xfill True
                                    xmargin -7
                                    ymargin -7
                                    text FirstLinetext xminimum 1.0 xfill True size textlogtextsize xsize 1920 layout "nobreak" 
                                for item in textlog:
                                    text item size textlogtextsize layout "nobreak" 
                else:
                    frame id "frame":
                        background UIbackgroundcolor
                        yfill True
                        xfill True
                        xmargin -5
                        ymargin -5
                        side "c r":
                            viewport id "textlog":
                                mousewheel True
                                yfill False
                                vbox:
                                    yalign 1.0
                                    for item in textlog:
                                        text item size textlogtextsize color BodyTextColor
                            vbar value YScrollValue("textlog") id "textlogscrollbar" bar_invert True xalign 1.0 
            frame:
                right_margin 9
                xsize 1.0
                #xpos gui_leftmargin
                ysize 70
                ypos 10
                background "#FFFF"
                
                frame:          
                    background "#4e515a"
                    xmargin -5
                    ymargin -5

                    yfill True
                    xfill True
                
        #right side inventory+location gui
        vbox:
            xsize 1.0
            xalign .995
            yalign 0.005
            yanchor 0
            #xsize .3
            spacing 10
            #inventory GUI
            frame:
                background UIoutlinecolor
                #bottom_margin 20
                vbox:
                    xsize 1.0
                    ymaximum 300
                        
                    frame:
                        background "#2B2D31"
                        xpos -5
                        ypos -5
                        xsize 1.0
                        right_margin -10
                        bottom_margin -10

                        textbutton "[InventoryButtonText]" text_color HeaderTextColor id "inventorybtn":
                            text_size guiheader_textsize
                            ymargin -7
                            xsize 1.0
                            action (Function(ToggleView,"inventoryview"))    
                            
                    showif showinventory:
                        frame:
                            background UIoutlinecolor
                            xsize 1.0
                            xpos -5
                            ypos 5
                            ysize 6
                            right_margin -10

                        frame:
                            background UIbackgroundcolor
                            xpos -5
                            xsize 1.0
                            right_margin -10
                            bottom_margin -5

                            fixed:
                                yfit True
                                #inventory split button to the left
                        
                                if not InventoryViewSplit:
                                    #inventory view is not split so we are only displaying one list
                                    frame:
                                        top_margin -5
                                        bottom_margin 0
                                        background ViewIconOutlineColor
                                        button:
                                            xmargin -10
                                            ymargin -10
                                            add "SplitViewIcon.png"
                                            tooltip "Split this into two views"
                                            action (Function(OnSplitMergeButtonClicked,"inventory")) 
                                    vbox:
                                        id "inventoryview1" 
                                        hbox:
                                            id "inventoryview1icons"
                                            xcenter .5
                                            spacing 5
                                            python: 
                                                index = 0
                                            for icon in ValidInventoryViewIcons:
                                                python: 
                                                    index +=1
                                                frame:                                                  
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "inventoryview1icon"+str(index)
                                                        if "inventoryview1icon"+str(index) == inventoryview1lastselectediconid:                                                           
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"inventoryview1",icon,index))  
                                        text "[inventoryview1header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                                                                
                                        vpgrid id "inventoryitems": 
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"
                                            python:
                                                index = 0                          
                                            for item in inventoryview1list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if inventoryview1header == "Everything": 
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext
                                                if item.isvisible:
                                                    frame id "inventoryviewitem " + str(index):
                                                        if item == currentlyselectedinventoryitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                            textbutton buttontext:     
                                                                text_layout "nobreak"                  
                                                                text_size interactiveobject_textsize
                                                                text_color BodyTextColor                        
                                                                xfill True
                                                                action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor    
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))  
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize          
                                                                        xfill True
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                                else:
                                    frame:
                                        background "#FFFF"
                                        xpos 365
                                        xsize 5
                                        ysize 60
                                        ymargin -5
                                    frame:
                                        top_margin -5
                                        bottom_margin 0
                                        background ViewIconOutlineColor  
                                        button:
                                            xmargin -10
                                            ymargin -10
                                            add "MergViewIcon.png"
                                            tooltip "Merge both sides back into one"
                                            action (Function(OnSplitMergeButtonClicked,"inventory")) 
                                    vbox:
                                        id "inventoryview1"
                                        xsize .5
                                        hbox:
                                        #the inventoryview is split. We need 2 hboxes.
                                            id "inventoryview1icons"
                                            xcenter .5
                                            spacing 5

                                            python: 
                                                index = 0
                                            for icon in ValidInventoryViewIcons:
                                                python: 
                                                    index +=1
                                                frame:
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "inventoryview1icon"+str(index)
                                                        if "inventoryview1icon"+str(index) == inventoryview1lastselectediconid:                                                     
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"inventoryview1",icon,index))

                                        text "[inventoryview1header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                        vpgrid id "inventoryitems":
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"                         
                                            python:
                                                index = 0                          
                                            for item in inventoryview1list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if inventoryview1header == "Everything": 
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext
                                                if item.isvisible:
                                                    frame id "inventoryviewitem " + str(index):
                                                        if item == currentlyselectedinventoryitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                            textbutton buttontext:
                                                                text_layout "nobreak"
                                                                text_size interactiveobject_textsize
                                                                text_color BodyTextColor                         
                                                                xfill True
                                                                action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor    
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))  
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item))
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize          
                                                                        xfill True
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                                    vbox:
                                        id "inventoryview2"
                                        xpos .5
                                        xsize .5
                                        hbox:
                                            id "inventoryview2icons"
                                            xcenter .5
                                            spacing 5                                                       
                                            python: 
                                                index = 0
                                            for icon in ValidInventoryViewIcons:
                                                python: 
                                                    index +=1
                                                frame:       
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "inventoryview2icon"+str(index)
                                                        if "inventoryview2icon"+str(index) == inventoryview2lastselectediconid:                                                     
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"inventoryview2",icon,index))
                                        text "[inventoryview2header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                        vpgrid id "inventoryview2items":
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"                         
                                            python:
                                                index = 0                          
                                            for item in inventoryview2list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if inventoryview2header == "Everything":
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext
                                                if item.isvisible:
                                                    frame id "inventoryview2item " + str(index):
                                                        if item == currentlyselectedinventoryitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                            textbutton buttontext: 
                                                                text_layout "nobreak"
                                                                text_size interactiveobject_textsize
                                                                text_color BodyTextColor                         
                                                                xfill True
                                                                action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item))
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor   
                                                                    action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))   
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize          
                                                                        xfill True
                                                                        action (Function(OnItemClicked,"inventoryview","inventoryview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))                         
                        if inventoryviewhasverbs:
                            frame:
                                background UIbackgroundcolor
                                xpos -5
                                xsize 1.0
                                right_margin -10
                                bottom_margin -5
                                hbox:                        
                                    style_prefix "verb"
                                    xalign 0.5
                                    spacing -20  
                                    for verb in currentlyselectedinventoryitem.currentverbs:                                    
                                        textbutton verb text_color BodyTextColor:
                                            text_size verb_textsize
                                            xfill False
                                            left_margin 30
                                            if verbsenabled and not gettinginput:
                                                action (Call("OnVerbClicked","inventoryview",verb))
                                            else:
                                                action(Function(OnVerbClickedPython,"inventoryview",verb)) 
            #Current Location GUI
            frame:
                background UIoutlinecolor

                vbox:
                    id "LocationView"
                    xsize 1.0
                    ymaximum 600
                        
                    frame:
                        background "#2B2D31"
                        xpos -5
                        ypos -5
                        xsize 1.0
                        right_margin -10
                        bottom_margin -10

                        textbutton "[LocationButtonText]" text_color HeaderTextColor id "locationbtn":
                            text_size guiheader_textsize
                            ymargin -7
                            xsize 1.0
                            action (Function(ToggleView,"locationview"))
                            
                    showif showlocation:

                        frame:
                            background UIoutlinecolor
                            xsize 1.0
                            xpos -5
                            ypos 5
                            ysize 6
                            right_margin -10

                        frame:
                            background UIbackgroundcolor
                            xpos -5
                            xsize 1.0
                            right_margin -10
                            bottom_margin -5 

                            fixed:
                                yfit True
                                #location split button to the left
                        
                                if not LocationViewSplit:
                                    #location view is not split so we are only displaying one list
                                    frame:
                                        top_margin -5
                                        bottom_margin 0
                                        background ViewIconOutlineColor
                                        button:
                                            xmargin -10
                                            ymargin -10
                                            add "SplitViewIcon.png"
                                            tooltip "Split this into two views"
                                            action (Function(OnSplitMergeButtonClicked,"location")) 
                                    vbox:
                                        id "locationview1" 
                                        hbox:
                                            id "locationview1icons"
                                            xcenter .5
                                            spacing 5
                                            python: 
                                                index = 0
                                            for icon in ValidLocationViewIcons:
                                                python: 
                                                    index +=1
                                                frame:                                                  
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "locationview1icon"+str(index)
                                                        if "locationview1icon"+str(index) == locationview1lastselectediconid:                                                           
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"locationview1",icon,index))  
                                        text "[locationview1header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                          

                                            
                                        vpgrid id "locationitems": 
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"                          
                                            python:
                                                index = 0                          
                                            for item in locationview1list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if locationview1header == "Everything": 
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext + ""
                                                if item.isvisible:
                                                    frame id "locationviewitem " + str(index):
                                                        if item == currentlyselectedlocationitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                            textbutton buttontext:  
                                                                text_layout "nobreak"                     
                                                                text_size interactiveobject_textsize
                                                                text_color BodyTextColor                         
                                                                xfill True
                                                                action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor   
                                                                    action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))   
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize                                                                        
                                                                        xfill True
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                                else:
                                    frame:
                                        background "#FFFF"
                                        xpos 365
                                        xsize 5
                                        ysize 60
                                        ymargin -5
                                    frame:
                                        top_margin -5
                                        bottom_margin 0
                                        background ViewIconOutlineColor  
                                        button:
                                            xmargin -10
                                            ymargin -10
                                            add "MergViewIcon.png"
                                            tooltip "Merge both sides back into one"
                                            action (Function(OnSplitMergeButtonClicked,"location")) 
                                    vbox:
                                        id "locationview1"
                                        xsize .5
                                        hbox:
                                        #the locationbiew is split. We need 2 hboxes.
                                            id "locationview1icons"
                                            xcenter .5
                                            spacing 5

                                            python: 
                                                index = 0
                                            for icon in ValidLocationViewIcons:
                                                python: 
                                                    index +=1
                                                frame:
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "locationview1icon"+str(index)
                                                        if "locationview1icon"+str(index) == locationview1lastselectediconid:                                                     
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"locationview1",icon,index))

                                        text "[locationview1header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                        vpgrid id "locationitems":
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"                         
                                            python:
                                                index = 0                          
                                            for item in locationview1list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if locationview1header == "Everything": 
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext
                                                if item.isvisible:
                                                    frame id "locationviewitem " + str(index):
                                                        if item == currentlyselectedlocationitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                                textbutton buttontext:
                                                                    text_layout "nobreak" 
                                                                    text_size interactiveobject_textsize
                                                                    text_color BodyTextColor                         
                                                                    xfill True
                                                                    action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor    
                                                                    action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))   
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item))
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize          
                                                                        xfill True
                                                                        action (Function(OnItemClicked,"locationview","locationviewitem "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                        
                                    vbox:
                                        id "locationview2"
                                        xpos .5
                                        xsize .5
                                        hbox:
                                            id "locationview2icons"
                                            xcenter .5
                                            spacing 5                                                       
                                            python: 
                                                index = 0
                                            for icon in ValidLocationViewIcons:
                                                python: 
                                                    index +=1
                                                frame:       
                                                    top_margin -5
                                                    bottom_margin 0
                                                    background ViewIconOutlineColor
                                                    frame:
                                                        id "locationview2icon"+str(index)
                                                        if "locationview2icon"+str(index) == locationview2lastselectediconid:                                                     
                                                            style "svi_button"
                                                        else:
                                                            style "uvi_button"
                                                        xmargin -4
                                                        ymargin -4
                                                        button:
                                                            xmargin -12
                                                            ymargin -12
                                                            add icon.icon
                                                            tooltip icon.tooltip
                                                            action (Function(ViewIconClicked,"locationview2",icon,index))
                                        text "[locationview2header]" size interactiveobject_textsize xpos viewheaderspacing
                                        frame:
                                            background "#FFFF"
                                            xpos 10
                                            xsize .9
                                            ysize 1  
                                        vpgrid id "locationview2items":
                                            cols 1
                                            spacing 0
                                            xmaximum 1.0
                                            xfill True
                                            mousewheel True
                                            scrollbars "vertical"                         
                                            python:
                                                index = 0                          
                                            for item in locationview2list:
                                                python:
                                                    index +=1
                                                    buttontext = item.displayname
                                                    spacingtext = ""
                                                if locationview2header == "Everything":
                                                    python:
                                                        buttontext = item.spacingtext+buttontext
                                                        spacingtext = item.spacingtext
                                                if item.isvisible:
                                                    frame id "locationview2item " + str(index):
                                                        if item == currentlyselectedlocationitem:
                                                            style "sio_button"
                                                        else:
                                                            style "uio_button"
                                                        if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                            textbutton buttontext: 
                                                                text_layout "nobreak" 
                                                                text_size interactiveobject_textsize
                                                                text_color BodyTextColor                         
                                                                xfill True
                                                                action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item))
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        else:
                                                            hbox:
                                                                xfill True
                                                                xsize 1.0
                                                                spacing -12
                                                                textbutton spacingtext:
                                                                    xmargin 0
                                                                    text_size 22
                                                                    text_color BodyTextColor
                                                                    action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))
                                                                for tooltipobj in item.beforetooltips:
                                                                    button:
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))
                    
                                                                textbutton item.displayname:
                                                                    text_layout "nobreak"
                                                                    text_size interactiveobject_textsize 
                                                                    text_color BodyTextColor    
                                                                    action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item)) 
                                                                    hovered (Function(OnItemHovered,item,_update_screens=False))   
                                                                    if len(item.aftertooltips) == 0: 
                                                                        xfill True 

                                                                for tooltipobj in item.aftertooltips:
                                                                    button:
                                                                        xmargin 0
                                                                        add tooltipobj.icon ypos 2
                                                                        tooltip tooltipobj.tooltip
                                                                        action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))

                                                                if len(item.aftertooltips) != 0:
                                                                    textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                        text_size interactiveobject_textsize          
                                                                        action (Function(OnItemClicked,"locationview","locationview2item "+str(index),item)) 
                                                                        hovered (Function(OnItemHovered,item,_update_screens=False))                                            
                        if locationviewhasverbs:
                            frame:
                                background UIbackgroundcolor
                                xpos -5
                                xsize 1.0
                                right_margin -10
                                bottom_margin -5
                                hbox:   
                                    spacing -20                   
                                    style_prefix "verb"
                                    xalign 0.5
                                    for verb in currentlyselectedlocationitem.currentverbs:                                    
                                        textbutton verb text_color BodyTextColor:
                                            text_size verb_textsize
                                            xfill False
                                            left_margin 30
                                            if verbsenabled and not gettinginput:
                                                action (Call("OnVerbClicked","locationview",verb))
                                            else:
                                                action(Function(OnVerbClickedPython,"locationview",verb)) 
                                                #this will not work because it could call "say" which freezes the screen which causes an error if not called from within renpy script
                                                #...or at least that would be the case, but as long as it simply doesnt call anything that calls say (or anything that will pause the script), 
                                                #which we can check for before calling the function, then we are good!also, since this isnt technically the same function as the Call("OnVerbClicked")
                                                #this can be run just fun asynchonously alongside the other call, allowing us to await input (a click on any part of the screen that would otherwise not
                                                #capture a click) and to do other things with the UI!

            if specialviewenabled:
                frame:
                    background UIoutlinecolor
                    vbox:
                        xsize 1.0
                        ymaximum 300
                            
                        frame:
                            background "#2B2D31"
                            xpos -5
                            ypos -5
                            xsize 1.0
                            right_margin -10
                            bottom_margin -10

                            textbutton "[SpecialViewButtonText]" text_color HeaderTextColor:
                                text_size guiheader_textsize
                                ymargin -7
                                xsize 1.0
                                action (Function(ToggleView,"specialview"))     
                                
                        showif showspecialview:
                            frame:
                                background UIoutlinecolor
                                xsize 1.0
                                xpos -5
                                ypos 5
                                ysize 6
                                right_margin -10

                            frame:
                                background UIbackgroundcolor
                                xpos -5
                                xsize 1.0
                                right_margin -10
                                bottom_margin -5
                            #vbox:
                                #id "inventoryview1" 
                                #hbox:
                                    #id "inventoryview1icons"
                                    #xcenter .5
                                    #spacing 5
                                    #python: 
                                        #index = 0
                                    #for icon in ValidSpecialViewIcons:
                                        #python: 
                                            #index +=1
                                        #frame:                                                  
                                            #top_margin -5
                                            #bottom_margin 0
                                            #background ViewIconOutlineColor
                                            #frame:
                                                #id "inventoryview1icon"+str(index)
                                                #if "inventoryview1icon"+str(index) == inventoryview1lastselectediconid:                                                           
                                                    #style "svi_button"
                                                #else:
                                                    #style "uvi_button"
                                                #xmargin -4
                                                #ymargin -4
                                                #button:
                                                    #xmargin -12
                                                    #ymargin -12
                                                    #add icon.icon
                                                    #tooltip icon.tooltip
                                                    #action (Function(ViewIconClicked,"inventoryview1",icon,index))  
                                #text "[inventoryview1header]" size interactiveobject_textsize xpos viewheaderspacing
                                #frame:
                                    #background "#FFFF"
                                    #xpos 10
                                    #xsize .9
                                    #ysize 1  
                                                                        
                                vpgrid id "specialitems": 
                                    cols 1
                                    spacing 0
                                    xmaximum 1.0
                                    xfill True
                                    mousewheel True
                                    scrollbars "vertical"
                                    #python:
                                        #index = 0                          
                                    for item in specialviewlist:
                                        #python:
                                            #index +=1
                                            #buttontext = item.displayname
                                            #spacingtext = ""
                                        #if specialview1header == "Everything": 
                                            #python:
                                                #buttontext = item.spacingtext+buttontext
                                                #spacingtext = item.spacingtext
                                        if item.isvisible:
                                            frame id "specialviewitem " + str(index):
                                                if item == currentlyselectedspecialitem:
                                                    style "sio_button"
                                                else:
                                                    style "uio_button"
                                                if len(item.beforetooltips) == 0 and len(item.aftertooltips) == 0:
                                                    textbutton item.displayname:                       
                                                        text_size interactiveobject_textsize
                                                        text_color BodyTextColor                        
                                                        xfill True
                                                        action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                        hovered (Function(OnItemHovered,item,_update_screens=False))  
                                                else:
                                                    hbox:
                                                        xsize 1.0
                                                        spacing -12
                                                        #textbutton item.displayname:
                                                            #xmargin 0
                                                            #text_size 22
                                                            #text_color BodyTextColor
                                                            #action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                            #hovered (Function(OnItemHovered,item,_update_screens=False))
                                                        for tooltipobj in item.beforetooltips:
                                                            button:
                                                                add tooltipobj.icon ypos 2
                                                                tooltip tooltipobj.tooltip
                                                                action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))
            
                                                        textbutton item.displayname:
                                                            text_size interactiveobject_textsize 
                                                            text_color BodyTextColor    
                                                            action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                            hovered (Function(OnItemHovered,item,_update_screens=False))   
                                                            if len(item.aftertooltips) == 0: 
                                                                xfill True 

                                                        for tooltipobj in item.aftertooltips:
                                                            button:
                                                                xmargin 0
                                                                add tooltipobj.icon ypos 2
                                                                tooltip tooltipobj.tooltip
                                                                action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False))  

                                                        if len(item.aftertooltips) != 0:
                                                            textbutton "": #we use a textbutton here so the button can set its height automatically
                                                                text_size interactiveobject_textsize          
                                                                action (Function(OnItemClicked,"specialview","specialviewitem "+str(index),item)) 
                                                                hovered (Function(OnItemHovered,item,_update_screens=False)) 
                            if specialviewhasverbs:
                                frame:
                                    background UIbackgroundcolor
                                    xpos -5
                                    xsize 1.0
                                    right_margin -10
                                    bottom_margin -5
                                    hbox:                        
                                        style_prefix "verb"
                                        xalign 0.5
                                        spacing -20  
                                        for verb in currentlyselectedspecialitem.currentverbs:                                    
                                            textbutton verb text_color BodyTextColor:
                                                text_size verb_textsize
                                                xfill False
                                                left_margin 30
                                                if verbsenabled:
                                                    action (Call("OnVerbClicked","specialview",verb)) 
    $ tooltip = GetTooltip()
    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                background "#3669b6de"
                xalign 0.5
                text tooltip size tooltiptextsize

default inventoryitems = []
default locationitems = [] #this has to go before any items are declared because they will try to default to this as the list they are in
default wornitems = [NoneItem("Nothing")]
default inventoryfavorites = [NoneItem("Nothing, alt+click to favorite")]
default locationNPCs = []
default locationfavorites = [NoneItem("Nothing, alt+click to favorite")]

default showinventory = False
default InventoryButtonText = "> Inventory"

default LocationName = "Big Room"
default LocationButtonText = "> Big Room"
default showlocation = False

default specialviewenabled = False
default SpecialViewOccurence = "Shop"
default SpecialViewButtonText = "> Shop"
default showspecialview = False
init python:
    def ToggleView(Viewname):
        if Viewname == "inventoryview":
            global showinventory
            if showinventory:
                #it was shown so we shouldnt now
                globals()["InventoryButtonText"] = "> Inventory"
                showinventory = False
            else:
                globals()["InventoryButtonText"] = "v Inventory"
                showinventory = True
        elif Viewname == "locationview":
            global showlocation
            if showlocation:
                #it was shown so we shouldnt now
                global LocationName
                globals()["LocationButtonText"] = "> " + LocationName
                showlocation = False
            else:
                globals()["LocationButtonText"] = "v " + LocationName
                showlocation = True
        elif Viewname == "specialview":
            global SpecialViewOccurence
            global showspecialview
            if showspecialview:
                #it was shown so we shouldnt now
                globals()["SpecialViewButtonText"] = "> "+SpecialViewOccurence
                showspecialview = False
            else:
                globals()["SpecialViewButtonText"] = "v "+SpecialViewOccurence
                showspecialview = True
        renpy.checkpoint()


default currentlyselectedinventoryitem = None
default currentlyselectedinventorybutton = None
default currentlyselectedlocationitem = None
default currentlyselectedlocationbutton = None
default currentlyselectedspecialitem = None
default currentlyselectedspecialbutton = None

default inventoryviewhasverbs = False
default inventoryview1header = "All Items"
default inventoryview2header = "Worn & Held Items"
default inventoryview1list = []
default inventoryview2list = []
default inventoryview1lastselectediconid = "inventoryview1icon1"
default inventoryview2lastselectediconid = "inventoryview2icon2"

default locationviewhasverbs = False
default locationview1header = "Everything"
default locationview2header = "NPCs"
default locationview1list = []
default locationview2list = []
default locationview1lastselectediconid = "locationview1icon1"
default locationview2lastselectediconid = "locationview2icon2"

default specialviewhasverbs = False
default specialviewlist = []

init python:
    #this handles what happens when you click on an item in the inventory
    def OnItemClicked(ViewName,FrameID,item):
        #smartlog("Click!")
        #this gets the actual button object that was clicked
        global choosingobject
        if not choosingobject:
            if not item.flag("isnothing"):
                #Viewname is of pattern somethingview so by removing the last 4 characters we isolate the something where something is variable
                keyword = ViewName[0:-4]
                selectedbutton = renpy.get_displayable("game_gui",FrameID)
                lastselectedbutton = globals()["currentlyselected"+keyword+"button"]
                lastselecteditem =  globals()["currentlyselected"+keyword+"item"]
                #if we clicked on a different item then before
                if item != lastselecteditem:
                    #temporarily set hasverbs to none so the game dosent attempt to immediately place them if the new object dosent have verbs
                    viewhasverbs = False
                    #set our currentlyselectedinventoryitem, this will allow us to access it in other places such as when we click on a verb
                    currentlyselecteditem = item
                    #check if it hasverbs or not
                    if currentlyselecteditem.currentverbs : viewhasverbs = True
                    else : viewhasverbs = False

                    #This section used to help but now it does nothing as the if statements in renpy screen language can handle it just fine (as long as  _update_screens isnt set to false)).
                    #this could be changed later if we wanted to set _update_screens_ to false again and manually do the work ourself in python and update just the buttons that need it
                    #set the style of the frame that surrounds the button to sio_button (selected inventory object _ button)
                    #selectedbutton.style = Style("sio_button")     
                    #renpy.redraw(selectedbutton,0)  
                    #if lastselectedbutton != None:
                        #set the style of the last selected button to uio button so that it dosent appear seelected anymore
                        #lastselectedbutton.style = Style("uio_button")   
                        #renpy.redraw(lastselectedbutton,0)   
                    #then we set last selected_inventory button to the button we recieved so the next call knows what the last button was 
                    globals()["currentlyselected"+keyword+"button"] = currentlyselectedspecialbutton = selectedbutton 
                    globals()[ViewName+"hasverbs"] = viewhasverbs
                    #remove the "view" from view name
                    globals()["currentlyselected"+keyword+"item"] = item
                if keyboard.is_pressed('alt'):
                    ToggleFavoriteItem(item)
                #renpy.checkpoint()
                #smartlog("checkpoint made?")
            else:
                #its nothing we shouldnt focus it!
                pass
        else:
            #We are trying to choose an object to do something with!
            itemtext = ProcessText(choosingobjecttryitemtext,item)

            if item.flag(choosingobjectrequiredproperty):
                itemtext += "✓"
            else:
                itemtext += ProcessText(choosingobjectdoesntworktext,item)

            if item.flag(choosingobjectrequiredproperty):
                #it works! We can close the screen and do a callback now
                renpy.hide_screen("chooseobjects")
                choosingobject = False
                global verbsenabled
                verbsenabled = True
                global choosingobjectcallbackarguments
                choosingobjectcallbackarguments.insert(1,item)
                global choosingobjectcallback
                choosingobjectcallback(*choosingobjectcallbackarguments)             
            else:
                renpy.show_screen("chooseobjects",choosingobjectprompt,choosingobjectsuggestionlist,itemtext)           
                
default LocationViewSplit = False
default InventoryViewSplit = False
default ValidLocationViewIcons = [ViewSortIcon("AllViewIcon.png","Show anything and everything in the surrounding area","Everything","locationitems"),
ViewSortIcon("NPCViewIcon.png","Show just the NPCs","NPCs","locationNPCs"),
ViewSortIcon("FavoritesViewIcon.png","Show favorited items","Favorites","locationfavorites")]

default ValidInventoryViewIcons = [ViewSortIcon("AllViewIcon.png","Show everything in the inventory","All Items","inventoryitems"),
ViewSortIcon("EquipmentViewIcon.png","Show Worn Items","Worn & Held items","wornitems"),
ViewSortIcon("FavoritesViewIcon.png","Show favorited items","Favorites","inventoryfavorites")]

default ValidSpecialViewIcons = []

init python:
    def ViewIconClicked(View,icon,index):
        #smartlog("wow cool")
        currentlyselectediconid = View + "icon" + str(index)
        currentlyselectedicon = renpy.get_displayable("game_gui",currentlyselectediconid)
        lastselectediconid = globals()[View+"lastselectediconid"]
        lastselectedicon = renpy.get_displayable("game_gui",  lastselectediconid) 

        #set our header text of our View
        headertext = icon.headertext
        globals()[View+"header"] = headertext
        #set what list our view is currently using to display
        viewlistname = icon.viewliststr
        globals()[View+"list"] = globals()[viewlistname]
     
        #do our button style setting redrawing now, this is the same everywhere
        if currentlyselectedicon != lastselectedicon:
                currentlyselectedicon.style = Style("svi_button")     
                renpy.redraw(currentlyselectedicon,0) 
                if lastselectedicon != "":
                    lastselectedicon.style = Style("uvi_button") 
                    renpy.redraw(lastselectedicon,0)
                #set our last selected icon to the proper thing
                globals()[View+"lastselectediconid"] = currentlyselectediconid             
        #locationview = renpy.get_displayable("game_gui",View)
        #renpy.redraw(locationview,0) 

    def OnSplitMergeButtonClicked(viewname):
        if viewname == "location":
            global LocationViewSplit
            LocationViewSplit = not LocationViewSplit
            locationview = renpy.get_displayable("game_gui","LocationView")
            renpy.redraw(locationview,0)
        elif viewname == "inventory":
            global InventoryViewSplit
            InventoryViewSplit = not InventoryViewSplit
            locationview = renpy.get_displayable("game_gui","InventoryView")
            renpy.redraw(locationview,0)
        return

    def InitializeGUI():
        pass
        #global locationview1lastselectedicon
        #locationview1lastselectedicon = renpy.get_displayable("game_gui","locationview1icon1")
        #global locationview1astselectedicon
        #locationview2lastselectedicon =  renpy.get_displayable("game_gui","locationview2icon2")

default verbsenabled = True
init python:
    #this version is used if something is being said. You should not "say" anything in this function. You technically can but after say() is run it will error and not run whatever is after it
    #which can cause problems
    def OnVerbClickedPython(view,verbstr):
        verbitem = None
        if view == "inventoryview":
            global currentlyselectedinventoryitem
            verbitem = currentlyselectedinventoryitem
        elif view == "locationview":
            global currentlyselectedlocationitem
            verbitem = currentlyselectedlocationitem
        elif view == "specialview":
            global currentlyselectedspecialitem
            verbitem = currentlyselectedspecialitem
        #smartlog("Verb item is "+str(verbitem.name)+". Verb item has "+str(dir(verbitem)))
        global verbsenabled
        if verbsenabled:
            tryverbstring = "On"+verbstr.replace(" ","")
            #smartlog("trying "+tryverbstring)
            #verbstring = tryverbstring
            hasoverride = hasattr(verbitem,tryverbstring)
            #smartlog("hasoverride is "+str(checkoveride))
            if hasoverride:
                #smartlog("It has an override! calling it")
                globals()["textlog_firstline"] = True
                override = getattr(verbitem,tryverbstring)
                override()
            else:
                #smartlog("Check override does not exist. Using default implementation.")
                try:
                    globals()[tryverbstring](verbitem)
                except Exception as e:
                    #smartlog("","verb \""+tryverbstring+"\" is not a defined global verb!")                  
                    if Debug:
                        smartlog("An error occured "+traceback.format_exc())
                    pass
                else:
                    pass
            renpy.checkpoint()
        else: 
            if gettinginput:
                smartlog("You cant click these now! Type something in first.")
            else:
                smartlog("You cant click these now! Please click on an object first")

label OnVerbClicked(view,verbstr):
    python:
        #smartlog("Verbs enabled..." +str(verbsenabled))
        verbitem = None
        if view == "inventoryview":
            verbitem = currentlyselectedinventoryitem
        elif view == "locationview":
            verbitem = currentlyselectedlocationitem
        elif view == "specialview":
            verbitem = currentlyselectedspecialitem
            #smartlog("Verb item is "+str(verbitem))
        #smartlog("Verb item is "+str(verbitem.name)+". Verb item has "+str(dir(verbitem)))
        if verbsenabled:
            tryverbstring = "On"+verbstr.replace(" ","")
            #verbstring = tryverbstring
            hasoverride = hasattr(verbitem,tryverbstring)
            #smartlog("hasoverride is "+str(checkoveride))
            if hasoverride:
                #smartlog("It has an override! calling it")
                globals()["textlog_firstline"] = True
                override = getattr(verbitem,tryverbstring)
                override()
            else:
                #smartlog("Check override does not exist. Using default implementation.")
                try:
                    globals()[tryverbstring](verbitem)
                except Exception as e:
                    pass
                    #smartlog("","verb \""+tryverbstring+"\" is not a defined global verb!")
                    if Debug:
                        smartlog("An error occured "+traceback.format_exc())
                else:
                    renpy.checkpoint()
        else: 
            if gettinginput:
                smartlog("You cant click these now! Type something in first.")
            else:
                smartlog("You cant click these now! Please click on an object first")
        global sayingthings 
        sayingthings = False #just to make sure this doesnt get locked at any moment although it should never happen
        global gettinginput
        gettinginput = False
    return

default choosingobject = False
default choosingobjectprompt = ""
default choosingobjectsuggestionlist = ""
default choosingobjectcallback = None
default choosingobjectcallbackarguments = None
default choosingobjectrequiredproperty = ""
default choosingobjecttryitemtext = ""
default choosingobjectdoesntworktext = ""

init python:
    #we run this from python code because this is not a call statement and thus it makes it so the screen doesnt have to 
    #redraw itself, thus saving a lot of performance
    def OnItemHovered(item):
        #renpy.hide_screen("chooseobjects")
        if choosingobject:
            itemtext = ProcessText(choosingobjecttryitemtext,item)

            if item.flag(choosingobjectrequiredproperty):
                itemtext += "✓"
            else:
                itemtext += ProcessText(choosingobjectdoesntworktext,item)
            #renpy.hide_screen("chooseobjects")
            renpy.show_screen("chooseobjects",choosingobjectprompt,choosingobjectsuggestionlist,itemtext)
            chooseobjects = renpy.get_displayable("chooseobjects","chooseobjectswindow")
            renpy.redraw(chooseobjects,0)
        return

default clonedobjectid = 0
default clonedlist = [] 
default startinglocation = None
default player = PlayerClass()
default gameready = False

default idnum = 0

init python:
    #objects defined in init python should never be changed after the game starts, this wont save between opening and closing the game, same with python early
    #this can be reconciled if you want to use a type as a global variable of sorts, such as using PlayerClass as a global class where Player.attribute can
    #be used to get all attributes refferring to the player. In order to use a type as a global varaible, just define a default variable and set its value to the
    #type. Basically think of init python classes as static classes, except you can change them (you should not though). If you do this however, you are choosing
    #to not instantiate the type, meaning that none of its functions can have self as a parameter, not even inherited classes. 
    #just instantiate
    class PlayerClass:
        @property
        def pose(self):
            #say("","getter method called")
            return self._pose

        @pose.setter
        def pose(self,thepose):
            #smartlog("Spacing updated on " + self.name+" to "+str(self.displayspacing))
            #smartlog("Pose set "+thepose.name)
            if thepose != self._pose:
                #smartlog("Not the same")
                self._pose = thepose
                #if thepose == pose.standing:
                    #smartlog("You stand up")
                #elif thepose == pose.sitting:
                    #smartlog("You sit on the "+self.mostspecificlocation.name.lower())
                #elif thepose == pose.layingdown:
                    #smartlog("You lay down on the "+self.mostspecificlocation.name.lower())
        
        def __init__(self):
            self.current_location = None
            self.current_IA = None
            self.current_IL = None
            self.current_IO = None
            self.mostspecificlocation = None
            self._pose = pose.standing
            self.ActionResponseType = ARCustom1()
            self.favoritecolor = "Pink" 

        


    def MoveItemToRelativeLocationInObject(item,obj,rl,canclone = False, cancombine = True, canmoveall = False):
        if item.count>1 and not (canmoveall and keyboard.is_pressed('shift')):
            item = SeperateItem(item)
        else:
            DeselectObject(item)

        if item.scope != scope.none:
            if item.listlocation is not None:
                item.listlocation.remove(item)
            item.scopelist.remove(item)
            if item.isfavorite:
                RemoveFromFavoriteList(item)

        relativelocationliststr = relativelocationlists(rl.value).name
        relativelocationlist = getattr(obj,relativelocationliststr)

        didcombine = False
        if cancombine:
            didcombine = CheckIfCanCombineInList(item,relativelocationlist)
        if not didcombine:
            item.listlocation = relativelocationlist
            item.scopelist = obj.scopelist
            item.scopelist.insert(obj.lastindexinscope(rl)+1,item)
            relativelocationlist.append(item)
            #now we have to add the item to the proper place in its scope list.
            item.scope = obj.scope
            if obj.scope == scope.inventory:
                item.ininventory = True
                item.currentverbs = item.inventoryverbs
            else:
                item.ininventory = False
                item.currentverbs = item.locationverbs
            item.parent = obj
            item.relativelocation = rl
            if item.relativelocation == relativelocation.inside:
                if not item.parent.isopen:
                    #smartlog("invis")
                    item.isvisible = False
             
    #this attempts to move an item to the inventory but will clone an item and move it if it was not meant to be moved directly
    def MoveToInventory(obj,canclone = True,cancombine = True):
        if obj.scope == scope.inventory:
            return False

        global clonedobjectid
        global clonedlist
        #smartlog("Yes?")
        cloned = False
        if canclone and obj.flag("iscloneable") and obj.flag("isoriginal"):
            #its an original object and it is cloneable. That means we can make a copy of it
            obj = obj.clone()
            cloned = True

        if obj.count>1:
            obj = SeperateItem(obj)
        else:
            DeselectObject(obj)

        if obj.scope != scope.none:
            if obj.listlocation is not None:
                obj.listlocation.remove(obj)
            obj.scopelist.remove(obj)
            if obj.isfavorite:
                RemoveFromFavoriteList(obj)

        #if we can combine it try that and if it fails then we add it manually
        didcombine = False
        if cancombine:
            didcombine = CheckIfCanCombineInList(obj,inventoryitems)
        if not didcombine:
            global inventoryitems
            global inventoryfavorites
            obj.ininventory = True
            #if obj.flag("iswearable"):
                #obj.isworn = False
            obj.listlocation = None
            obj.scopelist = inventoryitems
            obj.relativelocation = relativelocation.none
            inventoryitems.append(obj)
            obj.currentverbs = obj.inventoryverbs
            if obj.isfavorite:
                obj.favoritelistin = inventoryfavorites
                AddToFavoriteList(obj)
            obj.scope = scope.inventory
            if obj.parent is not None:
                obj.parent.setdisplayname()
                obj.parent = None

    #try to wear the item. Do it if we can and if not return false
    def TryWearItem(obj) -> bool: #returns if it was worn or not
        if obj.iswearable and not obj.isworn:
            if not obj.ininventory:
                MoveToInventory(obj, canclone = False, cancombine = False)
            obj = SeperateItemAndFocus(obj,canrecombine = obj.flag("cancombineonwear"))
            obj.cancombine = obj.flag("cancombineonwear")
            obj.isworn = True
            obj.currentverbs = obj.wornverbs
            #smartlog(wornitems[-1].name)
            if wornitems[-1].name == "Nothing":
                del wornitems[-1]
            wornitems.append(obj)
            obj.currentverbs = obj.wornverbs
            return True   
        return False

    def TakeOffItem(obj) -> bool: #returns if we could take it off or not
        if obj.iswearable:
            obj.isworn = False
            obj.currentverbs = obj.inventoryverbs
            wornitems.remove(obj)
            if not wornitems:
                wornitems.append(NoneItem("Nothing"))
            return True
        smartlog("you cant remove that")
        return False

    def DropItem(obj):
        if obj.scope == scope.location:
            return False
        
        #check if there is more than one. If there is seperate it and use that object for our drop. if not, that means this is the last object in its stack
        #and thus after its dropped our invetory should have nothing selected
        if obj.count>1:
            obj = SeperateItem(obj)
        else:
            DeselectObject(obj)

        if obj.scope != scope.none:
            obj.scopelist.remove(obj)
            if obj.isfavorite:
                RemoveFromFavoriteList(obj)

        #check if we can combine it with something already in the list
        combinelist = None
        if player.current_IL is not None:
            combinelist = player.current_IL.objectsinarea
        else:
            combinelist = player.current_IA.objectsinarea

        if not CheckIfCanCombineInList(obj,combinelist):
            obj.ininventory = False
            #obj.isworn = False
            obj.scopelist = locationitems
            #our default behavior is to drop the item around the area of the players current interaction location or interaction area if the IL does not exist
            lastitem = None
            obj.relativelocation = relativelocation.inarea
            if player.current_IL is not None:
                lastitem = player.current_IL.getLastChild()
                player.current_IL.objectsinarea.append(obj)
                obj.listlocation = player.current_IL.objectsinarea
                obj.parent = player.current_IL
            else:
                #check if its empty
                lastitem = player.current_IA.getLastChild()
                player.current_IA.objectsinarea.append(obj)
                obj.listlocation = player.current_IA.objectsinarea
                obj.parent = player.current_IA
            #obj.set
            locationitems.insert(locationitems.index(lastitem)+1,obj)
            obj.currentverbs = obj.locationverbs
            if obj.isfavorite:
                obj.favoritelistin = locationfavorites
                AddToFavoriteList(obj)
            obj.scope = scope.location

    def ToggleFavoriteItem(item):
        global inventoryfavorites
        global locationfavorites
        listin = inventoryfavorites
        if not item.flag("ininventory"):
            listin = locationfavorites
        if item.isfavorite:
            #its favorited now, make it unfavorited
            item.isfavorite = False
            item.removetooltip("favorite")
            RemoveFromFavoriteList(item)
            item.favoritelistin = None
            #smartlog("unfavorited "+item.name)
        else:
            #its not favorited, make it favorited
            item.isfavorite = True
            item.beforetooltips.append(ItemTooltip("Favorited","favoritetooltip.png","favorite"))
            item.favoritelistin = listin
            AddToFavoriteList(item)
            #smartlog("favorited "+item.name)
        
    def SetFavoriteStatus(item,status):
        if item.isfavorite != status:
            ToggleFavoriteItem(item)

    #these both account for favoritelistin to be accurate
    def AddToFavoriteList(item):
        if item.favoritelistin[-1].name == "Nothing, alt+click to favorite":
            del item.favoritelistin[-1]
        item.favoritelistin.append(item)

    def RemoveFromFavoriteList(item):
        item.favoritelistin.remove(item)
        if not item.favoritelistin:
            item.favoritelistin.append(NoneItem("Nothing, alt+click to favorite"))

    #technically this doesnt actually deslect an object, it just makes it so that whatever scope the object is in has nothing selected, but thats just a
    #product of *deselecting* an object not selecting anything else (which is desired)
    #this also means this function will work even if the object that this is run on is not acatually selected, it doesnt check for that
    def DeselectObject(obj):
        globals()[obj.scope.name+"viewhasverbs"]=False
        globals()["currentlyselected"+obj.scope.name+"item"] = None

    def DeleteItem(item):
        if item.scope != scope.none:
            if item.listlocation is not None:
                item.listlocation.remove(item)
            item.scopelist.remove(item)
            if item.isfavorite:
                RemoveFromFavoriteList(item)
            DeselectObject(item)
        else:
            pass
            #smartlog("no scope??")
        #delete it from any category it might be in
        #todo later, not a problem now
        if item.parent is not None:
            item.parent.setdisplayname()
        del item

    #this function checks if an object, Object, has the same meaningful properties as any of the other objects in list scope, and if so, combines
    #them. returns true if Object was combined or false if not
    def CheckIfCanCombineInList(Object,Scope) -> bool:
        #this function checks if an object, Object, has the same meaningful properties as any of the other objects in list scope, and if so, combines
        #them. returns true if Object was combined or false if not
        #smartlog("we here ")
        if Object.cancombine == False:
            return False
        for item in Scope:
            #check the name first as this will eliminate most things
            if Object.name == item.name:
                #smartlog("Same name!")
                if item.cancombine == False:
                    continue
                dict1 = vars(Object).copy()
                dict2 = vars(item).copy()
                #remove these because they are either unique or irrelevant to determining if the object is the same
                donotcompare = ["id","_count","ids","displayname","isfavorite","favoritelistin","listlocation","beforetooltips","aftertooltips","ininventory",
                "_scope","currentverbs", "relativelocation","spacingtext","_parent","_displayspacing","scopelist","_isvisible"]
                for key in donotcompare:
                    dict1.pop(key, None) 
                    dict2.pop(key, None)
                #smartlog("we good")
                # smartlog(str(dict1).replace("{","<(")+"\n")
                # for k,v in dict1.items():
                #     if k in dict2.keys():
                #         if dict2.get(k)!=v:
                #             smartlog("Different! Key:"+str(k)+" .Value:"+str(v))
                #     else:
                #         smartlog("Key:"+str(k)+" .Missing!") 
                #smartlog("\n")
                #smartlog(str(dict2).replace("{","<("))
                #its names are the same, check all properties now
                if dict1 == dict2:
                    # smartlog("Same object!")
                    #these are the same object! instead of adding this to our inventory we can simply increase the count of the already existing object by 1
                    item.count = item.count + Object.count
                    #we ignored this before when comparing but if the object we are taking is favorited we can favorite the whole stack for now
                    if (Object.isfavorite):
                        SetFavoriteStatus(item,True)
                    #we also want to preserve the unique id so we will add it to a list which we can pop the last element of when we want to seperate them
                    if hasattr(item,"ids"):
                        #smartlog("it had it")
                        item.ids.append(Object.id)
                        #if our object also already had an ids tag then we add all those as well
                        if hasattr(Object,"ids"):
                            item.ids.append(Object.ids)
                    else:
                        #smartlog("it didnt have it")
                        item.ids = [item.id,Object.id]
                    #item.setdisplayname()
                    return True
        return False
    
    def GetMostSpecificLocation(thing):
        if thing.current_IO is not None:
            return thing.current_IO
        elif thing.current_IL is not None:
            return thing.current_IL
        return thing.current_IA

    def SeperateItemAndFocus(item,canrecombine = True) -> 'item': #returns the seperated item or the inputted item if we did not seperate
        if item.count==1: return item
        item = SeperateItem(item,canrecombine)
        renpy.restart_interaction()
        GiveFocusToItem(item)
        return item

    def SeperateItem(item,canrecombine = True):
        if item.count==1:
            return item
        #smartlog("We made it")
        clone = copy.copy(item)
        #smartlog("Copied")
        item.count-=1
        clone.count = 1
        clone.id = item.ids.pop()
        clone.cancombine = canrecombine
        #insert the new cloned item after the original item in the relevant scope
        clone.scopelist.insert(clone.scopelist.index(item)+1,clone)
        #insert the new cloned item after the original item behind the scenes
        if clone.listlocation:
            clone.listlocation.insert(clone.listlocation.index(item)+1,clone)

        if  clone.isfavorite:
            clone.favoritelistin.append(clone)
        #smartlog("not so easy")
        #return the new cloned item
        return clone

    def GetFromLocationList(locationclass) -> 'Location':
        locationlist2 = globals()["locationlist"]
        for location in locationlist2:
            if isinstance(Location, locationclass):
                #smartlog("we found it")
                return location
        return None #we didnt find it return None

    def DoSomethingForAllList(objectlist,callback):
        for thing in objectlist:
            DoSomethingForAll(thing,callback)

    def DoSomethingForAll(obj, callback):
        #smartlog("Doing something for "+obj.displayname)
        #smartlog("Running callback...")
        callback(obj)
        #smartlog("Ran callback!")
        if isinstance(obj,Container):
            for item in obj.objectsinside:
                DoSomethingForAll(item,callback)
        if isinstance(obj, Location):
            for IA in obj.interactionareas:
                DoSomethingForAll(IA,callback)

        elif isinstance(obj, InteractionArea):
            for IL in obj.interactionlocations:
                DoSomethingForAll(IL,callback)
            for IO in obj.objectsinarea:
                DoSomethingForAll(IO,callback)

        elif isinstance(obj,InteractionLocation):
            #smartlog("its an interaction location!")
            for IO in obj.objectsontop:
                DoSomethingForAll(IO,callback)
            for IO in obj.objectsunder:
                DoSomethingForAll(IO,callback)
            for IO in obj.objectsinarea:
                DoSomethingForAll(IO,callback)



    def DoSomethingForAllChildren(obj,callback):
        #smartlog("Doing something for all children of "+obj.displayname)
        #if it is a location
        #smartlog("its a container!")
        if isinstance(obj,Container):
            for item in obj.objectsinside:
                DoSomethingForAll(item,callback)

        if isinstance(obj, Location):
            for IA in obj.interactionareas:
                DoSomethingForAll(IA,callback)
        #if it is an interaction area
        elif isinstance(obj, InteractionArea):
            for IL in obj.interactionlocations:
                #smartlog("about to callback for "+IL.displayname)
                DoSomethingForAll(IL,callback)
            for IO in obj.objectsinarea:
                DoSomethingForAll(IO,callback)

        elif isinstance(obj,InteractionLocation):
            #smartlog("its an interaction location!")
            for IO in obj.objectsontop:
                DoSomethingForAll(IO,callback)
            for IO in obj.objectsunder:
                DoSomethingForAll(IO,callback)
            for IO in obj.objectsinarea:
                DoSomethingForAll(IO,callback)

        #smartlog("Done with children of "+obj.displayname)


    #this is the only function that could not be replaced by the dosomethingforallchildren function and a callback (without modifications) as this function requires both
    #the object and the parent in the function AT THE SAME TIME to do its task and DoSomethingForAll only supplies one argument to the callback. While it could be modified
    #this is pretty useless because as soon as each object has a parent set you can then do future operations requiring parents with just the child as the child now has a reference
    #to its parent
    def SetObjectParents(thing):
        if isinstance(thing, Location):
            for IA in thing.interactionareas:
                IA.parent = thing
                SetObjectParents(IA)
        elif isinstance(thing, InteractionArea):
            for IL in thing.interactionlocations:
                IL.parent = thing
                IL.listlocation = thing.interactionlocations
                SetObjectParents(IL)
            for IO in thing.objectsinarea:
                IO.parent = thing
                IO.listlocation = IO.parent.objectsinarea
                IO.relativelocation = relativelocation.inarea
                SetObjectParents(IO)
        elif isinstance(thing,InteractionLocation):
            for item in thing.objectsinarea:
                item.listlocation = thing.objectsinarea
                item.parent = thing
                item.relativelocation = relativelocation.inarea
                SetObjectParents(item)
            for IO in thing.objectsontop:
                IO.parent = thing
                IO.listlocation = thing.objectsontop
                IO.relativelocation = relativelocation.ontop
                SetObjectParents(IO)
            for IO in thing.objectsunder:
                IO.parent = thing
                IO.listlocation = thing.objectsunder
                IO.relativelocation = relativelocation.under
                SetObjectParents(IO)
        if isinstance(thing,Container):
            for item in thing.objectsinside:
                if thing.isopen:
                    item.isvisible = True
                else:
                    item.isvisible = False
                item.parent = thing
                item.relativelocation = relativelocation.inside
                item.listlocation = thing.objectsinside
                SetObjectParents(item)

    def InitializeLocation(locationobject) -> bool:
        #this function will initialize all of the properties of a location as well as sorting everything there into its proper category lists
        global locationitems
        parentsset = SetObjectParents(locationobject) 
        #spaced = SetObjectSpacing(locationobject)
        global locationfavorites 
        currentlocationitemlist = []
        currentlocationNPClist = []
        def DoStuff(obj): #this function, with the help of our DoSomethingForAllChildren helper function, will do something for every item in the loaction we are initializing
            #set some default properties that all objects need to have but can also be easily gotten based off of other properties that NEED to be defined already
            #and they will be because every object in a location will inhert from DisplayObject in some way or another
            obj.simplename = obj.name.replace(" ","")
            obj.currentverbs = obj.locationverbs
            obj.scopelist = currentlocationitemlist
            obj.scope = scope.location
            if obj.flag("nameisproper"):
                #say("","Yeah that name, "+obj.name+", its proper.")
                obj.article = ""
            #this is how we add all (initially) recursively nested objects into a flattened list for displaying purposes
            #they are initally recursively nested as this is the easiest way to write the python code
            currentlocationitemlist.append(obj)
            #TODO make sophisticated
            obj.pluralname = obj.name + "s" #this is a placeholder and will be changed to something for sofisticated later
            #add stuff to our categories list (will be dictated by our viewicons later, but for now, is manually done)
            if obj.flag("isnpc"):
                currentlocationNPClist.append(obj)
            obj.setdisplayname()
        DoSomethingForAllChildren(locationobject,DoStuff)
        #in the future this should run through every category list and add None items if nothing was found
        if not currentlocationNPClist:
            currentlocationNPClist.append(NoneItem("None"))
        globals()["locationitems"] = currentlocationitemlist
        globals()["locationNPCs"] = currentlocationNPClist
        locationfavorites = []
        locationfavorites.append(NoneItem("Nothing, ctrl+click to favorite"))
        #and our global list for the views. These are set to by default " all location items, and location NPCs"
        for icon in ValidLocationViewIcons:
            if icon.headertext == locationview1header:
                globals()["locationview1list"] = globals()[icon.viewliststr] 
            if icon.headertext == locationview2header:
                globals()["locationview2list"] = globals()[icon.viewliststr] 
        locationobject.isready = True
        return True

    #gets a list of all contained items in that item, excluding the item inputted. so if a location is inputted it wont be included in the list
    def GetAllContainedItemsList(obj,itemlist) -> list:
        def addtolist(obj):
            itemlist.append(obj)
        DoSomethingForAllChildren(obj,addtolist)
        return itemlist  

    def SaveCurrentLocationItems():
        for icon in ValidLocationViewIcons:
            setattr(player.current_location,icon.viewliststr,globals()[icon.viewliststr])
        #smartlog("Saved!")

    def LoadCurrentLocationItems() -> bool:
        if not player.current_location.isready:
            InitializeLocation(player.current_location)
            return
        locationobject = player.current_location
        #set each global list as declared in the valid views icon list
        for icon in ValidLocationViewIcons:
            #we use a try except for future scaling and error prevention, though as of now getattr here should never error
            try:
                globals()[icon.viewliststr] = getattr(player.current_location,icon.viewliststr)
            except:
                globals()[icon.viewliststr] = []

        #populate global lists
        #these will make sure that what we are showing is the same category from room to room  and wont break the view icons
        for icon in ValidLocationViewIcons:
            if icon.headertext == locationview1header:
                globals()["locationview1list"] = globals()[icon.viewliststr] 
            if icon.headertext == locationview2header:
                globals()["locationview2list"] = globals()[icon.viewliststr] 
        #smartlog("Loaded!")

        
    #this sets the players current location and thus changes what items appear in the objects and places tab as well as changing some other corresponding stuff
    #location is either a string or an object
    def SetCurrentLocation(location) -> bool:
        if isinstance(location,str):
            global locationlist
            #smartlog(location)
            for locationobj in locationlist:
                if locationobj.name == location:
                    location = locationobj
        locationobject = location
        global LocationName
        LocationName = locationobject.displayname
        global showlocation
        if showlocation:
            #it was shown so we shouldnt now
            globals()["LocationButtonText"] = "v " + LocationName
        else:
            globals()["LocationButtonText"] = "> " + LocationName
        if showinventory:
            GiveFocusToItem(locationobject.defaultinteractionarea)
        #if we are at a location (which should be anytime other than the very first call of this function)
        #then we should tell the game we arent there anymore
        if player.mostspecificlocation is not None:
            player.mostspecificlocation.removetooltip("playerpresent")
            player.mostspecificlocation.locationverbs.insert(0,"Go")
        if player.current_IO is not None:
            player.current_IO.playerpresent = False
            player.current_IO = None
        if player.current_IL is not None:
            player.current_IL.playerpresent = False
            player.current_IL = None
        if player.current_IA is not None:
            player.current_IA.playerpresent = False

        if player.current_location != locationobject:
            if player.current_location != None:
                SaveCurrentLocationItems()

            player.current_location = locationobject
            LoadCurrentLocationItems()

            player.current_location = locationobject
            player.current_IA = locationobject.defaultinteractionarea
            player.mostspecificlocation = player.current_IA
            player.mostspecificlocation.beforetooltips.append(ItemTooltip("You are here","playerheretooltip.png","playerpresent"))
            locationobject.defaultinteractionarea.playerpresent = True
            if "Go" in locationobject.defaultinteractionarea.currentverbs:
                locationobject.defaultinteractionarea.currentverbs.remove("Go")

            #GiveFocusToItem(player.current_IA)
            return True
        #we were already in that location
        return False

    def GiveFocusToItem(item):
        #smartlog("trying to give focus to...")
        try:
            globals()[item.scope.name+"viewhasverbs"]= item.currentverbs
        except:
            globals()[item.scope.name+"viewhasverbs"] = False
        globals()["currentlyselected"+item.scope.name+"item"] = item
        #renpy.restart_interaction()

    #unneeded currently
    def FocusItemWhenExists(InventoryItemButtonID,item,waitfor):
        inventoryitemselectedbutton = renpy.get_displayable("game_gui",waitfor)
        while inventoryitemselectedbutton is None:
            #smartlog("its none")
            time.sleep(0.01)
            inventoryitemselectedbutton = renpy.get_displayable("game_gui",waitfor)
        OnInventoryItemClickedPython(InventoryItemButtonID,item)
        #renpy.call("OnInventoryItemClicked",InventoryItemButtonID,item)
        #smartlog("called!")

    #currently uneeded, obsoleted by making the current click function in python
    def OnInventoryItemClickedPython(item):
        #this gets the actual button object that was clicked
        global currentlyselectedinventoryitem
        global lastselected_inventorybutton
        #smartlog("we got it")
        inventoryitemselectedbutton = renpy.get_displayable("game_gui",InventoryItemButtonID)

        #if the lastselected_inventorybutton is not the same as the button we just clicked
        if lastselected_inventorybutton != inventoryitemselectedbutton:
            #temporarily set hasverbs to none so the game dosent attempt to immediately place them if the new object dosent have verbs
            hasverbs = False
            #set our currentlyselectedinventoryitem, this will allow us to access it in other places such as when we click on a verb
            currentlyselectedinventoryitem = item
            #check if it hasverbs or not
            if currentlyselectedinventoryitem.inventoryverbs : hasverbs = True
            else : hasverbs = False
            #tell the gui that we need to refresh, the last clicked button needs to be unselected
            #needsrefresh = True 
            #set the style of the frame that surrounds the button to sio_button (selected inventory object _ button)
            inventoryitemselectedbutton.style = Style("sio_button")
            renpy.redraw(inventoryitemselectedbutton,0)  
            if lastselected_inventorybutton != None:
                #set the style of the last selected button to uio button so that it dosent appear seelected anymore
                lastselected_inventorybutton.style = Style("uio_button")   
                renpy.redraw(lastselected_inventorybutton,0)   
            #then we set last selected_inventory button to the button we recieved so the next call knows what the last button was 
            lastselected_inventorybutton = inventoryitemselectedbutton
            renpy.hide_screen(game_gui)
            renpy.show_screen(game_gui)

# #unused
# label OnInventoryToggle:
#     #action ToggleScreen("inventory_item_description") 
#     python:
#         #toggleinvbutton = renpy.get_displayable("game_gui","invbutton")
#         toggleinvbuttontext = InventoryButtonText
#         #toggleinvbuttontext = toggleinvbuttontext[0]
#         if toggleinvbuttontext =="> Inventory":
#             #toggleinvbutton.set_text("v Inventory")
#             InventoryButtonText = "v Inventory"
#             showinventory = True
#         else:
#             #toggleinvbutton.set_text("> Inventory")
#             InventoryButtonText = "> Inventory"
#             showinventory = False
#         renpy.checkpoint()
#     return

# #unused
# label OnLocationToggle:
#     python:
#         #togglelocationbutton = renpy.get_displayable("game_gui","locationbtn")
#         togglelocationbuttontext = LocationButtonText
#         #togglelocationbuttontext = toggleinvbuttontext[0]
#         if togglelocationbuttontext =="> Current Location":
#             #toggleinvbutton.set_text("v Inventory")
#             LocationButtonText = "v Current Location"
#             showlocation = True
#         else:
#             #toggleinvbutton.set_text("> Inventory")
#             LocationButtonText = "> Current Location"
#             showlocation = False
#         renpy.checkpoint()
#     return
          




