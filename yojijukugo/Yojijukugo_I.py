#2024/07/02 Yojijukugo game (Intermediate)
import time
import random

print("""四字熟語が表示されるので、読みを'ひらがな'で入力してください。
中級の問題数は30です。
""")
time.sleep(2)

Yoj = []
Alr_Q = []
n = 0
Life = 2
Correct = 0

with open("Program_Y/Yojijukugo_I_csv.txt", "r", newline = "\n") as f:
    for line in f:
        Jukugo, Yomi, Meaning = line.split(",")
        Yoj.append([Jukugo, Yomi, Meaning])

while n < 5:
    if Life == 0:
        print("ライフが0になりました:/")
        break
    AnsC = 3
    print("問題 : ", end = "")
    while True:
        global Que
        Que = random.randint(0, 29)
        if Yoj[Que][0] in Alr_Q:
            continue
        else:
            Alr_Q.append(Yoj[Que][0])
            break
    print(Yoj[Que][0])
    while AnsC > 0:
        print(f"あと{AnsC}回だけ回答できます")
        Ans = input("入力 : ")
        if Ans == Yoj[Que][1]:
            print("正解です:D")
            time.sleep(1)
            print(Yoj[Que][0] + ":" + Yoj[Que][1])
            print("意味:" + Yoj[Que][2])
            Correct += 1
            break
        else:
            print("答えが違います:(")
            AnsC -= 1
    else:
        print("失敗です:/")
        time.sleep(1)
        print(Yoj[Que][0] + ":" + Yoj[Que][1])
        print("意味:" + Yoj[Que][2])
        Life -= 1
        print(f"残りライフは{Life}です")
    n += 1
    time.sleep(3)

time.sleep(1)
print(f"正解数は{Correct}でした。また挑戦してみてみましょう！")
