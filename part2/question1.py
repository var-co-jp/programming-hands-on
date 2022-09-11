# 2つの値を入力して変数に格納し、変数の内容を交換して画面に表示するプログラムを作成せよ。

i = 300
j = 100

print(i, j)
def change(i, j):
    num = i
    i = j
    j = num
    print(i, j)
change(i,j)