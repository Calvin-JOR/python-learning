#给定一个字符串 text 和字符串列表 words，返回 words 中每个单词在 text 中的位置
txt = input("text:")
wds = input("words:")
wds = wds.split()

result = []
for each in wds:
    temp = txt.find(each)
    while temp != -1:
        result.append([temp, temp + len(each) - 1])
        temp = txt.find(each, temp + 1) #更新temp的起始位置

print(result)