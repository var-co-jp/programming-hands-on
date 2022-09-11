# 九九の表を作るプログラムを作成せよ。式と答えも表示せよ。
i = 1
# 段のループ
while i <= 9:
    j = 1
    # 段内のループ
    while j <= 9:
        a = i * j
        # i.j.aの表示
        if(i<=j):
            print(i,"x",j,"=",a)
        j = j + 1
    i = i + 1