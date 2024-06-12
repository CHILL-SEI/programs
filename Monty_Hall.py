#2024/06/12 MontyHallProblem
import random
print("モンティホール問題を検証します")
print("ドアを変えたとき、そのドアに車が隠されている確率を表示します")
print("コンピューターに検証させる場合は１を、自分で検証する場合は２を入力してください")
mode = int(input())

door = ["sheep", "sheep", "car"]
n = 0
get_c = 0

#500回検証させる
#毎回doorリストをシャッフルし、コンピューターにd_shuffledのindexを選ばせる
#show_shで残りの羊のindexを割り出す
#残りのドアに車があった場合、get_cに１を足していく
if mode == 1:
    while n < 500:
        d_shuffled = random.sample(door, len(door))
        d_num = random.randint(0, 2)
        if d_num == 0:
            show_sh = [d_shuffled[1], d_shuffled[2]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                get_c += 1
        elif d_num == 1:
            show_sh = [d_shuffled[0], d_shuffled[2]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                get_c += 1
        else:
            show_sh = [d_shuffled[0], d_shuffled[1]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                get_c += 1
        n += 1

#0を入力するとbreakで検証終了
elif mode == 2:
    print("ドアを１から３の整数で選び、入力してください")
    print("ドアの番号として０を入力すると検証を終了します")
    while True:
        d_shuffled = random.sample(door, len(door))
        d_num = int(input("ドアを選んでください"))
        if d_num == 0:
            print("検証を終了します")
            break
        if d_num == 1:
            show_sh = [d_shuffled[1], d_shuffled[2]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                print("車を入手しました :)")
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                print("車を入手しました :)")
                get_c += 1
            else:
                print("羊でした :/")
        elif d_num == 2:
            show_sh = [d_shuffled[0], d_shuffled[2]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                print("車を入手しました :)")
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                print("車を入手しました :)")
                get_c += 1
            else:
                print("羊でした :/")
        else:
            show_sh = [d_shuffled[0], d_shuffled[1]]
            sh = show_sh.index("sheep")
            if sh == 0 and show_sh[1] == "car":
                print("車を入手しました :)")
                get_c += 1
            elif sh == 1 and show_sh[0] == "car":
                print("車を入手しました :)")
                get_c += 1
            else:
                print("羊でした :/")
        n += 1

#結果表示部分
#ZeroDivisionErrorをexceptで回避
if mode == 1:
    print(f"選ぶドアを変え、そのドアに車が隠されている確率はおよそ{get_c / 500}です")
else:
    try:
        print(f"選ぶドアを変え、そのドアに車が隠されている確率はおよそ{get_c / n}です")
    except ZeroDivisionError:
        print("試行回数０で確率は定義されません :I")
