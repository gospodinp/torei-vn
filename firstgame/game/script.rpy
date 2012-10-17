# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg towers = "outskirts_by_kingcloud-d56ho2i.jpg"
image bg apt = "city_by_unidcolor-d4js0v5.jpg"
image bg space = "nearly_home_by_transience39.jpg"


# Declare characters used by this game.
#define e = Character('Eileen', color="#c8ffc8")


transform reset:
    xalign 0.5 yalign 0.5
    zoom 1.0 xzoom 1.0 yzoom 1.0
    crop None size None
    alpha 1.0
    rotate None

label tutorial_positions:

# The game starts here.
label start:
    play music "shagrugge_-_sprechen_sie_sanibel.ogg" noloop

    show bg space with dissolve:
        xpos -200 ypos -200
        parallel:
            linear 10.0 xpos -1000 ypos -800
        parallel:
            linear 10.0 zoom 2.0

    "Torei is my homeworld."

    "That's a funny word to our ears, \"homeworld\".  We're so used to thinking of Torei as the only world there ever was."



    show bg towers:
        zoom 1.0
        xpos -800 ypos 0 xanchor 0 yanchor 0
        linear 20.0 xpos 0 ypos -800

    "Men from other stars want to come here."

    "This is as new as space to us: we're not used to seeing so many men.  For all you hear about our plight, we are a planet of women."

    "But offworld men find us alluring.  I suppose that women from other stars do not learn to cherish and obey men as we have."

    show bg apt with dissolve:
        xpos 0 ypos 0
        linear 15.0 xpos -500 ypos -1200

    "My home is not the glamorous harem you may come to expect from reading \"Torean Love Slave\"."

    "I rent simple accomodations in an inexpensive district."

    "And as for my story, well it begins with a debt..."

    return
