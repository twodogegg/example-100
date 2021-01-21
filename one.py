# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析 遍历全部可能，把有重复的剃掉。
import itertools

total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j, k)



arr = [1,2,3,4]
for i in itertools.permutations(arr, 3):
    print(i)