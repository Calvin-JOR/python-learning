'''https://fishc.com.cn/thread-214231-1-2.html
做一个员工管理系统'''
#员工类
class Employee:
    LEVEL_ORDER = ['E', 'T', 'M']
    MAX_GRADE = {'E': 10, 'T': 6, 'M': 3}
    def __init__(self, name, level, grade, year, uid):
        self.name = name
        self.level = level
        self.grade = grade
        self.year = year
        self.uid = uid
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_grade(self):
        return self.grade
    def get_year(self):
        return self.year
    def get_uid(self):
        return self.uid
    def salary(self):
        if self.level == 'E':
            sal = 3000 + 500*self.grade + 50*self.year
        elif self.level == 'T':
            sal = 4000 + 800*self.grade + 100*self.year
        elif self.level == 'M':
            sal = 5000 + 1000*(self.grade + self.year)
        return sal

class Manage:
    def __init__(self):
        self.employees = {}
        self.uid = 10000
    def run(self):
        order = 0
        while order != '5':
            order = input('1.录入 2.查询 3.升级 4.降级 5.退出 ')
            if order == '1':
                self.create()
            elif order == '2':
                if self.employees is None:
                    print('当前没有员工')
                while True:
                    suborder = input('1.工号查询 2.职位查询: ')
                    if suborder not in ['1', '2']:
                        continue
                    break
                if suborder == '1':
                    self.id_search()
                elif suborder == '2':
                    self.level_search()
            elif order == '3':
                self.promote()
            elif order == '4':
                pass

    def create(self):
        name = input('姓名： ')
        level = input('职位(E.普通员工 T.组长 M.经理): ').upper()
        while level not in ['E', 'T', 'M']:
            level = input('职位(E.普通员工 T.组长 M.经理): ').upper()
        max_g = Employee.MAX_GRADE[level]
        grade = int(input('级别：'))
        while grade > max_g:
            grade = int(input(f'该职位最高为{max_g}级，请重新输入: '))
        year = int(input('工龄：'))
        self.employees[self.uid] = Employee(name, level, grade, year, self.uid)
        sal = self.employees[self.uid].salary()
        print(f'录入成功！ 姓名：{name}, 工号：{self.uid}, 薪资：{sal}')
        self.uid += 1

    def id_search(self):
        uid = int(input('请输入工号: '))
        while uid not in self.employees:
            print('该工号不存在')
            uid = int(input('请重新输入: '))
        print(f'姓名: {self.employees[uid].get_name()}')
        print(f'职位: {self.employees[uid].get_level()}')
        print(f'级别: {self.employees[uid].get_grade()}')
        print(f'工龄: {self.employees[uid].get_year()}')
        print(f'薪资: {self.employees[uid].salary()}')

    def level_search(self):
        while True:
            level = input('请输入职位E.职员 T.组长 M.经理: ').upper()
            if level not in ['E', 'T', 'M']:
                continue
            matched = [emp for emp in self.employees.values() if emp.get_level() == level]
            if not matched:
                print('该职位暂无员工，请重新输入')
                continue
            break

        lv_map = {'E': '职员', 'T': '组长', 'M': '经理'}
        lv = lv_map[level]
        print(f'目前{lv}共有 {len(matched)}人')
        for emp in matched:
            print(f'工号: {emp.get_uid()} - 姓名 {emp.get_name()}')

    def foreplay(self):
        while True:
            uid = int(input('请输入工号: '))
            if uid not in self.employees:
                print('该工号不存在')
                continue
            break
        emp = self.employees[uid]
        sal = emp.salary()
        print(f'{emp.get_name()}, '
                f'工号: {emp.get_uid()},'
                f'当前职位: {emp.get_level()}{emp.get_grade()},'
                f'当前薪资: {sal},')
        return emp
        
    def promote(self):
        emp = self.foreplay()
        sal = emp.salary()
        prom = int(input('请输入升级级数: '))
        if emp.get_grade() + prom > Employee.MAX_GRADE[emp.get_level()]:
            if emp.get_level() == 'M':
                emp.grade = 3
                print('M3为当前最高职级')
            else:
                emp.grade = 1
                idx = Employee.LEVEL_ORDER.index(emp.level)
                emp.level = Employee.LEVEL_ORDER[idx + 1]
        else:
              emp.grade += prom
        print('升级成功！')
        change = emp.salary()-sal
        print(f'{emp.get_name()}, '
                f'工号: {emp.get_uid()},'
                f'升级后职位: {emp.get_level()}{emp.get_grade()},'
                f'升级后薪资: {emp.salary()}({change})')

def main():
    m = Manage()
    m.run()
main()