class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score == other.score

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score != other.score

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score < other.score

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score <= other.score

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score > other.score

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score >= other.score


class StudentManager:
    def __init__(self, init_id=100):
        self.students = {}
        self.stu_id = init_id

    def add_student(self, student):
        self.students[self.stu_id] = student
        print(f'添加成功，{student.name} -> ID: {student.score}')
        self.stu_id += 1

    def update_score(self, stu_id, new_score):
        self.students[stu_id].score = new_score

    def find_student(self, name):
        return [target for target in self.students.values() if target.name == name]

    def delete_student(self, stu_id):
        self.students.pop(stu_id, None)

    def __iter__(self):
        self._ids = list(self.students.keys())
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.students):
            raise StopIteration
        stu = self.students[self._ids[self.i]]
        self.i += 1
        return stu

    def __contains__(self, name):
        return any(stu.name == name for stu in self.students.values())

    def __len__(self):
        return len(self.students)

if __name__ == "__main__":
    manager = StudentManager()

    # 添加学生
    s1 = Student("小甲鱼", 666)
    s2 = Student("不二如是", 888)
    s3 = Student("张三李四", 233)
    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)

    # 更新学生成绩
    manager.update_score(100, 999)

    # 查找学生
    stu = manager.find_student("小甲鱼")
    for target in stu:
        print(f"查找 -> {target.name}，成绩: {target.score}")

    # 删除学生
    manager.delete_student(102)

    # 迭代学生列表
    for student in manager:
        print(f"迭代 -> 姓名：{student.name}，成绩: {student.score}")

    # 检查学生是否在列表中
    print("小甲鱼" in manager)

    # 获取学生数量
    print(len(manager))

    # 学生之间的成绩PK
    print(s1 > s2)
