'''通过运算符重载，将中文数字转换为阿拉伯数字'''
class CN_int:
    def __init__(self, num):
        self.num = num
    def __int__(self):
        try:
            return int(self.num)
        except ValueError:
            CN = {'零':0, '一':1, '二':2, '三':3, '四':4, '五':5, 
                  '六':6, '七':7, '八':8, '九':9, '十':10, 
                  '百':100, '千':1000, '万':10000, '亿':10**8}
            number  = 0     #当前读取数字
            result = 0
            for each in self.num:
                if each not in CN:
                    raise ValueError(f'不认识的字符: {each}')
                
                if each in ['十', '百', '千', '万', '亿']:
                    if each == '十':
                        result += (number or 1) * 10
                    elif each == '百':
                        result += number * 100
                    elif each == '千':
                        result += number * 1000
                    elif each == '万':
                        result += number * 10000
                    elif each == '亿':
                        result += number * 10**8
                    number = 0
                else:
                    number = CN[each]
            return result + number

n = CN_int(input('输入中文数字: '))
print(int(n))