# 足し算と引き算をする電卓を作成せよ。コマンドラインに数字を入力すると値を表示する。

x = int(input("1つ目の数字"))
y = int(input("2つ目の数字"))
add = x + y
sub = x - y
print("足し算の合計{}".format(add))
print("引き算の合計{}".format(sub))
