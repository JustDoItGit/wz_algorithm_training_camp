def drink(x):
    count = x  # 喝了多少瓶酒
    k1 = x  # 多少空瓶子
    k2 = x  # 多少瓶盖
    while k1 >= 3 or k2 >= 7:
        while k1 >= 3:
            change = k1 // 3
            count += change
            k1 %= 3
            k1 += change
            k2 += change
        while k2 >= 7:
            change = k2 // 7
            count += change
            k2 %= 7
            k1 += change
            k2 += change
    return count


if __name__ == '__main__':
    x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i in x_list:
        print(f'x={i}:\t{drink(i)}')

