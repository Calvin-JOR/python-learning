'''通过运算符重载，将中文数字转换为阿拉伯数字float版'''
class CN_float:
    def __init__(self, num):
        self.num = num
    def __float__(self):
        try:
            return float(self.num)
        except ValueError:
            CN = {'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, 
                  '六':6, '七':7, '八':8, '九':9, '十':10, '百':100,
                  '千':1000, '万':10000, '亿':10**8, '负':None}
            total   = 0     #万/亿的部分
            section = 0     #万以内的部分
            number  = 0     #当前临时数字
            frac = ''

            minus = self.num.startswith('负')
            if minus:
                self.num = self.num[1:]
            _int, _, _float = self.num.partition('点')
            for each in _int:
                if each not in CN:
                    raise ValueError(f'不认识的字符: {each}')
                val = CN[each]      #当前读取数字
                if val < 10:        #0~9
                    number = val
                elif val < 10000:   #十百千
                    section += (number or 1) * val
                    number = 0
                elif val == 10000:  #万
                    total += (section + number) * val
                    section = number = 0
                else:               #亿
                    total = (total + section + number) * val
                    section = number = 0

            if number and len(_int) >= 2:
                prev = CN[_int[-2]]     # 最后一个数字前面的字符
                if prev >= 100:             # 百千万亿
                    number *= prev // 10    # 一百一 → 1 * (100//10) = 10

            for each in _float:
                if each not in CN or CN[each] >= 10:
                    raise ValueError(f'不认识的字符: {each}')
                frac += str(CN[each])
            flt = float('0.' + frac) if frac else 0.0

            fin = total + section + number + flt
            if minus == True:
                fin *= -1
            return fin
n = CN_float(input('输入中文数字: '))
print(float(n))