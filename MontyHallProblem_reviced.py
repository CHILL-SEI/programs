#2024/07/19 MontyHallProblem
import random
import sys
print("""モンティホール問題を検証します。
ドアを変えた時、そのドアに車が隠されている確率を表示します。
コンピューターに検証させる場合は1を、自分で検証する場合は2を入力してください
""")
mode = int(input("->"))

Door = [1, 0, 0]
n = 0
c = 0
e = 1

if mode == 1:
    while n < 1000:
        d_shuffled = random.sample(Door, len(Door))
        R = random.randint(0, 2)
        if d_shuffled[R] == 1:
            n += 1
            continue
        else:
            c += 1
            n += 1
    print(f"ドアを変えた時に車である確率は{c/ 1000}です")

else:
    print("検証を終わる際は3を入力してください")
    while e != 3:
        d_shuffled = random.sample(Door, len(Door))
        e = int(input("0, 1, 2のドアのうち、好きな番号を入力してください。\n->"))
        if e == 3:
            print(f"""検証を終了します。
ドアを変えた時に車である確率は{c / n}でした""")
            sys.exit()
        else:
            if d_shuffled[e] == 1:
                print("はずれです:(")
            else:
                print("車でした:)")
                c += 1
        n += 1
