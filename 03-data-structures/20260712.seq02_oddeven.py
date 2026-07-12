''' 给定一个整数列表，调整该列表中整数的顺序，
使所有奇数排好序后放在数组的前半部分，所有偶数
排好序后放在数组的后半部分
比如给定的整数列表是  [1, 8, 7, 3, 6, 5, 4, 2]，
那么调整后的结果应该是[1, 3, 5, 7, 2, 4, 6, 8]'''

s = [1,8,7,3,6,5,4,2]
ds = sorted(s)
odd = []
even = []
for each in ds:
    if each % 2 == 0:
        even.append(each)
    else:
        odd.append(each)
print(odd + even)
