'''获取指定路径（文件夹）中所有的文件名，并按文件尺寸按从小到大进行排序'''
from pathlib import Path
from time import strftime, localtime

p = Path.cwd()
files = []
for f in p.iterdir():
    if f.is_file():
        files.append(f)

#files.sort(key=lambda f:f.stat().st_size) #题6
files.sort(key=lambda f:f.stat().st_mtime)
for each in files:
    time = strftime('%Y-%m-%d %H:%M:%S', localtime(each.stat().st_mtime))
    print(each.name, f'\n{each.stat().st_size}字节, 修改时间{time}')
print(files[-1].name)
