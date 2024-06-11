import random
import time
import sys

print("●✖ゲームを開始します")
print("行（横）、列（縦）をそれぞれ1から4の整数で入力し、取りたいマスを指定してください")
time.sleep(5)
print("それではゲームを開始します")

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

line_1 = ["ー", "ー", "ー", "ー"]
line_2 = ["ー", "ー", "ー", "ー"]
line_3 = ["ー", "ー", "ー", "ー"]
line_4 = ["ー", "ー", "ー", "ー"]

def print_line():
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)

turn = random.randint(0,1)

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
    elif turn == 1:
        print("あなたのターンです")
        while True:
            hor = int(input("行を入力してください"))
            ver = int(input("列を入力してください"))
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
                line_1.insert(ver - 1, "●")
                del line_1[ver]
                break
            if hor == 2:
                line_2.insert(ver - 1, "●")
                del line_2[ver]
                break
            if hor == 3:
                line_3.insert(ver - 1, "●")
                del line_3[ver]
                break
            if hor == 4:
                line_4.insert(ver - 1, "●")
                del line_4[ver]
                break
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
    else:
        print("コンピューターのターンです")
        time.sleep(1)
        if set(line_1) == set(line_2) == set(line_3) == set(line_4) == {"ー"}:
            hor = random.randint(1, 4)
            ver = random.randint(1, 4)
            if hor == 1:
                line_1.insert(ver - 1, "✖")
                del line_1[ver]
            elif hor == 2:
                line_2.insert(ver - 1, "✖")
                del line_2[ver]
            elif hor == 3:
                line_3.insert(ver - 1, "✖")
                del line_3[ver]
            elif hor == 4:
                line_4.insert(ver - 1, "✖")
                del line_4[ver]
        else:
            time.sleep(1)
            cir_h1 = line_1.count("●")
            cir_h2 = line_2.count("●")
            cir_h3 = line_3.count("●")
            cir_h4 = line_4.count("●")
            cir_v1_list = [line_1[0], line_2[0], line_3[0], line_4[0]]
            cir_v2_list = [line_1[1], line_2[1], line_3[1], line_4[1]]
            cir_v3_list = [line_1[2], line_2[2], line_3[2], line_4[2]]
            cir_v4_list = [line_1[3], line_2[3], line_3[3], line_4[3]]
            cir_v1 = cir_v1_list.count("●")
            cir_v2 = cir_v2_list.count("●")
            cir_v3 = cir_v3_list.count("●")
            cir_v4 = cir_v4_list.count("●")
            cir_count_h = [cir_h1, cir_h2, cir_h3, cir_h4]
            cir_count_v = [cir_v1, cir_v2, cir_v3, cir_v4]
            cir_top_h = max(cir_count_h)
            cir_top_v = max(cir_count_v)
            if cir_top_h == 3 and cir_h1 == 3 and set(line_1) == {"●", "ー"}:
                A = line_1.index("ー")
                line_1.insert(A, "✖")
                del line_1[A + 1]
            elif cir_top_h == 3 and cir_h2 == 3 and set(line_2) == {"●", "ー"}:
                B = line_2.index("ー")
                line_2.insert(B, "✖")
                del line_2[B + 1]
            elif cir_top_h == 3 and cir_h3 == 3 and set(line_3) == {"●", "ー"}:
                C = line_3.index("ー")
                line_3.insert(C, "✖")
                del line_3[C + 1]
            elif cir_top_h == 3 and cir_h4 == 3 and set(line_4) == {"●", "ー"}:
                D = line_4.index("ー")
                line_4.insert(D, "✖")
                del line_4[D + 1]
            elif cir_top_v == 3 and cir_v1 == 3 and set(cir_v1_list) == {"●", "ー"}:
                E = cir_v1_list.index("ー")
                if E == 0:
                    line_1.insert(0, "✖")
                    del line_1[1]
                elif E == 1:
                    line_2.insert(0, "✖")
                    del line_2[1]
                elif E == 2:
                    line_3.insert(0, "✖")
                    del line_3[1]
                elif E == 3:
                    line_4.insert(0, "✖")
                    del line_4[1]
            elif cir_top_v == 3 and cir_v2 == 3 and set(cir_v2_list) == {"●", "ー"}:
                F = cir_v2_list.index("ー")
                if F == 0:
                    line_1.insert(1, "✖")
                    del line_1[2]
                elif F == 1:
                    line_2.insert(1, "✖")
                    del line_2[2]
                elif F == 2:
                    line_3.insert(1, "✖")
                    del line_3[2]
                elif F == 3:
                    line_4.insert(1, "✖")
                    del line_4[2]
            elif cir_top_v == 3 and cir_v3 == 3 and set(cir_v3_list) == {"●", "ー"}:
                G = cir_v3_list.index("ー")
                if G == 0:
                    line_1.insert(2, "✖")
                    del line_1[3]
                elif G == 1:
                    line_2.insert(2, "✖")
                    del line_2[3]
                elif G == 2:
                    line_3.insert(2, "✖")
                    del line_3[3]
                elif G == 3:
                    line_4.insert(2, "✖")
                    del line_4[3]
            elif cir_top_v == 3 and cir_v4 == 3 and set(cir_v4_list) == {"●", "ー"}:
                H = cir_v4_list.index("ー")
                if H == 0:
                    line_1.insert(3, "✖")
                    del line_1[4]
                elif H == 1:
                    line_4.insert(3, "✖")
                    del line_2[4]
                elif H == 2:
                    line_3.insert(3, "✖")
                    del line_3[4]
                elif H == 3:
                    line_4.insert(3, "✖")
                    del line_4[4]
            elif cir_top_h == cir_h1 and set(line_1) != {"●", "✖"}:
                while True:
                    hor = random.randint(1, 2)
                    ver = random.randint(1, 4)
                    if hor == 1 and (line_1[ver - 1] == "●" or line_1[ver - 1] == "✖"):
                        continue
                    if hor == 2 and (line_2[ver - 1] == "●" or line_2[ver - 1] == "✖"):
                        continue
                    if hor == 1:
                        line_1.insert(ver - 1, "✖")
                        del line_1[ver]
                        break
                    if hor == 2:
                        line_2.insert(ver - 1, "✖")
                        del line_2[ver]
                        break
            elif cir_top_h == cir_h2 and set(line_2) != {"●", "✖"}:
                while True:
                    hor = random.randint(1, 3)
                    ver = random.randint(1, 4)
                    if hor == 1 and (line_1[ver - 1] == "●" or line_1[ver - 1] == "✖"):
                        continue
                    if hor == 2 and (line_2[ver - 1] == "●" or line_2[ver - 1] == "✖"):
                        continue
                    if hor == 3 and (line_3[ver - 1] == "●" or line_3[ver - 1] == "✖"):
                        continue
                    if hor == 1:
                        line_1.insert(ver - 1, "✖")
                        del line_1[ver]
                        break
                    if hor == 2:
                        line_2.insert(ver - 1, "✖")
                        del line_2[ver]
                        break
                    if hor == 3:
                        line_3.insert(ver - 1, "✖")
                        del line_3[ver]
                        break
            elif cir_top_h == cir_h3 and set(line_3) != {"●", "✖"}:
                while True:
                    hor = random.randint(2, 4)
                    ver = random.randint(1, 4)
                    if hor == 2 and (line_2[ver - 1] == "●" or line_2[ver - 1] == "✖"):
                        continue
                    if hor == 3 and (line_3[ver - 1] == "●" or line_3[ver - 1] == "✖"):
                        continue
                    if hor == 4 and (line_4[ver - 1] == "●" or line_4[ver - 1] == "✖"):
                        continue
                    if hor == 2:
                        line_2.insert(ver - 1, "✖")
                        del line_2[ver]
                        break
                    if hor == 3:
                        line_3.insert(ver - 1, "✖")
                        del line_3[ver]
                        break
                    if hor == 4:
                        line_4.insert(ver - 1, "✖")
                        del line_4[ver]
                        break
            elif cir_top_h == cir_h4 and set(line_4) != {"●", "✖"}:
                while True:
                    hor = random.randint(3, 4)
                    ver = random.randint(1, 4)
                    if hor == 3 and (line_3[ver - 1] == "●" or line_3[ver - 1] == "✖"):
                        continue
                    if hor == 4 and (line_4[ver - 1] == "●" or line_4[ver - 1] == "✖"):
                        continue
                    if hor == 3:
                        line_3.insert(ver - 1, "✖")
                        del line_3[ver]
                        break
                    if hor == 4:
                        line_4.insert(ver - 1, "✖")
                        del line_4[ver]
                        break
            else:
                if set(line_1) == {"✖", "ー"}:
                    I = line_1.index("ー")
                    line_1.insert(I, "✖")
                    del line_1[I + 1]
                elif set(line_2) == {"✖", "ー"}:
                    J = line_2.index("ー")
                    line_2.insert(J, "✖")
                    del line_2[J + 1]
                elif set(line_3) == {"✖", "ー"}:
                    K = line_3.index("ー")
                    line_3.insert(K, "✖")
                    del line_3[K + 1]
                elif set(line_4) == {"✖", "ー"}:
                    L = line_4.index("ー")
                    line_4.insert(L, "✖")
                    del line_4[L + 1]

    time.sleep(1)
    turn = 1 - turn
