class Student:
    def __init__(self, name, number, age):
        self.name = name
        self.number = number
        self.age = age

    def set_gender(self, gender):
        self.gender = gender


stu = Student('wangpei', '2012124016', 21)

print(hasattr(stu, 'name'))
stu.set_gender('male')
stu.like = 'coding'
print(hasattr(stu, 'gender'))
print(hasattr(stu, 'like'))
