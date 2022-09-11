## 10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
## 200万以下の全ての素数の和を求めよ.

x = 0
limit = 2000000
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        x = x + i
        print(i)
print(x)