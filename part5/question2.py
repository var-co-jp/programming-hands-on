# バブルソートを作成せよ

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]: #左の方が大きい場合
                data[j], data[j+1] = data[j+1], data[j] #前後入れ替え

    return data

if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = bubble_sort(data.copy())

    print(f"{data}  =>  {sorted_data}")
