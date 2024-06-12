#2024/06/11 "●,✖game"
import random
import time
import sys

print("●✖ゲームを開始します")
print("行（横）、列（縦）をそれぞれ1から4の整数で入力し、取りたいマスを指定してください")
time.sleep(5)
print("それではゲームを開始します")

#カウントダウン
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

#盤面
line_1 = ["ー", "ー", "ー", "ー"]
line_2 = ["ー", "ー", "ー", "ー"]
line_3 = ["ー", "ー", "ー", "ー"]
line_4 = ["ー", "ー", "ー", "ー"]

def print_line():
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)

#ランダムでターンを決定
turn = random.randint(0,1)

#盤面を表示したのち、コンピューターが勝ったか否かを判定する、を繰り返す
while True:
    print("-" * 40)
    print_line()
    print("-" * 40)
    if set(line_1) == set(line_2) == set(line_3) == set(line_4) == {"●", "✖"}:
        print("引き分けです :)")
        sys.exit()
    elif set(line_1) == {"✖"}:
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif set(line_2) == {"✖"}:
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif set(line_3) == {"✖"}:
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif set(line_4) == {"✖"}:
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif line_1[0] == line_2[0] == line_3[0] == line_4[0] == "✖":
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif line_1[1] == line_2[1] == line_3[1] == line_4[1] == "✖":
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif line_1[2] == line_2[2] == line_3[2] == line_4[2] == "✖":
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif line_1[3] == line_2[3] == line_3[3] == line_4[3] == "✖":
        print("コンピューターの 勝ちです :/")
        sys.exit()
    elif line_1[0] == line_2[1] == line_3[2] == line_4[3] == "✖":
        print("コンピューターの勝ちです :/")
        sys.exit()
    elif line_1[3] == line_2[2] == line_3[1] == line_4[0] == "✖":
        print("コンピューターの勝ちです :/")
        sys.exit()
#turnが1なら自分のターン
    elif turn == 1:
        print("あなたのターンです")
#hor(horizon)：横、ver(vertical)：縦
        while True:
            hor = int(input("行を入力してください"))
            if hor < 0 or hor > 4:
                print("行、列ともに1から4の整数値にのみ対応しています")
                continue
            ver = int(input("列を入力してください"))
            if ver < 0 or ver > 4:
                print("行、列ともに1から4の整数値にのみ対応しています")
                continue
            if hor == 1 and (line_1[ver - 1] == "●" or line_1[ver - 1] == "✖"):
                print("指定したマスはすでに入力されています")
                continue
            if hor == 2 and (line_2[ver - 1] == "●" or line_2[ver - 1] == "✖"):
                print("指定したマスはすでに入力されています")
                continue
            if hor == 3 and (line_3[ver - 1] == "●" or line_3[ver - 1] == "✖"):
                print("指定したマスはすでに入力されています")
                continue
            if hor == 4 and (line_4[ver - 1] == "●" or line_4[ver - 1] == "✖"):
                print("指定したマスはすでに入力されています")
                continue
            if hor == 1:
                line_1[ver - 1] = "●"
                break
            if hor == 2:
                line_2[ver - 1] = "●"
                break
            if hor == 3:
                line_3[ver - 1] = "●"
                break
            if hor == 4:
                line_4[ver - 1] = "●"
                break
#プレイヤーの入力が終わったのちに、プレイヤーが勝利したか判定する
        while True:
                if set(line_1) == {"●"}:
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if set(line_2) == {"●"}:
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if set(line_3) == {"●"}:
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if set(line_4) == {"●"}:
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[0] == line_2[0] == line_3[0] == line_4[0] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[1] == line_2[1] == line_3[1] == line_4[1] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[2] == line_2[2] == line_3[2] == line_4[2] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[3] == line_2[3] == line_3[3] == line_4[3] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[0] == line_2[1] == line_3[2] == line_4[3] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                if line_1[3] == line_2[2] == line_3[1] == line_4[0] == "●":
                    print("-" * 40)
                    print_line()
                    print("-" * 40)
                    print("あなたの勝ちです :D")
                    sys.exit()
                else:
                    break
#turnが0ならコンピューターのターン
    else:
        print("コンピューターのターンです")
        time.sleep(1)
#line_1～line_4の要素が全て"ー"の時は、完全にランダムで"✖"を配置する
        if set(line_1) == set(line_2) == set(line_3) == set(line_4) == {"ー"}:
            hor = random.randint(1, 4)
            ver = random.randint(0, 3)
            if hor == 1:
                line_1[ver] = "✖"
            elif hor == 2:
                line_2[ver] = "✖"
            elif hor == 3:
                line_3[ver] = "✖"
            elif hor == 4:
                line_4[ver] = "✖"
        else:
#プレイヤーの勝利を防ぐ、コンピューターが勝つために必要な変数およびリスト
            cir_h1 = line_1.count("●")
            cir_h2 = line_2.count("●")
            cir_h3 = line_3.count("●")
            cir_h4 = line_4.count("●")
            cro_h1 = line_1.count("✖")
            cro_h2 = line_2.count("✖")
            cro_h3 = line_3.count("✖")
            cro_h4 = line_4.count("✖")
            v1_list = [line_1[0], line_2[0], line_3[0], line_4[0]]
            v2_list = [line_1[1], line_2[1], line_3[1], line_4[1]]
            v3_list = [line_1[2], line_2[2], line_3[2], line_4[2]]
            v4_list = [line_1[3], line_2[3], line_3[3], line_4[3]]
            cir_v1 = v1_list.count("●")
            cir_v2 = v2_list.count("●")
            cir_v3 = v3_list.count("●")
            cir_v4 = v4_list.count("●")
            cro_v1 = v1_list.count("✖")
            cro_v2 = v2_list.count("✖")
            cro_v3 = v3_list.count("✖")
            cro_v4 = v4_list.count("✖")
            cir_count_h = [cir_h1, cir_h2, cir_h3, cir_h4]
            cir_count_v = [cir_v1, cir_v2, cir_v3, cir_v4]
            cro_count_h = [cro_h1, cro_h2, cro_h3, cro_h4]
            cro_count_v = [cro_v1, cro_v2, cro_v3, cro_v4]
            d1_list = [line_1[0], line_2[1], line_3[2], line_4[3]]
            d2_list = [line_1[3], line_2[2], line_3[1], line_4[0]]
            cro_d1 = d1_list.count("✖")
            cro_d2 = d2_list.count("✖")
            cir_top_h = max(cir_count_h)
            cir_top_v = max(cir_count_v)
            cro_top_h = max(cro_count_h)
            cro_top_v = max(cro_count_v)
            time.sleep(1)
#横に"✖"が３つあるとき、コンピューターが勝つための動作部
            if cro_top_h == 3 and cro_h1 == 3 and set(line_1) == {"✖", "ー"}:
                Y = line_1.index("ー")
                line_1[Y] = "✖"
            elif cro_top_h == 3 and cro_h2 == 3 and set(line_2) == {"✖", "ー"}:
                Z = line_2.index("ー")
                line_2[Z] = "✖"
            elif cro_top_h == 3 and cro_h3 == 3 and set(line_3) == {"✖", "ー"}:
                a = line_3.index("ー")
                line_[a] = "✖"
            elif cro_top_h == 3 and cro_h4 == 3 and set(line_4) == {"✖", "ー"}:
                b = line_4.index("ー")
                line_4[b] = "✖"
#縦に"✖"が３つあるとき、コンピューターが勝つための動作部
            elif cro_top_v == 3 and cro_v1 == 3 and set(v1_list) == {"✖", "ー"}:
                c = v1_list.index("ー")
                if c == 0:
                    line_1[0] = "✖"
                elif c == 1:
                    line_2[0] = "✖"
                elif c == 2:
                    line_3[0] = "✖"
                elif c == 3:
                    line_4[0] = "✖"
            elif cro_top_v == 3 and cro_v2 == 3 and set(v2_list) == {"✖", "ー"}:
                d = v2_list.index("ー")
                if d ==0:
                    line_1[1] = "✖"
                elif d == 1:
                    line_2[1] = "✖"
                elif d == 2:
                    line_3[1] = "✖"
                elif d == 3:
                    line_4[1] = "✖"
            elif cro_top_v == 3 and cro_v3 == 3 and set(v3_list) == {"✖", "ー"}:
                e = v3_list.index("ー")
                if e ==0:
                    line_1[2] = "✖"
                elif e == 1:
                    line_2[2] = "✖"
                elif e == 2:
                    line_3[2] = "✖"
                elif e == 3:
                    line_4[2] = "✖"
            elif cro_top_v == 3 and cro_v4 == 3 and set(v4_list) == {"✖", "ー"}:
                f = v4_list.index("ー")
                if f ==0:
                    line_1[3] = "✖"
                elif f == 1:
                    line_2[3] = "✖"
                elif f == 2:
                    line_3[3] = "✖"
                elif f == 3:
                    line_4[3] = "✖"
#斜めに"✖"が３つあるとき、コンピューターが勝つための動作部
            elif cro_d1 == 3 and set(d1_list) == {"✖", "ー"}:
                g = d1_list.index("ー")
                if g == 0:
                    line_1[0] = "✖"
                elif g == 1:
                    line_2[1] = "✖"
                elif g == 2:
                    line_3[2] = "✖"
                elif g == 3:
                    line_4[3] = "✖"
            elif cro_d2 == 3 and set(d2_list) == {"✖", "ー"}:
                h = d2_list.index("ー")
                if h == 0:
                    line_1[3] = "✖"
                elif h == 1:
                    line_2[2] = "✖"
                elif h == 2:
                    line_3[1] = "✖"
                elif h == 3:
                    line_4[0] = "✖"
#横に"●"が３つあるとき、コンピューターがプレイヤーの勝ちを阻止するための動作部
            elif cir_top_h == 3 and cir_h1 == 3 and set(line_1) == {"●", "ー"}:
                A = line_1.index("ー")
                line_1[A] = "✖"
            elif cir_top_h == 3 and cir_h2 == 3 and set(line_2) == {"●", "ー"}:
                B = line_2.index("ー")
                line_2[B] = "✖"
            elif cir_top_h == 3 and cir_h3 == 3 and set(line_3) == {"●", "ー"}:
                C = line_3.index("ー")
                line_3[C] = "✖"
            elif cir_top_h == 3 and cir_h4 == 3 and set(line_4) == {"●", "ー"}:
                D = line_4.index("ー")
                line_4[D] = "✖"
#縦に"●"が３つあるとき、コンピューターがプレイヤーの勝ちを阻止するための動作部
            elif cir_top_v == 3 and cir_v1 == 3 and set(v1_list) == {"●", "ー"}:
                E = v1_list.index("ー")
                if E == 0:
                    line_1[0] = "✖"
                elif E == 1:
                    line_2[0] = "✖"
                elif E == 2:
                    line_3[0] = "✖"
                elif E == 3:
                    line_4[0] = "✖"
            elif cir_top_v == 3 and cir_v2 == 3 and set(v2_list) == {"●", "ー"}:
                F = v2_list.index("ー")
                if F == 0:
                    line_1[1] = "✖"
                elif F == 1:
                    line_2[1] = "✖"
                elif F == 2:
                    line_3[1] = "✖"
                elif F == 3:
                    line_4[1] = "✖"
            elif cir_top_v == 3 and cir_v3 == 3 and set(v3_list) == {"●", "ー"}:
                G = v3_list.index("ー")
                if G == 0:
                    line_1[2] = "✖"
                elif G == 1:
                    line_2[2] = "✖"
                elif G == 2:
                    line_3[2] = "✖"
                elif G == 3:
                    line_4[2] = "✖"
            elif cir_top_v == 3 and cir_v4 == 3 and set(v4_list) == {"●", "ー"}:
                H = v4_list.index("ー")
                if H == 0:
                    line_1[3] = "✖"
                elif H == 1:
                    line_4[3] = "✖"
                elif H == 2:
                    line_3[3] = "✖"
                elif H == 3:
                    line_4[4] = "✖"
#これより下にある条件に当てはまらない場合の動作部
            elif cir_top_h == 3 and set(line_1) == {"●", "✖"}:
                while True:
                    ran = random.randint(2, 4)
                    if ran == 2 and set(line_2) != {"●", "✖"}:
                        M = line_2.index("ー")
                        line_2[M] = "✖"
                        break
                    elif ran == 3 and set(line_3) != {"●", "✖"}:
                        N = line_3.index("ー")
                        line_3[N] = "✖"
                        break
                    elif ran == 4 and set(line_4) != {"●", "✖"}:
                        O = line_4.index("ー")
                        line_4[O] = "✖"
                        break
            elif cir_top_h == 3 and set(line_2) == {"●", "✖"}:
                while True:
                    ran = random.randint(2, 4)
                    if ran == 2 and set(line_1) != {"●", "✖"}:
                        P = line_1.index("ー")
                        line_1[P] = "✖"
                        break
                    elif ran == 3 and set(line_3) != {"●", "✖"}:
                        Q = line_3.index("ー")
                        line_3[Q] = "✖"
                        break
                    elif ran == 4 and set(line_4) != {"●", "✖"}:
                        R = line_4.index("ー")
                        line_4[R] = "✖"
                        break
            elif cir_top_h == 3 and set(line_3) == {"●", "✖"}:
                while True:
                    ran = random.randint(2, 4)
                    if ran == 2 and set(line_1) != {"●", "✖"}:
                        S = line_1.index("ー")
                        line_1[S] = "✖"
                        break
                    elif ran == 3 and set(line_2) != {"●", "✖"}:
                        T = line_2.index("ー")
                        line_2[T] = "✖"
                        break
                    elif ran == 4 and set(line_4) != {"●", "✖"}:
                        U = line_4.index("ー")
                        line_4[U] = "✖"
                        break
            elif cir_top_h == 3 and set(line_4) == {"●", "✖"}:
                while True:
                    ran = random.randint(2, 4)
                    if ran == 2 and set(line_1) != {"●", "✖"}:
                        V = line_1.index("ー")
                        line_1[V] = "✖"
                        break
                    elif ran == 3 and set(line_2) != {"●", "✖"}:
                        W = line_2.index("ー")
                        line_2[W] = "✖"
                        break
                    elif ran == 4 and set(line_3) != {"●", "✖"}:
                        X = line_3.index("ー")
                        line_3[X] = "✖"
                        break
#プレイヤーの勝利をできる限り防ぐため、"●"が多い行に近い部分に"✖"を置くための動作部
            elif cir_top_h == cir_h1 and set(line_1) != {"●", "✖"}:
                while True:
                    hor = random.randint(1, 2)
                    ver = random.randint(0, 3)
                    if hor == 1 and (line_1[ver] == "●" or line_1[ver] == "✖"):
                        continue
                    if hor == 2 and (line_2[ver] == "●" or line_2[ver] == "✖"):
                        continue
                    if hor == 1:
                        line_1[ver] = "✖"
                        break
                    if hor == 2:
                        line_2[ver] = "✖"
                        break
            elif cir_top_h == cir_h2 and set(line_2) != {"●", "✖"}:
                while True:
                    hor = random.randint(1, 3)
                    ver = random.randint(0, 3)
                    if hor == 1 and (line_1[ver] == "●" or line_1[ver] == "✖"):
                        continue
                    if hor == 2 and (line_2[ver] == "●" or line_2[ver] == "✖"):
                        continue
                    if hor == 3 and (line_3[ver] == "●" or line_3[ver] == "✖"):
                        continue
                    if hor == 1:
                        line_1[ver] = "✖"
                        break
                    if hor == 2:
                        line_2[ver] = "✖"
                        break
                    if hor == 3:
                        line_3[ver] = "✖"
                        break
            elif cir_top_h == cir_h3 and set(line_3) != {"●", "✖"}:
                while True:
                    hor = random.randint(2, 4)
                    ver = random.randint(0, 3)
                    if hor == 2 and (line_2[ver] == "●" or line_2[ver] == "✖"):
                        continue
                    if hor == 3 and (line_3[ver] == "●" or line_3[ver] == "✖"):
                        continue
                    if hor == 4 and (line_4[ver] == "●" or line_4[ver] == "✖"):
                        continue
                    if hor == 2:
                        line_2[ver] = "✖"
                        break
                    if hor == 3:
                        line_3[ver] = "✖"
                        break
                    if hor == 4:
                        line_4[ver] = "✖"
                        break
            elif cir_top_h == cir_h4 and set(line_4) != {"●", "✖"}:
                while True:
                    hor = random.randint(3, 4)
                    ver = random.randint(0, 3)
                    if hor == 3 and (line_3[ver] == "●" or line_3[ver] == "✖"):
                        continue
                    if hor == 4 and (line_4[ver] == "●" or line_4[ver] == "✖"):
                        continue
                    if hor == 3:
                        line_3[ver] = "✖"
                        break
                    if hor == 4:
                        line_4[ver] = "✖"
                        break

#turnを切り替える
    time.sleep(1)
    turn = 1 - turn
