## 「*」を使って、直角三角形を下記のように画面に表示するプログラムを作成せよ

h = int(5)
for i in range(h + 1):
    for j in range(i):
        print("*", end="")
    print()

### while文

h = int(5)
i = 1
while i <= h:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1