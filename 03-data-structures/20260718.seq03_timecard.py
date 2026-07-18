'''假设有一个密室，每次只能放一个人进去，
在进去之前和出来之后都要求摁一下门口的打
卡机按钮，打卡机会依次将名字和进出时间戳
记录为以下的格式：
times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]
意为：
A 君是从时间戳为 0 的时候进入，从时间戳为 1 的时候出来，总共耗时为 1
B 君是从时间戳为 1 的时候进入，从时间戳为 3 的时候出来，总共耗时为 2
...
现在要求大家编写代码，统计给定的数据，打印耗时最长和最短的人员名称'''

times = [1, 3, 3.5, 6.5, 9.5, 10, 10.8]
names = ["A", "B", "C", "D", "E", "F", "G"]

max_name = [names[0]]
min_name = [names[0]]
max_time = times[0]
min_time = times[0]

for i in range(1, len(names)):
    each_name = names[i]
    each_time = times[i] - times[i-1]

    if each_time > max_time:
        max_name.clear()
        max_name.append(each_name)
        max_time = each_time
    elif each_time == max_time:
        max_name.append(each_name)
    elif each_time < min_time:
        min_name.clear()
        min_name.append(each_name)
        min_time = each_time
    elif each_time == min_time:
        min_name.append(each_name)
    
print(f'最快的是：{min_name}，耗时{min_time}')
print(f'最慢的是：{max_name}，耗时{max_time}')