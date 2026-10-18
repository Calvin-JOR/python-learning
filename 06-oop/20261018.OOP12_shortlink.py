'''制作一个短链接生成工具,让长URL变得更易分享、易记、易管理,并且能提供有关链接点击次数和其他有用的统计信息
生成短链接
存储 URL 映射（通过 __setitem__() 方法实现）
通过短链接获取长 URL（通过 __getitem__() 方法实现）
统计每个短链接被访问的次数
注意预防冲突的发生（即不同的 URL 恰巧生成了同一个短链接）'''

import random, string

class ShortURL:
    def __init__(self):
        self.url = {}            # 存储短链接和长链接的对应关系
        self.click = {}          # 存储短链接的点击次数
        self.long_to_short = {}  # 存储长链接到短链接的映射

    def __getitem__(self, short_url):
        # 当短链接被访问时，增加其点击次数，并返回对应的长链接
        if short_url in self.url:
            self.click[short_url] = self.click.get(short_url, 0) + 1
            return self.url[short_url]
        raise KeyError(f'Short URL {short_url} not exists')

    def __setitem__(self, short_url, long_url):
        self.url[short_url] = long_url

    def gen_short_url(self, long_url):
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]
        while True:             # 生成一个随机的短链接，长度为8
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if short_url not in self.url:
                break

        self.long_to_short[long_url] = short_url
        return short_url

    def get_clicked(self, short_url):
        return self.click.get(short_url, 0)

def main():
    url_gen = ShortURL()
    long_url = 'https://space.bilibili.com/9022882?spm_id_from=333.881.0.0'
    short_url = url_gen.gen_short_url(long_url)
    #print(f'short url: {short_url}')
    url_gen[short_url] = long_url   #通过先前定义的__setitem__来实现这一操作
    ori_url = url_gen[short_url]
    print(f'{ori_url} --> {short_url}')

    for _ in range(9):
        url_gen[short_url]
    print(f'link {short_url} has been clicked {url_gen.get_clicked(short_url)} times')

if __name__ == "__main__":
    main()