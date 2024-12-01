#Dead Color Script

define w = Character("Whisper")

#Variables
default talkative = False
default thoughtful = False
default rational = False

default music = False
default classical = False
default jazz = False
default pop = False
default lofi = False
default metal = False
default silence = False

default workaholic = False
default coffee = False
default tea = False
default water = False
default lemonade = False

default stare = False
default fix = False
default despair = False

default fumes = False
default somethingelse = False


# Game Start
label start:
    scene bg black
    $ renpy.pause(1.0)
    "Are you happy?"
    menu:
        "Yes.":
            "Good for you."
            "For the sake of our protagonist, pretend you aren't."
            jump question2
        "Sometimes.":
            "A reasonable answer."
            "The bad things in life can make it hard to recognize the good."
            "The good things in life can make it hard to recognize the bad."
            "Our protagonist feels the same as you."
            jump question2
        "No.":
            "That’s unfortunate..."
            "...but your honesty is admirable."
            "Our protagonist, on the other hand, could use some of your self-awareness."
            jump question2


label question2:
    "Now, here's a hypothetical question:"
    "If you were forced to stare at a portrait, {i}oil on canvas,{/i} for hours on end..."
    "...would you talk to it?"
    menu:
        "Of course. Every painting has a personality.":
            $ talkative = True
            "That's very sweet of you."
            "In a hypothetical world where paintings have thoughts and feelings, they might appreciate you taking the time to talk to them."
            "Or maybe they'd wish you'd shut your trap for a while. Every painting has a personality, after all."
            jump question3
        "Sometimes. Just to think aloud.":
            $ thoughtful = True
            "You must be a deep thinker."
            "Wild guess:"
            "When you're alone, you pace around the room and mumble to yourself, don't you?"
            menu:
                "Right.":
                    "Birds of a feather."
                    jump question3
                "Wrong.":
                    "Well, you have me eating crow."
                    jump question3
                "I don't mumble.":
                    "Oh, you've got some moxie."
                    "Pace on, and think loudly."
                    "But maybe step {i}a little{/i} lighter if you have neighbors beneath you."
                    jump question3
        "Never. It's a piece of linen with paint on it.":
            $ rational = True
            "How rational of you."
            "Hopefully it's an interesting painting, for your sake."
            jump question3

label question3:
    "The final question is, by far, the most important."
    "Imagine you're the protagonist of this story."
    "You're an art conservator who once loved your job, but after years you've become discontented, plagued by doubt in every single thing you do."
    "What music do you jam to while working?"
    menu:
        "Moody classical.":
            $ music = True
            $ classical = True
            "Noted."
            jump gettingsettled
        "Even moodier jazz.":
            $ music = True
            $ jazz = True
            "Noted."
            jump gettingsettled
        #"Upbeat pop.":
            $ music = True
            $ pop = True
            "Noted."
            jump gettingsettled
        # "Flow-inducing lofi.":
            $ music = True
            $ lofi = True
            "Noted."
            jump gettingsettled
        #"Energizing heavy metal.":
            $ music = True
            $ metal = True
            "Noted."
            jump gettingsettled
        "Silence.":
            $ silence = True
            #"Interesting."
            "Noted."
            jump gettingsettled

label gettingsettled:
    scene bg deskbase with dissolve
    $ renpy.pause(1.0)
    show textbox with dissolve
    "You arrive at your desk."
    
    if music == True:
        show bg deskmusic
        play sound "7778click.mp3"
        $ renpy.pause(0.5)
        if classical == True:
            play music "KevinMacLeod-BlueFeather.mp3"
        if jazz == True:
            play music "KevinMacLeod-NightontheDocks-Sax.mp3"
        "The very first thing you do is play music on your Bluetooth speaker."
        "It helps you concentrate..."
        "...which is another way of saying that it drowns out the oppressive void of silence in your studio."
    if silence == True:
        "You consider playing music on your Bluetooth speaker, but you opt not to."
        "You want to work in silence for once."
    
    menu:
        "Prepare your materials.":
            $ workaholic = True
            "You're not messing around with this whole protagonist thing."
            "You get straight to business."
            jump preparematerials
        "Procrastinate.":
            $ renpy.pause(1.0)
            show fade with dissolve
            jump procrastinate

label procrastinate:
    $ renpy.pause(1.0)
    "{i}Of course{/i} you procrastinate."
    "The best way to start a good day's work is to put it off by another five minutes."
    "Or ten."
    "Maybe fifteen for good measure."
    "You check your email."
    "You scroll through news headlines, feeling increasingly chilled by the state of the world."
    "You guzzle a..."
    
    menu:
        "...mug of coffee.":
            $ coffee = True
            "It's your third cup already, but who's counting?"
            jump procrastinated
        "...cup of tea.":
            $ tea = True
            "As you drink, you curl your hands around the warm ceramic."
            "Your studio is always so cold. Only a cup of tea can make you right as rain."
            jump procrastinated
        "...glass of water.":
            $ water = True
            "You feel hydrated and refreshed."
            "After all, the water of life is, quite simply, {i}water.{/i}"
            jump procrastinated
        "...pitcher of lemonade.":
            $ lemonade = True
            "Really?"
            "A whole pitcher?"
            "At least you won't get scurvy."
            jump procrastinated
   
label procrastinated:
    "Once you've procrastinated for longer than you intended, you feel guilty enough to begin your work."
    $ renpy.pause(0.5)
    hide fade with dissolve
    jump preparematerials

label preparematerials:
    $ renpy.pause(0.5)
    "As a private art conservator of no renown, you work with paintings whose only perceived value is their age."
    "A former colleague of yours jokingly called them \"garage sale antiquities.\""
    "There's nothing wrong with the art itself."
    "However, you often find yourself with two types of clients:"
    "The type who rescued a family heirloom from beneath generations of attic junk, thinking they've stumbled upon a lost Da Vinci."
    "And the type who sees so little worth in a dusty old painting that they ask you to transform it into a practically different painting altogether."
    "Both are exhausting."
    $ renpy.pause(1.0)
    "This client is different."
    $ renpy.pause(1.0)
    "For one thing, he communicates only through mail."
    "Not {i}email.{/i}"
    "Handwritten letters."
    "Embarrassingly, you had to buy stamps just to write him back."
    "You asked him about the painting's origins."
    "He replied:"
    "{i}\"1857. Self-portrait, artist unknown. No, I do not have 'Wenmo,' nor any other digital payment services. Do you not take cash?\"{/i}"
    "This back and forth between you and your prospective client took over four months."
    "Why he didn't just hire a local conservator is beyond you, but money is money."
    "When an agreement was finalized and the contract was signed, he shipped his painting across the country..."
    "...which took another three weeks due to ambiguous delays."
    "All in all, nearly half a year passed before you finally got your hands on it."
    
    $ renpy.pause(1.0)
    show portrait start with dissolve
    $ renpy.pause(2.0)
    "The painting is exactly what you expected."
    "An old portrait, nothing remarkable, yellowed by oxidized varnish and the grime of a century with some decades to spare."
   
    #Sit

    "As you sit in front of it, you say..."
    menu:
        "\"Glad to finally make your acquaintance.\"":
            if talkative == True:
                "You politely introduce yourself to the painting."
                "It does not reply."
            if thoughtful == True:
                "That's a bit more sentimental than just 'thinking aloud,' isn't it?"
                "But okay. Say what you like. You're the protagonist, after all."
            if rational == True:
                "You {i}talk{/i} to a piece of linen?"
                "How out of character for you."
            jump workstart
        "\"Let's get you cleaned up, shall we?\"":
            if talkative == True:
                "The painting does not reply."
            if thoughtful == True:
                "The painting does not reply."
            if rational == True:
                "You {i}talk{/i} to a piece of linen?"
                "How out of character for you."
            jump workstart
        "Nothing. It's a piece of linen with paint on it.":
            if talkative == True:
                "You don't talk to it?"
                "Really?"
                "Best hope that in a hypothetical world where paintings have feelings, it's not insulted."
            if thoughtful == True:
                "Fair enough."
            if rational == True:
                "How very predictable of you."
            jump workstart

label workstart:
    menu:
        "Inspect the painting.":
            "As you settle into your work, you give the painting a closer inspection."
            "Obviously, it's oil paint on linen canvas, varnished with mastic."
            "These are all ordinary materials for the mid-nineteenth century. You know how to handle them."
            "There are a few worn patches, along with some spots where the paint cracked and chipped away."
            "You'll need to fill and retouch them, but you've seen far worse deterioration than this."
            "A good cleaning will bring the painting back to life."
            menu:
                "Flip the painting over.":
                    show portrait startback with dissolve 
                    "The back of the canvas is filthy and stained, but there are no rips or old patches to worry about."
                    "The wooden stretcher is in fine condition."
                    "Plus, there's plenty of canvas to work with for retacking."
                    "This should be an easy job."
                    menu:
                        "Remove the tacks.":
                            "Armed with your pliers and tack puller, you pry the tacks from their holes."
                            "One by one, they {i}tink{/i} onto your desk."
                            show portrait backuntacked
                            show tackjar
                            with dissolve
                            "When you're done, you sweep them into a little jar."
                            menu:
                                "Remove the stretcher.":
                                    "Carefully, you lift the stretcher from the canvas."
                                    show portrait backdusty with dissolve
                                    "Clumps of dust rain from it."
                                    "You wrinkle your nose to suppress a sneeze."
                                    menu:
                                        "Sweep the dust.":
                                            "You grab your brush and gently sweep the back of the painting, chasing clumps off the edge of the canvas."
                                            "After a century or two, every painting accumulates grime like this."
                                            "Canvas fibers, skin particles, dirt, pollen, ash."
                                            "Some of it might be old as the painting itself."
                                            show portrait backclean with dissolve
                                            show wastedirt with dissolve
                                            "You sweep the historical mess into the waste bin."
                                            "You say:"
                                            menu:
                                                "\"Your backside is nice and clean now.\"":
                                                    "The painting does not reply to your bad joke."
                                                    jump flip
                                                "\"Time to get that varnish off.\"":
                                                    "The painting does not refute you."
                                                    jump flip
                                                "Nothing.":
                                                    jump flip

label flip:
    "With an abundance of caution so you don't fold or tear the fragile canvas, you flip the painting to its front."
    show portrait flatdirty
    with dissolve
    "You meet eyes with the man in the portrait."
    "He looks like he's staring at you."
    "It's easy to stare back at him and feel..."
    menu:
        "...a connection to someone long dead.":
            "In this case, the man was not only the subject but the artist."
            "Every brushstroke on this canvas was a choice he made."
            "While looking at his eyes, you almost feel like he's reaching across time to send you a message."
            jump cleaning
        "...less alone.":
            "Well, he's certainly better company than a landscape."
            "And he's much more agreeable than that 1930s clown portrait you fixed up last week."
            jump cleaning
        "...watched.":
            "Portraits like this one unsettle you."
            if talkative == True:
                "Just because every painting has a personality doesn't mean they're all good ones."
                "There's a gleam in his eyes that you just don't like."
            if thoughtful == True:
                "It's hard to think when someone's watching you."
                "For some reason, he counts."
            if rational == True:
                "You're too much of a realist to believe in ghosts..."
                "...but every now and then you come across a painting that has {i}just a little{/i} too much life in its expression."
                "He strikes you in much the same way."
            jump cleaning

label cleaning:
    "You have to remind yourself that \"he\" is a piece of linen with paint on it."
    menu:
        "Roll a swab.":
            "You wrap a strip of cotton around the tip of a wooden stick."
            "Then you dip it in solvent."
            "Now, this is your favorite part."
            "You delicately touch the swab to the painting."
            "Twirling the stick between your forefinger and thumb, you roll the damp cotton over the surface of the canvas."
            show portrait flatpatch with dissolve
            "The varnish lifts, revealing a streak of blue-black from the yellow."
            show portrait flatsleeve with dissolve
            "You clean his sleeve and buttons."
            show portrait flatglove with dissolve
            "Then his glove."
            show portrait flatcoat with dissolve
            "Then the rest of his coat."
            "It's a dark, rich color, just as he originally intended."
            "Though you've become disenchanted with your work over the years, this part of the process is still magic to you."
            "It almost makes you forget your dissatisfaction."
            "It almost makes you forget your regrets."
            "You roll a new swab."
            show portrait flatcurtains with dissolve
            "When you clean the curtains, a soft red color flushes across the canvas."
            "Methodically, you begin cleaning the background from the bottom corner."
            show portrait flatdiscovery1 with dissolve
            "Halfway through, you make a discovery."
            show portrait flatdiscovery2 with dissolve
            "The subject appears to be standing by a window."
            "With as much patience as you can muster, you lift more varnish."
            "It's like peeling back a curtain made of old mastic."
            show portrait flathill with dissolve
            "You reveal a hill."
            "The sky and earth are sickly gray, as if all the color has leached from them."
            "The hill is dotted with skeletal black trees."
            "Two wisps of clouds hang above it, like remnants of a fog."
            menu:
                "\"Well, that's unexpected.\"":
                    jump hill
                "Mull quietly over your unexpected discovery.":
                    jump hill

label hill:
    "For several minutes, you can't look away from it."
    "Your eyes trace the thin clouds, sweep along the line of the hill, dance between the trees."
    "You feel odd..."
    "...like you've been caught in an whirlpool."
    "The hill fills you with..."
    menu:
        "...curiosity.":
            "This is the stuff art conservators dream of."
            "Of course you're curious."
            menu:
                "Clean the face.":
                    "You rein in your eagerness, trying to keep your hand steady for this final part."
                    jump facereveal
        "...dread.":
            "You’re not sure why, but that gray, lifeless hill bothers you."
            "In some dark corner of your mind, a corner that's all gut feelings and bad hunches and self-preservation, you know that this hill is something you shouldn't have seen."
            menu:
                "Clean...the face.":
                    "You don't {i}really{/i} want to clean the face."
                    "But it's your job."
                    "You need the money."
                    "And it's just a painting."
                    jump facereveal
    
label facereveal:
    "You remove the varnish from his face."
    "{i}Its{/i} face."
    show portrait flatface with dissolve
    "Color returns to the hair and cheeks."
    "The pale skin is stark against the rest of the canvas."
    "As always, you've left the eyes for last."
    "They require extra careful attention."
    "You dab the tip of a small cotton swab into the solvent and graze it over his right eye."
    show portrait flateye with dissolve
    #light flickers?
    "The {color=#ffffff}white{/color} shine on his iris is shockingly bright."
    "It nearly burns to look at, and it leaves a faint pinprick of an afterimage in your vision."
    "You force yourself to focus on the last patch of varnish."
    "You dab his left eye..."
    show portrait flatoops with dissolve
    $ renpy.pause(1.0)
    "...and come face-to-face with disaster."

    if music == True:
        stop music fadeout 4.0
        "The music fades in your ears."
    play music "721108__mrpogofficial__heartbeat.mp3" volume 2.0
    "Your heart hammers."
    menu:
        "Oh no.":
            jump mistake
        "Oh, god.":
            jump mistake
        "Oh, fuuuuuuu-":
            jump mistake

label mistake:
    "You look at the jar of solvent."
    "You look at the blotch of dissolved paint."
    menu:
        "\"I should've...I'm sorry, I...\"":
            $ stare = True
            "You stammer out an apology."
            "There is no reply."
            "If paintings really do have personalities, this one is clearly judging you."
            "You feel as though the {color=#ffffff}white{/color} in his eyes is burning straight into your soul."
            "After a minute of staring back at him, you realize something."
            jump underpainting
        "\"I can fix this.\"":
            $ fix = True
            "You're an art conservator."
            "You've fixed folds and rips."
            "You've mended canvases so tattered that they might as well have been made from lace."
            "And much like the man in this portrait, you're an artist."
            "You can repaint an eye. You can fix this."
            "On second glance, you realize something about the patch of dissolved paint."
            jump underpainting
        "You ruined it.":
            $ despair = True
            "How quickly you plunge into despair!"
            "You lash yourself with a dozen foul thoughts."
            "{i}So stupid!{/i}"
            "{i}So careless!{/i}"
            "{i}So worthless you are!{/i}"
            "You feel as though all your disappointment, all your unhappiness, all your self-loathing has been concentrated into one caustic hole on this canvas."
            "You ruined it because you ruin everything."
            "Before you can continue your mental self-flagellations, you realize something about the patch of dissolved paint."
            jump underpainting

label underpainting:
    $ renpy.pause(1.0)
    "The {color=#ffffff}white{/color} spot is very, very {color=#ffffff}white.{/color}"
    $ renpy.pause(0.5)
    "It's {i}obviously{/i} not a bald patch on the canvas."
    $ renpy.pause(0.5)
    "It's paint."
    $ renpy.pause(0.5)
    "Which means there might be an {i}underpainting.{/i}"

    if stare == True:
        "You can't help but smile at your judgmental little portrait."
        "Now you know his secrets."
    if fix == True:
        "This is accident of yours could be a happy one."
    if despair == True:
        "Perhaps you didn't ruin anything after all."

    "There are a number of reasons why something could be hidden beneath paint."
    "It could have been a correction on the part of the artist."
    "It could have been an old canvas that was repurposed to save materials."
    "It could have been the damn Victorians at it again, \"beautifying\" other people's work to make it more palatable for their parlors."
    "Whatever the reason, the right path forward would be to reach out to the owner and ask him how he'd like to proceed."
    "{color=#ffffff}{i}But that would take days, maybe weeks,{/i}{/color} says a little voice in your head."
    "If only your client had a damn cellphone."
    "Heck, even a landline would be an improvement for him."
    "You stare at the {color=#ffffff}white{/color} patch and rap your fingertips on the desk."
    "{color=#ffffff}{i}You want to know what is underneath the paint.{/i}{/color}"
    "Or maybe you don't."
    "Maybe it should be left alone."
    "{color=#ffffff}{i}Or maybe it should be cleaned off.{/i}{/color}"
    "{color=#ffffff}{i}Isn't paint just another form of dust?{/i}{/color}"
    "You..."
    menu:
        "...roll a swab and dip it in solvent.":
            jump rollaswab
        "{color=#ffffff}{i}...roll a swab and dip it in solvent.{/i}{/color}":
            jump rollaswab
        "...hold your head in your hands.":
            jump putty

label putty:
    $ renpy.pause(1.0)
    show fade with dissolve
    "Your latex gloves squeak against your face, and your nose fills with their rubbery stench."
    "Something about the {color=#ffffff}white{/color} paint..."
    "...doesn't feel right."
    "You assumed it was..."
    "...lead {color=#ffffff}white{/color}..."
    "...but it shouldn't...burn your eyes just to look at it."
    "And why is...thinking..."
    "...so...{i}hard{/i} all of a sudden?"
    "You feel like your skull is full of fog."
    "{color=#ffffff}{i}Maybe dipping a swab in solvent would help.{/i}{/color}"
    "You..."
    menu:
        "...roll a swab and dip it in solvent.":
            $ renpy.pause(1.0)
            hide fade with dissolve
            jump rollaswab
        "{color=#ffffff}{i}...roll a swab and dip it in solvent.{/i}{/color}":
            $ renpy.pause(1.0)
            hide fade with dissolve
            jump rollaswab
        "...pick up your putty knife.":
            $ renpy.pause(1.0)
            hide fade with dissolve
            "Your joints feel stiff, like they're made of wood."
            "Through sheer force of will, you pick up the putty knife and open a jar of filler."
            "You..."
            menu:
                "{color=#ffffff}{i}...ROLL A SWAB AND DIP IT IN SOLVENT.{/i}{/color}":
                    "You put down the putty knife."
                    "Your joints feel slick and free as you finally roll a swab and dip it in solvent."
                    jump rollaswab
                "...cover the {color=#ffffff}white{/color} with putty.":
                    show portrait flatputty with dissolve
                    stop music fadeout 1.0
                    "Your heartbeat slows."
                    "You stare at the smear of putty."
                    "Its creamy color is a breath of fresh air."
                    menu:
                        "Take a minute to consider what the hell just happened.":
                            "It was just white paint."
                            "Why was it such a struggle for you to move?"
                            "Why did you have trouble {i}thinking?{/i}"
                            "Maybe it was fumes."
                            "Something in the paint reacted with your solvent."
                            "You breathed it in."
                            "You felt cloudy for a minute."
                            "That's a reasonable explanation."
                            menu:
                                "Leave your desk and procrastinate.":
                                    jump puttyprocrastinate
                                "Get back to work.":
                                    jump puttywork
                        "Leave your desk and procrastinate.":
                            jump puttyprocrastinate
                        "Get back to work.":
                            jump puttywork
label puttyprocrastinate:
    $ renpy.pause(1.0)
    show fade with dissolve
    if workaholic == True:
        "Your hands tremble as you pour a glass of water."
        "It does nothing to soothe your nerves."
    if coffee == True:
        "Your hands tremble as you pour a fourth mug of coffee."
        "You blame it on the caffeine."
    if tea == True:
        "Your hands tremble as you make a cup of tea."
        "For once, it doesn't make you right as rain."
    if water == True:
        "Your hands tremble as you pour a glass of water."
        "It does nothing to soothe your nerves."
    if lemonade == True:
        "Your hands tremble as you grab a pitcher of lemonade."
        "You scrunch your face. This one tastes much too sour."
    "You pull out your phone and check your email."
    "Your eyes glaze over the unread messages. They're mostly ads anyway."
    "You scroll through news headlines."
    "They feel like they happened in another world. The {i}real{/i} world. Not the one you're living in right now."
    "You search \"dangers of white paint\" on the internet and get the expected results."
    "Fumes."
    "That was probably it."
    menu:
        "Yes. Fumes.":
            $ fumes = True
            "Believe what you want to believe."
            "The fact of the matter is, that painting is not yours."
            "You signed a contract."
            "You need the money."
            "You're going to finish the job."
            menu:
                "Get back to work.":
                    jump puttywork
        "No. It was something else.":
            $ somethingelse = True
            "Believe what you want to believe."
            "The fact of the matter is, that painting is not yours."
            "You signed a contract."
            "You need the money."
            "You're going to finish the job."
            menu:
                "Get back to work.":
                    jump puttywork

label puttywork:
    $ renpy.pause(1.0)
    hide portrait
    hide tackjar
    hide wastedirt
    hide fade
    show bg black
    with dissolve
    "And so you work."
    "You stretch and retack the canvas."
    "You patch the chipped spots with putty."
    "You brush on varnish and paint and varnish again."
    $ renpy.pause(1.0)
    show bg deskbase
    show portrait finished
    with dissolve
    "After days, you finish the job."
    "As you admire your fine work, you notice one speck of {color=#ffffff}white{/color} in the right eye."
    if fumes == True:
        "{i}Fumes,{/i} you remind yourself."
    if somethingelse == True:
        "You know it's not natural."
    menu:
        "\"I'd say it was a pleasure, but...well...it wasn't.\"":
            "The painting does not reply."
            jump statusquo
        "\"We're done here.\"":
            "The painting does not reply."
            jump statusquo
        "Just pack it up.":
            jump statusquo

label statusquo:
    "You remove the painting from your desk and prepare it for packaging."
    "To get your money's worth from the stamps, you write a letter to send ahead of the portrait, informing your client of the job's completion."
    "In the letter you..."
    menu:
        "...mention the underpainting.":
            "Your client deserves to know, after all."
            "You can only hope that he doesn't undo your hard work by trying to take a look for himself."
            $ renpy.pause(0.5)
            "But that's not your problem, really."
            "You're an art conservator."
            "You conserved the art."
            "It's just what you do."
            jump statusquoend
        "...don't mention the underpainting.":
            "Your client doesn't need to know."
            "No one needs to know."
            "Maybe in one hundred and fifty years, another art conservator will tend to the painting and find what you covered up."
            "But that's so far away, so beyond your lifetime, that it might as well never happen."
            "You're an art conservator."
            "You conserved the art."
            "It's just what you do."
            jump statusquoend

label statusquoend:
    hide portrait
    show bg black
    with dissolve
    $ renpy.pause(1.0)
    "{cps=20}- END -\nSTATUS QUO{/cps}"
    $ renpy.pause(1.0)
    "Hello again, old friend."
    "Now that our protagonist's story has come to an end, here are three kernels of wisdom."
    "Don't clean paintings in the dark."
    "Don't use solvents without patch tests."
    "And for the love of god,\nsend your cursed paintings through priority mail."
    $ renpy.pause(0.5)
    "Thanks for playing!\nMay you find what makes you truly happy."
    return

label rollaswab:
    "Vigorously, you rub the saturated swab over the face."
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    show portrait flatpeekaboo
    with dissolve
    $ renpy.pause(1.0)
    "{color=#ffffff}{cps=20}{i}Something{/i}{/color} stares at you.{/cps}"
    play music "702966__zhr__loopable-horror-ambience.mp3"
    "{cps=20}You feel...{/cps}"
    "{cps=100}{i}...like a rabbit...{/i}{/cps}"
    "{cps=100}{i}...like a mouse...{/i}{/cps}"
    "{cps=100}{i}...like a lark...{/i}{/cps}"
    "{cps=100}{i}...like a deer...{/i}{/cps}"
    "{cps=20}...caught in the maw of...{/cps}"
    "{cps=100}{i}...a {color=#ffffff}fox{/color}...{/i}{/cps}"
    "{cps=100}{i}...a {color=#ffffff}cat{/color}...{/i}{/cps}"
    "{cps=100}{i}...a {color=#ffffff}hawk{/color}...{/i}{/cps}"
    "{cps=100}{i}...a {color=#ffffff}wolf{/color}.{/i}{/cps}"
    "{cps=20}You smell{/cps} {cps=100}{i}{color=#ffffff}paint{/color} in the pot...{/i}{/cps}"
    "{cps=100}{i}...wood in the fire...{/i}{/cps}"
    "{cps=100}{i}...soil in the hill.{/i}{/cps}"
    if coffee == True:
        "{cps=10}You taste{/cps} {cps=100}{i}sap bleeding from the tree, {color=#ffffff}blood{/color} seeping from the wound, coffee dripping from the mug.{/i}{/cps}"
    elif tea == True:
        "{cps=10}You taste{/cps} {cps=100}{i}sap bleeding from the tree, {color=#ffffff}blood{/color} seeping from the wound, tea dripping from the cup.{/i}{/cps}"
    elif lemonade == True:
        "{cps=10}You taste{/cps} {cps=100}{i}sap bleeding from the tree, {color=#ffffff}blood{/color} seeping from the wound, lemonade dripping from the pitcher.{/i}{/cps}"
    else:
        "{cps=10}You taste{/cps} {cps=100}{i}sap bleeding from the tree, {color=#ffffff}blood{/color} seeping from the wound, water dripping from the glass.{/i}{/cps}"
    "The {color=#ffffff}white{/color} is so clean, so bright, so filthy, so dark..."
    menu:
        "...so wrong.":
            "{color=#ffffff}{i}The secrets buried within the secrets buried within the secrets are yours for the knowing if only you would...{/i}{/color}"
            menu:
                "{color=#ffffff}{i}...drink from the font of the Dead One.{/i}{/color}":
                    jump drinkfromfont
                "...pour turpentine on the canvas...":
                    show portrait flatturpentine with dissolve
                    menu:
                        "...and clean.":
                            jump turpentine
        "...so {color=ffffff}right{/color}.":
            "{color=#ffffff}{i}The secrets buried within the secrets buried within the secrets are yours for the knowing if only you would...{/i}{/color}"
            menu:
                "...drink from the font of the {color=#ffffff}Dead One.{/color}":
                    jump drinkfromfont

label turpentine:
    $ renpy.pause(1.0)
    "To hell with conservation."
    show portrait flatscrubbed with dissolve
    "You dissolve and rub and scrape and scrub..."
    $ renpy.pause(0.5)
    show portrait flatblank with dissolve
    stop music fadeout 4.0
    "...until all that's left is a piece of linen."
    $ renpy.pause(1.0)
    "You sit back on your stool and look at the mess you've made."
    "{i}Cleaned.{/i}"
    "The mess you've cleaned."
    $ renpy.pause(2.0)
    "With slow inevitability, like a slug peeling off a ceiling, the reality of your situation hits you in the face."
    "{i}1857. Self-portrait, artist unknown.{/i}"
    "You {i}obliterated{/i} your client's painting."
    "Never, in the history of your career, have you screwed up quite so atrociously."
    "You're going to have to fight with your insurance company for months. They sure as hell won't cover you for \"haunted white paint.\""
    "You're never going to be entrusted with a painting again, even one as mundane as somebody's great-uncle's still life of an apple and a vase on a tablecloth."
    "You're going to have to find something else to do with your life."
    "The thought makes you feel..."
    $ renpy.pause(1.0)
    "..."
    $ renpy.pause(1.0)
    "...empty."
    $ renpy.pause(1.0)
    "But oddly enough, it's a good kind of empty."
    "Like a blank canvas."
    jump blankcanvas

label blankcanvas:
    scene bg black with dissolve
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    "{cps=20}- END -\nA BLANK CANVAS{/cps}"
    $ renpy.pause(1.0)
    "Hello again, old friend."
    "Now that our protagonist's story has come to an end, here are three kernels of wisdom."
    "Don't clean paintings in the dark."
    "Don't use solvents without patch tests."
    "And for the love of god,\ndon't drink paint, even if it asks you to."
    $ renpy.pause(0.5)
    "Thanks for playing!\nMay you find what makes you truly happy."
    return

label drinkfromfont:
    show portrait flatooze with dissolve
    $ renpy.pause(1.0)
    "{color=#ffffff}White{/color} oozes up from the paint."
    "Curiously, it looks like {color=#ffffff}liquid marshmallow{/color} bursting from a crust of char."
    "It reminds you of a time when you sat by a warm, crackling campfire..."
    "...a brief moment in your childhood..."
    "...when everything was still possible..."
    "...and you were happy."
    "You gaze at the {color=#ffffff}white{/color} like you gazed at that fire."
    show portrait flatfountain behind textbox with dissolve
    "You watch as it runs off the canvas, then spills over the edge of your desk like a waterfall from mossy rocks."
    "You curl your hand into a cup, {color=#ffffff}{i}for the most precious of vessels are the ones made of flesh,{/i}{/color} and you bring the {color=#ffffff}white{/color} to your lips."
    "It shimmers like a rainbow in a thin mist."
    "{color=#ffffff}{cps=100}{i}And you are going to taste it you are going to taste the light and all its colors and then it is upon your tongue like honey made from wood anemone grown out of the foul sweetness of meat long surrendered to the rot and then it is down your throat sparkling like stars and warm like the sun at its pinnacle on the longest day and then it is in you and then it is you and then...{/i}{/cps}{/color}"
    scene bg white
    $ renpy.pause(3.0)
    "{color=#000000}Show me the color of thy heart.{/color}"
    "{color=#000000}Paint a portrait of thyself, so that I may gaze upon thee."
    menu:
        "Paint a self portrait for {color=#ffffff}the Words in the White.{/color}":
            $ renpy.pause(2.0)
            scene bg rubedo with dissolve
            $ renpy.pause(4.0)
            jump rubedo

label rubedo:
    scene bg black
    stop music fadeout 1.0
    $ renpy.pause(1.0)
    "{cps=20}- END -\nRUBEDO{/cps}"
    $ renpy.pause(1.0)
    "Hello again, old friend."
    "Now that our protagonist's story has come to an end, here are three kernels of wisdom."
    "Don't clean paintings in the dark."
    "Don't use solvents without patch tests."
    "And for the love of god,\ndon't drink paint, even if it asks you to."
    $ renpy.pause(0.5)
    "Thanks for playing!\nMay you find what makes you truly happy."
    return

return
