'''https://fishc.com.cn/thread-214637-1-2.html
做一个租车系统'''
#汽车类
class Car:
    def __init__(self, brand, model, platenum, dayrent, sp, carid):
        self.brand = brand
        self.model = model
        self.platenum = platenum
        self.dayrent = dayrent
        self.sp = sp
        self.carid = carid
    def __str__(self):
        return (f'编号:{self.carid:<8}品牌:{self.brand:\u3000<3}型号:{self.model:\u3000<3}'
                f'日租:{self.get_dayrent():>3}$')
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_platenum(self):
        return self.platenum
    def get_dayrent(self):
        return self.dayrent
    def get_carid(self):
        return self.carid
    def calc(self, days):
        return self.get_dayrent() * days

#汽车子类
class EconomyCar(Car):
    def get_dayrent(self):
        return super().get_dayrent() - self.sp
class LuxuryCar(Car):
    def get_dayrent(self):
        return super().get_dayrent() + self.sp
class SportCar(Car):
    pass
    '''def get_dayrent(self):
        return super().get_dayrent() + self.sp'''
class SUV(Car):
    def get_dayrent(self):
        if self.day > 7:
            return super().get_dayrent() * self.sp * 0.1 * 0.7
        return super().get_dayrent() * self.sp

class Manage:
    def __init__(self):
        self.cars = {}
        self.stocks = {}
        self.rented = {}
        self.carid1 = 10000
        self.carid2 = 20000
        self.carid3 = 30000
        self.carid4 = 40000

    def operate(self):
        order = 0
        while order != '4':
            print('\n欢迎使用汽车租赁')
            order = input('\n1.录入汽车 2.开始租车 3.开始还车 4.退出: ')
            print()
            if order not in ['1', '2', '3', '4']:
                continue
            if order == '1':
                self.register()
            elif order == '2':
                self.rent()
            elif order == '3':
                self._return()

    def register(self):
        cardict = {'1':[EconomyCar,self.carid1],'2':[LuxuryCar,self.carid2],\
                   '3':[SportCar,self.carid3],  '4':[SUV,self.carid4]}
        carsp = {'1':'补贴: ', '2':'保险: ', '3':'损耗: ', '4':'折扣: '}
        while True:
            order = input('1.经济型 2.豪华型 3.跑车 4.SUV: ')
            if order not in ['1', '2', '3', '4']:
                continue
            while True:
                counts = input('请输入要录入的数量: ')
                if not counts.isdecimal():
                    continue
                counts = int(counts)
                break
            for i in range(counts):
                print(f'请输入第{i+1}量车')
                brand    = input('品牌: ')
                model    = input('型号: ')
                platenum = input('车牌: ')
                dayrent  = int(input('租金: '))
                sp = int(input(f'{carsp[order]}'))
                carid = cardict[order][1]
                car = cardict[order][0](brand, model, platenum, dayrent, sp, carid)
                self.cars[carid] = car
                self.stocks.setdefault(cardict[order][0], []).append(car)
                carid += 1
                print('>>-------------------------------------------<<')
            break
    def rent(self):
        cardict = {EconomyCar:'经济型', LuxuryCar:'豪华型', SportCar:'跑车', SUV:'SUV'}
        count = 1
        for each in cardict:
            if self.stocks.get(each):
                print(f'{count}.{cardict[each]}汽车，共有{len(self.stocks[each]):2}辆')
                for i in self.stocks[each]:
                    print(i)
                print('>>-------------------------------------------<<')
            count += 1
        while True:
            carid = input('请输入要租赁的车辆编号: ')
            if not carid.isdecimal():
                continue
            carid = int(carid)
            if carid not in self.cars or carid in self.rented:
                print('该车已出租或未有该编号车辆，请重新输入')
                continue
            days = input('请输入要租赁的天数: ')
            if not days.isdecimal():
                continue
            days  = int(days)
            break
        price = self.cars[carid].calc(days)
        car = self.cars[carid]
        self.rented[carid] = car
        self.stocks[type(car)].remove(car)
        print(f'租赁{days}天，租金为：{price:>3}$')
        print('>>-------------------------------------------<<')

    def _return(self):
        while True:
            carid = int(input('请输入车辆编号: '))
            if carid not in self.cars or carid not in self.rented:
                print('该车尚未出租或未有该编号车辆，请重新输入')
                continue
            car = self.rented.pop(carid)
            self.stocks.setdefault(type(car), []).append(car)
            self.stocks[type(car)].sort(key = lambda c : c.carid)
            break
        print('车辆归还成功')
        print('>>-------------------------------------------<<')

m = Manage()
m.operate()