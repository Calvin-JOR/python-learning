'''自动统计文件夹中Python代码行数，空行不算'''
from pathlib import Path
def get_files(p:Path):
    files = []
    for each in p.iterdir():
        if each.resolve() == Path(__file__).resolve():  # 计算代码行数时，自本这个脚本不算进去
            continue
        if each.is_file() and each.suffix == '.py':
            files.append(each)
        if each.is_dir():
            files.extend(get_files(each))
    return files

def count(files):
    lines = 0
    for each in files:
        with open(each, 'r', errors='ignore') as f:
            t = f.readlines()
            lines += len(t) - t.count('\n') #空白行不算
    return lines

p = Path.cwd()
files = get_files(p)
recs = count(files)
print(recs)