## 3の倍数の時に、fooと出力するプログラムを作成せよ
# inputしたい時はデバッグモードにして実行しましょう
## 左のサイドバーにある三角と虫のアイコンをクリックしましょう

num = int(input("数字を入力して下さい"))

if  num % 3 == 0:
    print("foo")
else:
    print("noo")