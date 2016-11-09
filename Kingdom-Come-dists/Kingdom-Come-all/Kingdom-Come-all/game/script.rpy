﻿## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.
define Skyler = Character(None, kind = nvl, who_color="21618C", what_color="AED6F1")
define Vo = Character(None, kind = nvl, who_color="6C3483", what_color="D7BDE2")
define Hallis = Character(None, kind = nvl, who_color="922B21", what_color="D98880")
define narrator = Character(None, kind = nvl, what_color="FEF5E7") 
define letter = Character(None, bold=True, kind=nvl,what_color="000000", what_font="JandaElegantHandwriting.ttf")
define title = Character(None, what_color="E74C3C", what_font="KINGC___.ttf")

## Declare Image Files
image bg Aremoch city = "Greece.jpg"
image NVL = "gui/nvl.png"
image Parchment = im.Scale("images/parchment.png",config.screen_width * 0.7, config.screen_height * 0.9,
                          align = (0.7, 0.3))
## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg Aremoch city
    
    show text ("{alpha=*0.3}{size=400}{font=KINGC___.ttf}{color=#FF0099}Kingdom Come{/color}{/font}{/size}{/alpha}")
    with dissolve
    pause 2
    hide text
    with dissolve
    ## These display lines of dialogue.
    
    jump Beginning
   
    ## This ends the game.

    return
    
# Initialize the nvl_menu display
init python:
    style.default.drop_shadow = (1, 1)
    style.default.drop_shadow_color = "#000"
    menu = nvl_menu

    Narrative_variables = {}

    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"
    
    gui.choice_button_text_idle_color = '#ABB2B9'
    gui.choice_text_hover_color = '#FEF5E7'
    
    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20
    
    gui.nvl_height = None
    
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55
    style.nvl_window.top_margin = 80
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
    # If you want a Drop Shadow for your NVL text, 1 pixel to the right and 1 pixel down.
    style.nvl_dialogue.drop_shadow = [(1, 1)] 

    # if you want a different Drop Shadow Color.
    style.nvl_dialogue.drop_shadow_color = "#330000"

############    BEGIN NARRATIVE     ############################################################


label Beginning:
    show NVL with dissolve
    "It’s been awhile since work has kept you busy. Eloas isn’t a kingdom without 
problems, per se, but lately the reputation for recklessness your group has acquired seems to have 
     discouraged some of the more tentative clients from approaching.\n" 

    "You aren’t expecting anything different today, but when you open 
the mail portal, you find a letter waiting inside."
    menu:
        "Open the letter":
            nvl clear
            jump Opening_letter
            
        "Wait for {color=#922B21}Hallis{/color} and {color=#6C3483}Vo{/color}":
            nvl clear
            jump Waiting_for_letter
            
label Friends_Letter_Arrival:
    "The not-so-distant sound of bickering and good-natured laughter announces your
    friends’ joint arrival."

    "{color=#922B21}Hallis{/color} and {color=#6C3483}Vo{/color} enter the pavilion a moment later, eyes landing on the letter in your hands."
    
    Hallis "\'Correspondence?\' Hallis says, giving the letter a curious look. 
    \'Do we have work again, Skyler?\'"

    Vo "Vo sighs, leaning against a pillar. He summons a dancing orb of fire with an 
    elegant pull of his wrist, and sets it to move in darting circles around the 
    stone. \'There goes my plans for today. So what is it?\'"
    return
    
    
label Do_We_Accept_Letter:
    "You wordlessly hand Hallis the letter. Vo scowls at you, no bite to it, and 
    moves to stand next to Hallis on the tips of his toes to see properly."
    
    "Vo’s mouth moves soundlessly as he reads; Hallis’ expression doesn’t change, 
    save for the slightest furrowing of his brow."


    Hallis "\'Well?\' Hallis says finally, looking at you. \'Are we taking it?\'"

    Vo "\'I'm rich,\' Vo says faintly, still staring at the letter.
    His eyes are sparkling. \'Skyler, please tell me we’re doing this. 
    I could get so many fireworks with that much money.\'"
    
    menu:
        "'Of course we're taking the job'":
            jump END
            return
        "\'Do either of you know about this Alliance?\n 
                Can we trust them to pay up?\'":
            jump END
            return
    return
 
label Opening_letter:
    $ Narrative_variables["letter"] = True
    "You reach into the circle of glimmering light up to your forearm, the magic 
    pleasantly buzzing against your skin as you pull the letter out."

    "The lighting in the pavilion your group works out of is fine, and you move over 
    to beneath one of the floating globes of light that hover near the tops of the 
    pillars."
    call Read_Letter("Friends_Letter_Arrival") from _call_Read_Letter
    nvl clear
    jump Do_We_Accept_Letter
    return


label Read_Letter(next):
    "The script on the paper in your hands is dark and elegantly looping."
    nvl clear
    hide NVL with dissolve
    show Parchment with dissolve
    letter "To the group known as group: The Alliance Aspirant has need of your 
            particular services to further our cause."

    letter "As you well know, magic is banned in our neighbor kingdom of Aremoch, 
            in stark contrast to the freedom Eloas provides us." 

    letter "In our efforts to encourage the freedom of magic in Aremoch,
            we have placed agents and speakers in many of the kingdom’s cities."

    letter "We have recently lost contact with our agent in the city of Coruscos." 

    letter "Given your group’s reputation for creativity under duress, 
            we would like to hire you to find our missing agent and bring them home." 
    nvl clear
    letter "They most often frequented the Smog’s End tavern, and work under the alias of Cinder."
    letter "We are prepared to offer you a sum of five hundred dromos for accepting this contract, 
            and double that upon successful completion."

    letter "Simply sign below for further information to reveal itself."
    letter "{size=250}{font=b5wd.ttf}f{/font}{/size}{size=100}\nX:{/size}______________________________________________"
    nvl clear
    hide Parchment with dissolve
    show NVL with dissolve
    "There is no signature at the bottom of the letter, merely an odd symbol, 
    like an arc of light coming over the ridge of a mountain." 

    "An empty line waits for your signing."
    call expression next from _call_expression
    return
    
label Waiting_for_letter:
   $ Narrative_variables["letter"] = False
   call Friends_Letter_Arrival from _call_Friends_Letter_Arrival
   "You look at the letter."
   call Read_Letter("Do_We_Accept_Letter") from _call_Read_Letter_1
   return
   
label END:
    return
    return
