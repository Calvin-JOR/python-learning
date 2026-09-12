'''编写一个递归函数，实现glob()的搜索功能'''
from pathlib import Path
p = Path.cwd()
def GLOB(p:Path, c:str):
    string = ''
    if p.is_file() and p.suffix == c:
        string += f'{p.name}\n'
    else:
        for each in p.iterdir():
            string += GLOB(each, c)
    return string

print(GLOB(p, '.py'))