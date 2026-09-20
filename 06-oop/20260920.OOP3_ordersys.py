class Meet:
    nums = 0

class Egg(Meet):
    name = "鸡蛋"
    price = 1

class Beef(Meet):
    name = "牛肉"
    price = 25

class Mutton(Meet):
    name = "羊肉"
    price = 30

class Vegetable:
    nums = 0

class Onion(Vegetable):
    name = "洋葱"
    price = 2

class Tomato(Vegetable):
    name = "番茄"
    price = 2

class Potato(Vegetable):
    name = "土豆"
    price = 3

class Radish(Vegetable):
    name = "萝卜"
    price = 3

class Menu:
    egg = Egg()
    beef = Beef()
    mutton = Mutton() 
    onion = Onion()
    tomato = Tomato()
    potato = Potato()
    radish = Radish()
    def order(self):
        self.x = []
        print('请问要吃什么？')
        order = input('1.洋葱炒牛肉；2.洋葱炒羊肉；3.煎蛋；4.番茄炒蛋；5.土豆萝卜炖羊肉：')
        order = order.split()
        for o in order:
            if o == '1':
                self.onion.nums += 1
                self.beef.nums += 1
                self.x.extend([self.onion, self.beef])

            elif o == '2':
                self.onion.nums += 1
                self.mutton.nums += 1
                self.x.extend([self.onion, self.mutton])

            elif o == '3':
                self.egg.nums += 2
                self.x.append(self.egg)

            elif o == '4':
                self.tomato.nums += 2
                self.egg.nums += 3
                self.x.extend([self.tomato, self.egg])

            elif o == '5':
                self.potato.nums += 2
                self.radish.nums += 1
                self.mutton.nums += 2
                self.x.extend([self.potato, self.radish, self.mutton])

    def pay(self):
        total = 0
        mat = {}
        self.x = set(self.x)
        for each in self.x:
            print(each.name, each.price, '*', each.nums)
            total += each.price * each.nums

        print(f'一共消费{total}元')
menu = Menu()
menu.order()
menu.pay()