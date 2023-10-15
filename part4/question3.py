# フィボナッチ数列を10000まで出力するプログラムを作成せよ。

def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(10000)


def fib2(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        tmp = a # 一時退避
        a = b
        b = tmp + b
    print()
fib2(10000)
