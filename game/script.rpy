## The script of the game goes in this file.

    
# Initialize the nvl_menu display
init python:
    # sounds:
    def typewriter(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-typwriter.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def lowmale(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-lowmale.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
    def lowfemale(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-lowfemale.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
    def male(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-blipmale.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
    def female(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-blipfemale.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            
    def default(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx-default1.wav", channel="sound", loop=True, fadeout =3, fadein=3, tight=False)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

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
    
    # add arrow keys to progress through dialogue:
    config.keymap['dismiss'].append('K_RIGHT')
    config.keymap['rollback'].append('K_LEFT')

## Declare characters used by this game. The color argument colorizes the name
## of the character.
define Skyler = Character('Skyler', kind = nvl, who_color="21618C", what_color="AED6F1")
define Vo = Character('Vo', kind = nvl, who_color="6C3483", what_color="D7BDE2")
define Hallis = Character('Hallis', kind = nvl, who_color="922B21", what_color="D98880")
define narrator = Character(None, kind = nvl, what_color="FEF5E7") 
define letter = Character(None, bold=True, kind=nvl,what_color="000000", what_font="JandaElegantHandwriting.ttf", callback=typewriter)
define title = Character(None, what_color="E74C3C", what_font="KINGC___.ttf")

## Declare Image Files
image bg Aremoch city = "Greece.jpg"
image bg Campfire = "maxresdefault.jpg"
image NVL = "gui/nvl.png"
image Parchment = im.Scale("images/parchment.png",config.screen_width * 0.7, config.screen_height * 0.9,
                          align = (0.5, 0.3))

###################################################################
## TODO Notes:
# Fix Font Size/Color for Main Screen's Title
# Add Load for bottom
# Fix Figure Name
# Put individual sounds (Like in Phoenix Wright or Harvest Moon)
####################################################################

## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg Aremoch city
    play music "25 - Record 07 - STH Spring season map.mp3" fadein 2 fadeout 2
    show text ("{alpha=*0.3}{size=400}{font=KINGC___.ttf}{color=#FF0099}Kingdom Come{/color}{/font}{/size}{/alpha}")
    with dissolve
    pause 2
    hide text
    with dissolve
    ## These display lines of dialogue.
    
    jump Beginning
   
    ## This ends the game.

    return

############    BEGIN NARRATIVE     ############################################################


label Beginning:
    show NVL with dissolve
    "It’s been a while since work has kept you busy. Eloas isn’t a kingdom without 
    problems, per se, but lately the reputation for recklessness your group has acquired 
    seems to have discouraged some of the more tentative clients from approaching." 
    
    "You aren’t expecting anything different today, but when you open 
    the mail portal, you find a letter waiting inside."
    
    menu:
        "Open the letter":
            nvl clear
            $ Narrative_variables['open letter'] = True
            jump Opening_letter
            
        "Wait for {color=#922B21}Hallis{/color} and {color=#6C3483}Vo{/color}":
            nvl clear
            $ Narrative_variables['open letter'] = False
            jump Waiting_for_letter
            
label Friends_Letter_Arrival (cl=False):
    "The not-so-distant sound of bickering and good-natured laughter announces
    your friends’ joint arrival. Hallis and Vo enter the pavilion a moment later,
    eyes landing on the letter in your hands." 
    
    "Hallis gives the letter a curious
    look. His tall frame is dressed in elegant folds of forest-green cloth that
    complement his eyes." 
    
    Hallis "Correspondence? Do we have work again, Skyler?"

    "Vo sighs, leaning against a pillar. The cream-white of his toga loops around 
    one shoulder in lazy drapery, leaving a borderline-scandalous amount of tanned
    skin bare, save for what looks like charcoal stains and possibly burn marks."
  
    if cl is True:
        nvl clear
    "He summons a dancing orb of fire with an elegant pull of his wrist, and sets
    it to move in darting circles around the stone."

    Vo "There goes my plans for today. So what is it?"

    return
    
    
label Do_We_Accept_Letter:
    "You wordlessly hand Hallis the letter. Vo scowls at you, no bite to it, and 
    moves to stand next to Hallis on the tips of his toes to see properly."
    
    "Vo’s mouth moves soundlessly as he reads; Hallis’ expression doesn’t change, 
    save for the slightest furrowing of his brow, before he looks back at you."
    
    "The corner’s of Vo’s mouth are twitching, probably only just holding back one
    of his trademark grins."

    Hallis "Well, Skyler? Are we taking it?"
    nvl clear
    Vo "I’m going to be so damn rich. 
        Skyler, please tell me we’re doing this. I could get so many fireworks with that much money."
    
    menu:
        "'Of course we're taking the job'":
            $ Narrative_variables['trust alliance'] = True
            jump No_Questions_Asked
        "\'Do either of you know about this Alliance?\n 
                Can we trust them to pay up?\'":
            $ Narrative_variables['trust alliance'] = False
            jump Sketchy_Alliance
    return
 
label Opening_letter:
    $ Narrative_variables["letter"] = True
    "You reach into the circle of glimmering light up to your forearm, the magic 
    pleasantly buzzing against your skin as you pull the letter out."

    "The lighting in the pavilion your group works out of is fine, and you move over 
    to beneath one of the floating globes of light that hover near the tops of the 
    pillars."
    call Read_Letter
    call Friends_Letter_Arrival(True)
    jump Do_We_Accept_Letter
    return


label Read_Letter:
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
    letter "We are prepared to offer you a sum of five hundred{b} {i}dromos{/i}{/b} for accepting this contract, 
            and double that upon successful completion."

    letter "Simply sign below for further information to reveal itself."
    letter "{size=250}{font=b5wd.ttf}f{/font}{/size}{size=100}\nX:{/size}______________________________________________"
    nvl clear
    hide Parchment with dissolve
    show NVL with dissolve
    "There is no signature at the bottom of the letter, merely an odd symbol, 
    like an arc of light coming over the ridge of a mountain." 

    "An empty line waits for your signing."
    return
    
label Waiting_for_letter:
   $ Narrative_variables["letter"] = False
   call Friends_Letter_Arrival
   nvl clear
   "You look at the letter."
   call Read_Letter
   jump Do_We_Accept_Letter
   return
   
   
label Sketchy_Alliance:
    nvl clear
    Skyler "Do either of you know about this Alliance? Can we trust them to pay up?" 

    Hallis "I’ve heard of them. Public opinion is divided: no one argues that their
    cause is just, but stirring up insurrection in a foreign kingdom is hardly 
    an admirable method."
    
    "The globe of fire dances around Vo’s fingertips, separating into sparks for a
    moment before reconstituting itself. His grin is sharper than normal."

    Vo "Who cares about the method? Everyone should have the chance to live a 
    life with magic. How we get there doesn’t matter."


    Hallis "Regardless, there’s no doubting they have power, and they keep their 
    word. I think we can trust them to hold their end of the deal."

    menu:
        "I guess we're doing this, then. It's for a good cause.":
            $ Narrative_variables['reason'] = 'Pro-Mage'
            jump Sign_Contract
        "We have to pay the bills, somehow...":
            $ Narrative_variables['reason'] = 'Pro-Money'
            jump Sign_Contract
    return
   
label No_Questions_Asked:
    nvl clear
    Skyler "Of course we’re taking the job."
    
    "Vo snatches the letter from Hallis’ hands with no small amount of glee."
    
    Vo "Thanks the gods. I don’t care if we need to wade through sewers for this 
    job, I’m done with having to buy day old bread from the bakery. My projects 
    need more than just shitty phosphorus, Skyler. I need fire."


    Hallis "I don’t even know where to start with that. We aren’t that poor, 
    Vo. And I know for a fact that you’re still doing your little pyrotechnic
    experiments, because your neighbor came to me just last week to ask me to
    stop you."


    Vo "Aw, really? Which neighbor was it? No, let me guess: it was Mary, right?
    I told her I was sorry about the cactus."


    Hallis "I think the problem was rather more with the smell. Point being, you
    are not in dire straights right now, other than those of your own making."

    nvl clear
    Vo "Spoilsport. Skyler, you should be the one to sign. Me ‘n Hallis apparently
    have a lot to talk about, since he’s slandering my good name and all that."
   
    "He hands you the letter. You notice with some trepidation and no surprise 
    whatsoever that there appears to be some sort of gunpowder residue where 
    his fingers were touching it."

    "It’s possible ~ probable, even ~ that there is more to this job than meets
    the eye. It certainly won’t be easy, and it probably won’t be safe. You’ll 
    have to be ready." 
    
    menu:
        "Sign the contract":
            $Narrative_variables['sign immediately'] = True
            jump Sign_Contract
        "Make certain that Hallis and Vo know\nwhat they’re getting into":
            $Narrative_variables['sign immediately'] = False
            jump Check_On_Friends
    return

label Check_On_Friends:
    nvl clear
    "With your two friend’s incessant bickering, you don’t often speak up as much, 
    except to take charge as the situation demands. When you do speak, both of them 
    give you their undivided attention."
    
    Skyler "This might not be safe, and I don’t want to see either of you hurt. 
    Are you sure you want to do this?"


    "Hallis straightens, his impressive height made even more apparent by the motion. 
    His auburn hair falls over his eyes, and he brushes it away to look at you head-on.
    His voice is quiet and firm."


    Hallis "I trust you. This is what we do, after all. I’ll help make sure we all 
    stay safe."
    
    "There isn’t really anything Vo can do to make himself look tall, so he doesn’t 
    bother. But he does tie his mess of blonde hair back into a ponytail, and the
    expression on his face is as close to serious as it gets."

    nvl clear
    Vo "Count on me to get us out of bad situations. I don’t leave my friends 
    behind, and I’m sure as hell not letting you two have all the fun."


    "You smile at your friends and with a flourish, sign the bottom of the letter."
    jump Sign_Contract
    
label Sign_Contract:
    nvl clear
    "The moment you finish scrawling your name across the parchment, the letter 
    flares with golden light, building in intensity until you’re forced to shield 
    your eyes from the glare." 
    
    "Judging by Vo’s muttered swearing and Hallis’ surprised “oh!”, you aren’t the only 
    one caught off-guard. Letters float through the air, gleaming as they peel off the 
    parchment, only to settle back down in new positions and new runnels of ink." 


    "When the light fades back down, you are left with a map in your hands, locations 
    carefully labeled - sometimes with warnings. Vo peers over your shoulder and winces."


    Vo "Aw, man, we need to wear the bracelets? I hated wearing those things during 
        meditations. Makes my magic feel itchy."

    Hallis "That’s because it’s not used to being contained. It’s not supposed to be." 
    
    nvl clear
    
    "You notice Hallis rubbing his wrists, almost absentmindedly. Your tall friend 
    doesn’t often speak about his past, but he’s mentioned before that he once lived 
    in Aremoch." 
     
    menu:
        "Ask Hallis if he'll be okay with the bracelets":
            $Narrative_variables['Hallis Favor'] = Narrative_variables.get('Hallis Favor', 0) + 1 
            jump Hallis_Bracelets
        "Prepare to set off":
            $Narrative_variables['prepare immediately'] = True
            jump Prepare2go
    return
    
label Hallis_Bracelets:
    Skyler "Hallis, is everything alright? I know you’ve had experience with the 
            bracelets before."

    "Hallis’ brow is furrowed, but he gives you a grateful little smile at your 
    question." 

    Hallis "I’ll be fine, Skyler. Thanks for asking. It will just… take some time 
    to get used to it again. I’m more worried about the two of you." 

    "It’s true that the only time most of Eloas’ mages have had to wear magical 
    suppression bracelets was during training classes. You can vaguely remember 
    the feeling; it wasn’t a pleasant one. Wearing it for possibly days, even weeks 
    at a time… Vo makes a face that accurately sums up up your feelings on the matter."
    
    nvl clear
    
    Vo "I’m not saying it won’t suck, but I’ll deal. I use my magic to set my bombs 
    off. Guess I’ll just have to bring matches instead."

    "Hallis huffs out a laugh." 

    Hallis "Somehow, that makes me feel better. I’m not certain I’m happy about it."

    Vo "Love you too, Hallis."

    Skyler "Then I guess it’s time to get ready."
    nvl clear
    jump Prepare2go
    return

label Prepare2go:
    "The three of you agree to meet just outside of Aorna, the city closest 
    to the border of the two kingdoms. Hallis leaves the pavilion with a 
    mention of “preparations,” and Vo follows soon after muttering something 
    about explosives and “ten thousand fucking matches.” You are left to your 
    own devices, and so you return home to pack." 

    "Your family is Eloan nobility, and you have never had reason to leave the 
    kingdom. The togas and cloth wrappings so favored in Eloas are all you know; 
    with luck, it will serve adequately in your time in Coruscos as well." 
    
    "You pick clothing in shades of blues and greens, opening a bag far larger on 
     the inside than it seems and put the articles inside. Hallis is in charge of 
     food supply, as you cannot cook and Vo is no longer allowed anywhere near the spices."
    nvl clear
    
    "It’s not the first time that you’ve been grateful for Hallis’ stabilizing presence 
    in your group. Vo gives heart, but Hallis keeps you all sane." 

    "By the end, there’s only a little bit of space left in your pack, even with 
    the enchantment. You have space to pack one more thing, and two options catch 
    your eye." 

    "The first is a slender willow reed, a project you finished when you were a 
    child exploring enchantments. The runes covering it were inscribed by a 
    child’s careful hands, and when you shake it, the reed gives off a tremulous 
    white light in a forward direction." 
    
    "Your teacher considered it a failure because it didn’t disperse light evenly, 
     but you kept it as a memento."
    nvl clear
    "The second is a bag of dust, a purchase gleefully encouraged during a market 
    outing with Vo. When you throw a handful in the air, the dust shimmers and 
    creates an illusion of a wall, patterned to match the environment around it. 
    It lasts only for a few minutes, but, as Vo pointed out, that’s more than 
    enough time to cause a little mischief."
    
    menu:
        "Put the wand in the bag":
            $Narrative_variables['Bag'] = 'Wand'
        "Put the dust in the bag":
            $Narrative_variables['Bag'] = 'Dust'
    jump CampScene_going
    return
    
label CampScene_going:
    stop music fadeout 0.1
    play music "27 - Record 09 - AWL Winter theme.mp3" fadein 1 fadeout 5 loop
    scene bg Campfire with fade
    show NVL with dissolve
    nvl clear
    "Once you’re packed, you head out. It’s time to meet Hallis and Vo at the camp."
    
    $Narrative_variables['CampTalkFirst1'] = []
    jump CampScene_goingMenu
    return
    
label CampScene_goingMenu:
    menu:
        "Talk to Hallis" if 'Hallis' not in Narrative_variables['CampTalkFirst1']:
            $Narrative_variables['CampTalkFirst1'].append('Hallis')
            jump Camp_Hallis1
        "Talk to Vo" if 'Vo' not in Narrative_variables['CampTalkFirst1']:
            $Narrative_variables['CampTalkFirst1'].append('Vo')
            jump Camp_Vo1
        "Prepare for travel" if Narrative_variables['CampTalkFirst1']:
            jump Prepare4Travel
    return

label Camp_Hallis1:
    jump CampScene_goingMenu
    return
    
label Camp_Vo1:
    jump CampScene_goingMenu
    return
    
label Prepare4Travel:
    return
label END:
    return
    return
