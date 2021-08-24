def is_straight(nums):
    dup = set()
    min_num = 100
    max_num = 1
    for num in nums:
        if num != 0:
            # 判断重复
            if num in dup:
                return False
            else:
                dup.add(num)

            # 找到最大值，最小值
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
    return max_num - min_num < 5


if __name__ == '__main__':
    test1 = [1, 1, 0, 0, 0]
    print(is_straight(test1))
    test2 = [1, 2, 0, 0, 5]
    print(is_straight(test2))
