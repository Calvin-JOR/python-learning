'''定义一个名为 FileManager 的类，该类可以实现简单的文件管理功能，
包括浏览目录、创建文件、重命名文件和删除文件'''
'''额外功能：
1.递归目录浏览：实现递归文件和文件夹浏览功能，以便用户能够看到整个目录结构
2.文件搜索功能：实现一个文件搜索功能，根据文件名或其他属性搜索文件
3.文件排序：在浏览文件时，可以根据文件名、大小、修改时间等属性对文件进行排序'''

from pathlib import Path

class FileManager:
    def __init__(self):
        self.p = Path.cwd()
        self.sort_keys = {'name':lambda x:x.name.lower(),
                    'size':lambda x:x.stat().st_size,
                    'time':lambda x:x.stat().st_mtime}
        
    def browse(self, p=None, prefix='', order=None):
        if p is None:
            p = self.p
            order = self.sort_keys.get(input('排序依据(name/size/time): '), self.sort_keys['name'])
        items = sorted(p.iterdir(), key=order)
        for i, each in enumerate(items):
            is_last = (i == len(items)-1)
            connector = '└─>' if is_last else '├─>'
            if each.is_dir():
                print(f'{prefix}{connector}{each.name}\\')
                extension = '    ' if is_last else '│   '
                self.browse(each, prefix + extension, order)
            else:
                print(f'{prefix}{connector}{each.name}')

    def create(self, name):
        (self.p/name).touch()

    def rename(self, oldname, newname):
        new = self.p / newname
        if new.exists():
            print("目标文件已存在")
            return
        (self.p/oldname).rename(new)

    def delete(self, name):
        (self.p/name).unlink(missing_ok = True)

    def search(self, name):
        found = False
        for each in self.p.rglob('*'):
            if each.is_file() and name.lower() in each.name.lower():
                print(each)
                found = True
        if not found:
            print('not found')


fm = FileManager()
#fm.create('zzz.txt')
#fm.rename('zzz.txt', 'zxd.txt')
#fm.browse()
#fm.delete('zxd.txt')
fm.search('OOP10')