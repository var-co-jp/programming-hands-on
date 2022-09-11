# 入力した10個の数の中に5があるか調べるプログラムを作成せよ。

x = list(map(int, input()))
for i in range(len(x)):
    j =x[i]
    if j == 5:
        print("5です!!")
    else:
        print("5じゃないです")
