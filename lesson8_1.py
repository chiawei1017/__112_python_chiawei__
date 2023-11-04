from tools import Student

stu1 = Student(name="robert",chinese=89,english=92,math=19)
print(stu1.name)
print(stu1.chinese)
print(stu1.english)
print(stu1.math)
print(stu1.sum())


from tools import getStudent

stu1 = getStudent(name="robert",chinese=89,math=92,english=75)
print(stu1.name)
print(stu1.chinese)
print(stu1.english)
print(stu1.math)
print(stu1.sum())