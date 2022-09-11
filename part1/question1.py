# 九九の段を出力するプログラムを作成
## 今回は九九の答えのみを表示してみましょう

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end= " ")
    print("「{}」の段です".format(i))

## while文でも作成してみましょう

print("********************************")
i = 1
while i < 10:
	j = 1
	while j < 10:
		print(i * j, end=" ")
		j = j + 1
	print()
	i = i + 1