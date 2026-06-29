words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]

res = []
for i in words:
    j = i.lower()
    if j.strip('qwertyuiop') == '' or j.strip('asdfghjkl') == '' or j.strip('zxcvbnm') == '':
        res.append(j)
print(res)