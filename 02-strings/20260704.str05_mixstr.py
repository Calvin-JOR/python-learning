s = input("type your string:")
arr1 = []
arr2 = []
for each in s:
    if each.isalpha():
        arr1.append(each)
    else:
        arr2.append(each)
if len(arr1) != len(arr2):
    print("number of chars and numbers are not equal")
    exit()
else:
    arr3 = ''
    for i in range(len(arr1)):
        arr3 = arr1[i]+arr2[i]
        print(arr3, end = '')