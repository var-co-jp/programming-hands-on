# 「*」を使って、正方形を下記のように画面に表示するプログラム

h = int(input("数字を入力して下さい"))
j = 1
# 1行目表示
for j in range(0,h):
    print("*", end="")
    if(j == h):
        print()
    j = j + 1
print()

i = 2
#2~最終行前表示
while i < h:
    print("*", end= "")
    j = 2
    while j < h:
        print(" ", end="")
        j = j + 1
    print("*")
    i = i + 1

j = 1
# 最終行
for i in range(0,h):
    print("*", end="")
    if(j == h):
        print()
    j = j + 1