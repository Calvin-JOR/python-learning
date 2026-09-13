'''在当前文件夹下创建1个子文件夹，再在里面创建10个子文件夹，
每个子文件夹下又放入自身的 10 个拷贝'''
from pathlib import Path
p = Path.cwd()
p = p / '20260913file3hwk'
new_dir = p.mkdir(exist_ok=True)
self = __file__

with open(self, 'r', encoding='utf-8') as sf:
    txt = sf.read()

for i in range(10):
    p = p / f'{i}'
    sub_dir = p.mkdir()
    for j in range(10):
        f = p / f'{j}.py'
        with open(f, 'w', encoding='utf-8') as file:
            file.write(txt)
    p = p.parent