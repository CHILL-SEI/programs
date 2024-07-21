#tkinter moduleをtkとしてimport
import tkinter as tk
import random

#初期値
scene = "title"
k = ""
door = [1, 0, 0]
GetC = 0
Att = 0

#押されたキーと対応する関数を呼び出す関数gkey
def gkey(e):
    global k, scene
    k = e.keysym
    if k == "space" and scene == "title":
        scene = "game"
        k = ""
        main()
    elif k == "Return" and scene == "result":
        scene = "title"
        main()
    elif k == "r" and (scene == "game" or scene == "select" or scene == "show"):
        scene = "result"
        main()
    elif (k == "1" or k == "2" or k == "3") and scene == "game":
        select()
    elif k == "c" or k == "k":
        show()

#一番メインの処理を行う関数main
def main():
    global GetC, Att, d_shuffled, scene
    if Att > 0 and k != "r" and k != "Return":
        scene = "game"
    if scene == "title":
        GetC = 0
        Att = 0
        cvs.delete("all")
        cvs["bg"] = "black"
        cvs.create_text(500, 300, text = "Monty Hall", fill = "white", font = ("Times New Roman", 70))
        cvs.create_text(500, 500, text = "Press Space to Start", fill = "white", font = ("System", 25))

    elif scene == "game":
        cvs.delete("all")
        cvs["bg"] = "white"
        cvs.create_text(150, 50, text = "Select One Door", font = ("System", 30))
        cvs.create_text(850, 50, text = "success : {}".format(GetC), font = ("System", 30))
        cvs.create_text(500, 675, text = "Push R to end", font = ("System", 30))
        d_shuffled = random.sample(door, len(door))
        for i in range(3):
            if d_shuffled[i] == 1:
                cvs.create_image(i * 275 + 225, 450, image = img[1])
            else:
                cvs.create_image(i * 275 + 225, 450, image = img[2])
            cvs.create_text(i * 275 + 225, 600, text = "{}".format(i + 1), font = ("Times New Roman", 30))
            cvs.create_image(i * 275 + 225, 400, image = img[0], tag = "DOOR{}".format(i))

    elif scene == "result":
        cvs.delete("all")
        cvs["bg"] = "pink"
        try:
            cvs.create_text(500, 350, text = "SUCCESS / ATTEMPT : {:.2f}".format(GetC / Att), font = ("System", 50))
            cvs.create_text(500, 450, text = "Press Enter", font = ("System", 35))
        except ZeroDivisionError:
            cvs.create_text(500, 350, text = "You need to try 1 time at least.", font = ("System", 50))
            cvs.create_text(500, 450, text = "Press Enter", font = ("System", 35))

#扉を変更するか否かを選ばせる関数select
def select():
    global Pk, scene
    scene = "select"
    Pk = ""
    while True:
        rSH = random.randint(0,2)
        if (d_shuffled[rSH] == 0) and int(k) - 1 != rSH:
            break
    cvs.delete("DOOR{}".format(rSH))
    cvs.create_text(500, 150, text = "You selected {}. Will you change the door?".format(int(k)), fill = "red", font = ("System", 30), tag = "QUE")
    cvs.create_text(500, 200, text = "CHANGE -> [c], KEEP -> [k]", fill = "red", font = ("System", 20), tag = "DEC")
    Pk = k

#結果をプレイヤーに見せる関数show
def show():
    global GetC, Att, scene
    scene = "show"
    cvs.delete("QUE")
    cvs.delete("DEC")
    for i in range(3):
        cvs.delete("DOOR{}".format(i))
    if d_shuffled[int(Pk) - 1] == 1 and k == "c":
        cvs.create_text(500, 150, text = "You failed:(", fill = "blue", font = ("System", 40))
    elif d_shuffled[int(Pk) - 1] == 1 and k == "k":
        cvs.create_text(500, 150, text = "You got the car:)", fill = "red", font = ("System", 40))
        GetC += 1
    elif d_shuffled[int(Pk) - 1] == 0 and k == "c":
        cvs.create_text(500, 150, text = "You got the car:)", fill = "red", font = ("System", 40))
        GetC += 1
    elif d_shuffled[int(Pk) - 1] == 0 and k == "k":
        cvs.create_text(500, 150, text = "You failed:(", fill = "blue", font = ("System", 40))
    Att += 1
    root.after(3000, main)

root = tk.Tk()
root.title("MontyHall")
cvs = tk.Canvas(width = 1000, height = 700, bg = "black")
cvs.pack()
root.bind("<Key>", gkey)
img = [tk.PhotoImage(file = "images/Door.png"), tk.PhotoImage(file = "images/Car.png"), tk.PhotoImage(file = "images/Sheep.png")]
main()
root.mainloop()
