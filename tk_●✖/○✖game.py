#2024/09/09
import tkinter
import random

base = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
scene = "title"
turn = random.randint(0, 1)
k = ""

def key_p(e):
    global scene
    k = e.keysym
    if scene == "title" and k == "space":
        scene = "game"
        main()
        k = ""

def main():
    if scene == "title":
        cvs.delete("all")
        cvs["bg"] = "black"
        cvs.create_text(375, 300, text = "○✖GAME", font = ("System", 50), fill = "white")
        cvs.create_text(375, 450, text = "Press 'Space' to start", font = ("System", 25), fill = "white")
    if scene == "game":
        cvs.delete("all")
        cvs["bg"] = "white"
        cvs.create_text(75, 100, text = "TURN", font = ("Times New Roman", 30))
        cvs.create_rectangle(0, 0, 750, 600, width = 5)
        for a in range(150, 751, 200):
            cvs.create_line(a, 0, a, 600, width = 5)
        for b in range(200, 401, 200):
            cvs.create_line(150, b, 750, b, width = 5)
        root.after(100, turn_w)
        if turn == 1:
            root.after(1000, enemy)
        

def turn_w():
    cvs.delete("TURN")
    if turn == 0:
        cvs.create_text(75, 150, text = "you", font = ("Times New Roman", 25), tag = "TURN")
    else:
        cvs.create_text(75, 150, text = "cpu", font = ("Times New Roman", 25), tag = "TURN")

def player_c(m):
    global m_x, m_y, base
    m_x, m_y = m.x, m.y
    if 0<m.y and m.y<200 and turn == 0 and scene == "game":
        if 150<m.x and m.x<350 and base[0][0] == 0:
            cvs.create_image(250, 100, image = IMAGE[0])
            base[0][0] = 1
        if 350<m.x and m.x<550 and base[0][1] == 0:
            cvs.create_image(450, 100, image = IMAGE[0])
            base[0][1] = 1
        if 550<m.x and m.x<750 and base[0][2] == 0:
            cvs.create_image(650, 100, image = IMAGE[0])
            base[0][2] = 1
        root.after(50, judge)
    if 200<m.y and m.y<400 and turn == 0 and scene == "game":
        if 150<m.x and m.x<350 and base[1][0] == 0:
            cvs.create_image(250, 300, image = IMAGE[0])
            base[1][0] = 1
        if 350<m.x and m.x<550 and base[1][1] == 0:
            cvs.create_image(450, 300, image = IMAGE[0])
            base[1][1] = 1
        if 550<m.x and m.x<750 and base[1][2] == 0:
            cvs.create_image(650, 300, image = IMAGE[0])
            base[1][2] = 1
        root.after(50, judge)
    if 400<m.y and m.y<600 and turn == 0 and scene == "game":
        if 150<m.x and m.x<350 and base[2][0] == 0:
            cvs.create_image(250, 500, image = IMAGE[0])
            base[2][0] = 1
        if 350<m.x and m.x<550 and base[2][1] == 0:
            cvs.create_image(450, 500, image = IMAGE[0])
            base[2][1] = 1
        if 550<m.x and m.x<750 and base[2][2] == 0:
            cvs.create_image(650, 500, image = IMAGE[0])
            base[2][2] = 1
        root.after(50, judge)

def enemy():
    global base
    if scene == "game" and turn == 1:
        while True:
            b_x = random.randint(0, 2)
            b_y = random.randint(0, 2)
            if base[b_x][b_y] == 0:
                base[b_x][b_y] = 2
                break
        for c in range(0, 3):
            for d in range(0, 3):
                if b_x == c and b_y == d:
                    cvs.create_image(200*d+250, 200*c+100, image = IMAGE[1])
        root.after(50, judge)

def judge():
    global turn, scene
    for i in range(0, 2):
        if sum(base[i]) == 3 and set(base[i]) == {1}:
            cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
            scene = "result"
        if sum(base[i]) == 6 and set(base[i]) == {2}:
            cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
            scene = "result"
    if base[0][0] == 1 and base[1][0] == 1 and base[2][0] == 1:
        cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
        scene = "result"
    if base[0][1] == 1 and base[1][1] == 1 and base[2][1] == 1:
        cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
        scene = "result"
    if base[0][2]  == 1 and base[1][2] == 1 and base[2][2] == 1:
        cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
        scene = "result"
    if base[0][0] == 2 and base[1][0] == 2 and base[2][0] == 2:
        cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
        scene = "result"
    if base[0][1] == 2 and base[1][1] == 2 and base[2][1] == 2:
        cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
        scene = "result"
    if base[0][2] == 2 and base[1][2] == 2 and base[2][2] == 2:
        cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
        scene = "result"
    if base[0][0] == 1 and base[1][1] == 1 and base[2][2] == 1:
        cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
        scene = "result"
    if base[0][0] == 2 and base[1][1] == 2 and base[2][2] == 2:
        cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
        scene = "result"
    if base[0][2] == 1 and base[1][1] == 1 and base[2][0] == 1:
        cvs.create_text(375, 300, text = "YOU WIN", fill = "blue", font = ("System", 75))
        scene = "result"
    if base[0][2] == 2 and base[1][1] == 2 and base[2][0] == 2:
        cvs.create_text(375, 300, text = "YOU LOSE", fill = "red", font = ("System", 75))
        scene = "result"
    elif turn == 1:
        turn = 0
        root.after(100, turn_w)
    elif turn == 0:
        turn = 1
        root.after(100, turn_w)
        root.after(1000, enemy)
        
root = tkinter.Tk()
root.title("○✖ game")
cvs = tkinter.Canvas(width = 750, height = 600)
cvs.pack()
root.bind("<Button>", player_c)
root.bind("<Key>", key_p)
IMAGE = [tkinter.PhotoImage(file = "images/CIRCLE.png"), tkinter.PhotoImage(file = "images/CROSS.png")]
main()
root.mainloop()
