'''列举出当前目录下的所有文件的尺寸'''
from pathlib import Path
from time import strftime, localtime

p = Path.cwd()
print(f'当前路径：{p}' )
all = []
for each in p.iterdir():
    size = each.stat().st_size
    time = strftime('%Y-%m-%d %H:%M:%S', localtime(each.stat().st_mtime))
    string = f'文件名：{each.name}, \n文件尺寸：{size}字节,\t修改时间：{time}'
    print(string)