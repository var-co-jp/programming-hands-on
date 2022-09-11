# 2つの正の整数値を入力させ、互いに素であるか判定するプログラムを作成せよ。

num1 = int(input("数字を入力して下さい"))
num2 = int(input("数字を入力して下さい"))

if num1 <= 1:
    print(False)
else:
    for i in range(2, int(num1**0.5)+1):
        if num1 % i == 0:
            print(False)
            break
    else:
        for i in range(2, int(num2**0.5)+1):
            if num2 % i == 0:
                print(False)
                break
        else:
            print(True)

print(num1**0.5)