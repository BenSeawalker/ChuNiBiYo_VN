# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg wb_0 = "bg_worldbuilders_0"
image bg wb_1 = "bg_worldbuilders_1"
image bg wb_2 = "bg_worldbuilders_2"
image bg wb_3 = "bg_worldbuilders_3"
image bg wb_4 = "bg_worldbuilders_4"
image bg wb_5 = "bg_worldbuilders_5"


# Declare characters used by this game.
define e = Character('Lucy', color="#c8ffc8")


# The game starts here.
label start:

    scene bg wb_0
    
    "In the Beginning, the world was dark."
    "There were no animals, or trees. Even the sky had nothing to fill it."
    "Then, the World Builders arrived."
    
    scene bg wb_1
    
    "They used powerful magics to bring everything to life."
    
    scene bg wb_2
    "They built many great and wonderful cities and temples, and lived in peace for millenia"
    
    
    "And then,"
    "one day,"
    "they dissapeared."
    "That's right, they vanished. Leaving no clues as to where they might have gone."
    "However, one of them was left behind."
    "This lone 'Wanderer' began a quest to find his people."
    "He determined to travel to each of the archives and gather the shards of 'The Artifact,' so that he might assemble
     the gate that would return him to the dimension from whence the World Builders had come."
    

    return
