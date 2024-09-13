#invader game

"""

if this program doesn't work in your environment,

    try to open command prompt and type 'pip install pygame'!

"""

#--------------------------------#

from pygame import mixer

import random

import tkinter

#--------------------------------#

mixer.init()

#title font
T_FONT = ("System", 60)

#fnt of others
S_FONT = ("System", 25)

#scene is friquently changed to distingish what player, invaders or programs, are doing 
scene = "title"

count = 3

BDR = 500

#this variable makes invaders be able to move \('')/  /('')\ 
i_motion = 1

#variable to delete player's beam when it hits invaders
t_f = False

#a variable to detect which key player has pressed
k = ""

#width and height of player's ship
s_w = 40
s_h = 16

#width and height of invaders
i_w = 30
i_h = 30

#center location, width and height of player's beam
b_x = 300
b_y = 650
b_w = 2
b_h = 5

#variables whether invaders can beam or not
#each invader can beam when this variable is True
i_0 = True
i_1 = True
i_2 = True
i_3 = True
i_4 = True

#main function
def main():

    #use "gloabal" to change these variables
    global SHIP, INV_0, INV_1, INV_2, INV_3, INV_4, enemy, s_x, s_y
    global i_0_x, i_1_x, i_2_x, i_3_x, i_4_x, i_0_y, i_1_y, i_2_y, i_3_y, i_4_y, i_0_v, i_1_v, i_2_v, i_3_v, i_4_v
    global i0_b_x, i0_b_y, i1_b_x, i1_b_y, i2_b_x, i2_b_y, i3_b_x, i3_b_y, i4_b_x, i4_b_y


    if scene == "title":

        #this list memories whether each invader is dead or not

        """

        if one of the enemies is dead,

            the value changes to 1 from 0

        """
        
        enemy = [0, 0, 0, 0, 0]

        #location of player's ship
        s_x = 300
        s_y = 650
        
        #locations of invaders
        i_0_x, i_0_y = 50, 100
        i_1_x, i_1_y = 100, 100
        i_2_x, i_2_y = 150, 100
        i_3_x, i_3_y = 200, 100
        i_4_x, i_4_y = 250, 100

        #velocity of invaders

        """

        of course you can change these values,
        
            but sometimes your beam bypass invaders when velocity is more than 7

        """
        
        i_0_v = 5
        i_1_v = 5
        i_2_v = 5
        i_3_v = 5
        i_4_v = 5
        
        #location of invaders' beam
        i0_b_x, i0_b_y = 0, 0
        i1_b_x, i1_b_y = 0, 0
        i2_b_x, i2_b_y = 0, 0
        i3_b_x, i3_b_y = 0, 0
        i4_b_x, i4_b_y = 0, 0

        #this means deleting all stuff on the screen
        cvs.delete("all")
        
        #title screen
        cvs["bg"] = "black"
        cvs.create_text(300, 250, text = "INVADER GAME", fill = "lime", font = T_FONT)
        cvs.create_text(301, 250, text = "INVADER GAME", fill = "white", font = T_FONT)
        cvs.create_text(300, 500, text = "Press 'ENTER' to Start", fill = "white", font = S_FONT)

    if scene == "count_down":

        cvs.delete("all")
        cvs.create_image(300, 340, image = IMAGES[2])

        #create images of invaders
        cvs.create_image(200, 100, image = IMAGES[0], tag = "INV_0")
        cvs.create_image(250, 100, image = IMAGES[0], tag = "INV_1")
        cvs.create_image(300, 100, image = IMAGES[0], tag = "INV_2")
        cvs.create_image(350, 100, image = IMAGES[0], tag = "INV_3")
        cvs.create_image(400, 100, image = IMAGES[0], tag = "INV_4")

        #create an image of player's ship
        cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "blue", outline = "black", tag = "SHIP")

        #create a border line

        """

        if invaders are beyond this line,
        
            player will lose a game :(

        you can move border line by changing variable 'BDR'

        """
        
        cvs.create_line(0, BDR, 600, BDR, fill = "red", width = 3)

        #call "count_down" function
        root.after(1000, count_down)

def count_down():

    global count, scene
    
    #call "count_down" function after 1000 ms until the variable "count" becomes 0
    if count > 0 and scene == "count_down":
        cvs.delete("COUNT")
        cvs.create_text(300, 300, text = str(count), font = S_FONT, tag = "COUNT")
        
        count -= 1

        mixer.music.load("musics/count_down.mp3")
        mixer.music.play(1)
        
        root.after(1000, count_down)

    else:
        cvs.delete("COUNT")
        count = 3

        scene = "game"

        #call "invaders" function
        root.after(15, invaders)
        root.after(15, beam_i)

def key_p(p):

    #use "global" to change values of s_x and s_y, and to change "k" at the other function
    global s_x, s_y, b_x, k, SHIP, scene

    #this variable memories what key you pressed ("Return" means Enter)
    k = p.keysym

    if k == "Return" and scene == "title":

        scene = "count_down"
        k = ""

        mixer.music.load("musics/start.mp3")
        mixer.music.play(1)

        #call main function after 15ms
        root.after(15, main)
    
    if k == "Left" and (scene == "game" or scene == "beam"):

        #when you press "LEFT" key, your ship will move 5 pixels left
        s_x -= 5
        cvs.delete("SHIP")
        cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "blue", outline = "black", tag = "SHIP")
        k = ""
        
    if k == "Right" and (scene == "game" or scene == "beam"):

        #when you press "RIGHT"key, your ship will move 5 pixels right
        s_x += 5
        cvs.delete("SHIP")
        cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "blue", outline = "black", tag = "SHIP")
        k = ""

    if k == "space" and scene == "game":

        """

        press SpaceKey to beam!

        """

        mixer.music.load("musics/beam.mp3")
        mixer.music.play(1)

        b_x = s_x

        #call beam_p function after 15ms
        root.after(15, beam_p)

    if k == "Up":

        scene = "title"
        k = ""

        #call main function after 600ms
        root.after(600, main)

def beam_p():

    """

    this function is for player

    """

    global b_y, k, scene, t_f

    #prevent rapid firing by changing "scene" 
    scene = "beam"
    

    #beam velocity

    """

    as well as invaders' beam velocity,

        if you change this to a big number,

            your beam probably bypass invaders :(

    """
    
    b_y -= 5

    """

    until your beam reaches at the end of the screen,

        repeat making and deleting it

    """
    
    if b_y <= 5 or t_f or scene == "game_over" or scene == "game_clear":
        
        cvs.delete("BEAM")
        
        scene = "game" 
        b_y = 650
        k = ""
        t_f = False

    else:

        cvs.delete("BEAM")
        cvs.create_rectangle(b_x - b_w, b_y - b_h , b_x + b_w, b_y + b_h, fill = "yellow", outline = "black", tag = "BEAM")

        
        #call this function after 15ms
        root.after(15, beam_p)

#the function for invaders
def invaders():
    
    global INV_0, INV_1, INV_2, INV_3, INV_4, i_0_x, i_0_y, i_1_x, i_1_y, i_2_x, i_2_y, i_3_x, i_3_y, i_4_x, i_4_y
    global i_0_v, i_1_v, i_2_v, i_3_v, i_4_v, enemy, scene, i_motion, t_f, i_0_b, i_1_b, i_2_b, i_3_b, i_4_b
    global i0_b_x,i0_b_y, i1_b_x, i1_b_y, i2_b_x, i2_b_y, i3_b_x, i3_b_y, i4_b_x, i4_b_y, SHIP

    #location + velocity
    i_0_x += i_0_v
    i_1_x += i_1_v
    i_2_x += i_2_v
    i_3_x += i_3_v
    i_4_x += i_4_v

    #this function only work when "scene" is beam or game
    if scene == "beam" or scene == "game":

        #use abs function and set a hit box of invaders
        if abs(i_0_x - b_x) <= (i_w / 2) + (b_w / 2) and abs(i_0_y - b_y) <= (i_w / 2) + (b_h / 2) and enemy[0] == 0:

            enemy[0] = 1
            cvs.delete("INV_0")

            mixer.music.load("musics/enemy_dead.mp3")
            mixer.music.play(1)

            t_f = True

        if abs(i_1_x - b_x) <= (i_w / 2) + (b_w / 2) and abs(i_1_y - b_y) <= (i_w / 2) + (b_h / 2) and enemy[1] == 0:

            enemy[1] = 1
            cvs.delete("INV_1")

            mixer.music.load("musics/enemy_dead.mp3")
            mixer.music.play(1)

            t_f = True

        if abs(i_2_x - b_x) <= (i_w / 2) + (b_w / 2) and abs(i_2_y - b_y) <= (i_w / 2) + (b_h / 2) and enemy[2] == 0:

            enemy[2] = 1
            cvs.delete("INV_2")

            mixer.music.load("musics/enemy_dead.mp3")
            mixer.music.play(1)

            t_f = True

        if abs(i_3_x - b_x) <= (i_w / 2) + (b_w / 2) and abs(i_3_y - b_y) <= (i_w / 2) + (b_h / 2) and enemy[3] == 0:

            enemy[3] = 1
            cvs.delete("INV_3")
        
            mixer.music.load("musics/enemy_dead.mp3")
            mixer.music.play(1)

            t_f = True

        if abs(i_4_x - b_x) <= (i_w / 2) + (b_w / 2) and abs(i_4_y - b_y) <= (i_w / 2) + (b_h / 2) and enemy[4] == 0:

            enemy[4] = 1
            cvs.delete("INV_4")

            mixer.music.load("musics/enemy_dead.mp3")
            mixer.music.play(1)

            t_f = True

        #judgement whether invaders reach a border
        if (BDR - i_0_y) < (i_w / 2) and enemy[0] == 0:

            scene = "game_over"

            root.after(2000, game_over)

        if (BDR - i_1_y) < (i_w / 2) and enemy[1] == 0:

            scene = "game_over"

            root.after(2000, game_over)

        if (BDR - i_2_y) < (i_w / 2) and enemy[2] == 0:

            scene = "game_over"

            root.after(2000, game_over)

        if (BDR - i_3_y) < (i_w / 2) and enemy[3] == 0:

            scene = "game_over"

            root.after(2000, game_over)

        if (BDR - i_4_y) < (i_w / 2) and enemy[4] == 0:

            scene = "game_over"

            root.after(2000, game_over)

        #set a hit box of player's ship
        if abs(s_x - i0_b_x) <= (s_w / 2 + b_w / 2) and abs (s_y - i0_b_y) <= (s_h / 2 + b_h / 2):

            scene = "game_over"

            cvs.delete("SHIP")
            cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "green", outline = "black")

            mixer.music.load("musics/p_dead.mp3")
            mixer.music.play(1)

            root.after(2000, game_over)

        if abs(s_x - i1_b_x) <= (s_w / 2 + b_w / 2) and abs (s_y - i1_b_y) <= (s_h / 2 + b_h / 2):

            scene = "game_over"

            cvs.delete("SHIP")
            cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "green", outline = "black")

            mixer.music.load("musics/p_dead.mp3")
            mixer.music.play(1)

            root.after(2000, game_over)

        if abs(s_x - i2_b_x) <= (s_w / 2 + b_w / 2) and abs (s_y - i2_b_y) <= (s_h / 2 + b_h / 2):

            scene = "game_over"

            cvs.delete("SHIP")
            cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "green", outline = "black")

            mixer.music.load("musics/p_dead.mp3")
            mixer.music.play(1)

            root.after(2000, game_over)

        if abs(s_x - i3_b_x) <= (s_w / 2 + b_w / 2) and abs (s_y - i3_b_y) <= (s_h / 2 + b_h / 2):

            scene = "game_over"

            cvs.delete("SHIP")
            cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "green", outline = "black")

            mixer.music.load("musics/p_dead.mp3")
            mixer.music.play(1)

            root.after(2000, game_over)

        if abs(s_x - i4_b_x) <= (s_w / 2 + b_w / 2) and abs (s_y - i4_b_y) <= (s_h / 2 + b_h / 2):

            scene = "game_over"

            cvs.delete("SHIP")
            cvs.create_rectangle(s_x - 20, s_y - 8, s_x + 20, s_y + 8, fill = "green", outline = "black")

            mixer.music.load("musics/p_dead.mp3")
            mixer.music.play(1)

            root.after(2000, game_over)

        #when invaders go right and they reach at the eadge of the screen, next they will go left, and vice versa
        if 600 - i_0_x < 20 or i_0_x < 20 and enemy[0] == 0:

            i_0_v = -i_0_v
            i_0_y += 100

        if 600 - i_1_x < 20 or i_1_x < 20 and enemy[1] == 0:

            i_1_v = -i_1_v
            i_1_y += 100

        if 600 - i_2_x < 20 or i_2_x < 20 and enemy[2] == 0:

            i_2_v = -i_2_v
            i_2_y += 100

        if 600 - i_3_x < 20 or i_3_x < 20 and enemy[3] == 0:

            i_3_v = -i_3_v
            i_3_y += 100

        if 600 - i_4_x < 20 or i_4_x < 20 and enemy[4] == 0:

            i_4_v = -i_4_v
            i_4_y += 100

        for i in range(5):

            cvs.delete(f"INV_{i}")

        #after game starts, if invaders are still alive, delete and create images of them
        if enemy[0] == 0:

            cvs.create_image(i_0_x, i_0_y, image = IMAGES[i_motion], tag = "INV_0")

            #when i_n (n = 0, 1, 2, 3, 4) is True, there's a 10% chance that invaders beam

            """

            if you want to change the probability of invaders' beam,

                you need to change  'randint.randint'  argument

            for examle, 'random.randint(1, 5) >> 20%', 'random.randint(1, 20) >> 5%', 'randint(1, 100) >> 1%'

            however, '1' must include in a range of an argument

            """
            
            if i_0:

                i_0_b = random.randint(1, 10)

                if i_0 and i_0_b == 1:

                    mixer.music.load("musics/i_beam.mp3")
                    mixer.music.play(1)
                    
                i0_b_x = i_0_x
                i0_b_y = i_0_y
        
        if enemy[1] == 0:

            cvs.create_image(i_1_x, i_1_y, image = IMAGES[i_motion], tag = "INV_1")

            if i_1:

                i_1_b = random.randint(1, 10)

                if i_1 and i_1_b == 1:

                    mixer.music.load("musics/i_beam.mp3")
                    mixer.music.play(1)
                    
                i1_b_x = i_1_x
                i1_b_y = i_1_y

        if enemy[2] == 0:

            cvs.create_image(i_2_x, i_2_y, image = IMAGES[i_motion], tag = "INV_2")

            if i_2:

                i_2_b = random.randint(1, 10)

                if i_2 and i_2_b == 1:

                    mixer.music.load("musics/i_beam.mp3")
                    mixer.music.play(1)
                    
                i2_b_x = i_2_x
                i2_b_y = i_2_y

        if enemy[3] == 0:

            cvs.create_image(i_3_x, i_3_y, image = IMAGES[i_motion], tag = "INV_3")

            if i_3:

                i_3_b = random.randint(1, 10)

                if i_3 and i_3_b == 1:

                    mixer.music.load("musics/i_beam.mp3")
                    mixer.music.play(1)
                    
                i3_b_x = i_3_x
                i3_b_y = i_3_y

        if enemy[4] == 0:

            cvs.create_image(i_4_x, i_4_y, image = IMAGES[i_motion], tag = "INV_4")

            if i_4:

                i_4_b = random.randint(1, 10)

                if i_4 and i_4_b == 1:

                    mixer.music.load("musics/i_beam.mp3")
                    mixer.music.play(1)
                    
                i4_b_x = i_4_x
                i4_b_y = i_4_y

        if scene == "game" or scene == "beam":

            i_motion = 1 - i_motion
            root.after(100, invaders)

        if set(enemy) == {1}:

            mixer.music.load("musics/game_clear.mp3")
            mixer.music.play(1)

            scene = "game_clear"

            root.after(500, game_clear)

#function about invaders' beam
def beam_i():

    global i_0, i_1, i_2, i_3, i_4, i0_b_y, i1_b_y, i2_b_y, i3_b_y, i4_b_y

    if i_0_b == 1:

        if i0_b_y >= 680:
            
            cvs.delete("BEAM_0")
            i_0 = True

        else:

            i_0 = False
        
            i0_b_y += 5

            cvs.delete("BEAM_0")
            cvs.create_rectangle(i0_b_x - b_w, i0_b_y - b_h, i0_b_x + b_w, i0_b_y + b_h, fill = "red", outline = "black", tag = "BEAM_0")

    if i_1_b == 1:

        if i1_b_y >= 680:

            cvs.delete("BEAM_1")
            i_1 = True

        else:
            
            i_1 = False

            i1_b_y += 5

            cvs.delete("BEAM_1")
            cvs.create_rectangle(i1_b_x - b_w, i1_b_y - b_h, i1_b_x + b_w, i1_b_y + b_h, fill = "red", outline = "black", tag = "BEAM_1")

    if i_2_b == 1:

        if i2_b_y >= 680:

            cvs.delete("BEAM_2")
            i_2 = True

        else:
            
            i_2 = False

            i2_b_y += 5

            cvs.delete("BEAM_2")
            cvs.create_rectangle(i2_b_x - b_w, i2_b_y - b_h, i2_b_x + b_w, i2_b_y + b_h, fill = "red", outline = "black", tag = "BEAM_2")

    if i_3_b == 1:

        if i3_b_y >= 680:

            cvs.delete("BEAM_3")
            i_3 = True

        else:
            
            i_3 = False

            i3_b_y += 5

            cvs.delete("BEAM_3")
            cvs.create_rectangle(i3_b_x - b_w, i3_b_y - b_h, i3_b_x + b_w, i3_b_y + b_h, fill = "red", outline = "black", tag = "BEAM_3")

    if i_4_b == 1:

        if i4_b_y >= 680:

            cvs.delete("BEAM_4")
            i_4 = True

        else:
            
            i_4 = False

            i4_b_y += 5

            cvs.delete("BEAM_4")
            cvs.create_rectangle(i4_b_x - b_w, i4_b_y - b_h, i4_b_x + b_w, i4_b_y + b_h, fill = "red", outline = "black", tag = "BEAM_4")


    if scene == "game" or scene == "beam":
        
        root.after(30, beam_i)

#this function is called when player lost a game
def game_over():

    cvs.delete("all")
    cvs.create_image(300, 340, image = IMAGES[4])
    cvs.create_text(300, 300, text = "YOU LOSE", font = T_FONT)
    cvs.create_text(300, 550, text = "Press 'Up' to go back to the title", font = S_FONT)

#this function is called when player won a game
def game_clear():

    cvs.delete("all")
    cvs["bg"] = "white"
    cvs.create_image(300, 340, image = IMAGES[3])
    cvs.create_text(300, 300, text = "YOU WIN", fill = "red", font = T_FONT)
    cvs.create_text(301, 300, text = "YOU WIN", fill = "black", font = T_FONT)
    cvs.create_text(300, 550, text = "Press 'Up' to go back to the title", font = S_FONT)
    
root = tkinter.Tk()
root.title("INVADER GAME")

cvs = tkinter.Canvas(width = 600, height = 680)
cvs.pack()

#whatever key is pressed, key_p function is called
root.bind("<Key>", key_p)

#allow not to change the window size
root.resizable(False, False)

IMAGES = [
    tkinter.PhotoImage(file = "images/invader_1.png"), tkinter.PhotoImage(file = "images/invader_2.png"),
    tkinter.PhotoImage(file = "images/BACKGROUND.png"), tkinter.PhotoImage(file = "images/GAME_CLEAR.png"),
    tkinter.PhotoImage(file = "images/GAME_OVER.png")
    ]

#call main function
main()

root.mainloop()
