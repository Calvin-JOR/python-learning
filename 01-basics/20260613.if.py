"""
a = input("输入a\n")
b = input("输入b\n")
small = a if a <= b else b
print(f"small={small}")
"""
score = int(input("type your score:"))
grade = ('D' if 0 <= score < 60 else
         'C' if 60 <= score < 80 else
         'B' if 80 <= score < 90 else
         'A' if 90 <= score < 100 else
         'S' if score == 100 else
         "please input a value between 0~100")
print(f"your grade is {grade}")
