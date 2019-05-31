
class Manager:
    role = "管理员"
    def __init__(self,name,sex,phone,mail):
        self.name = name
        self.sex = sex
        self.phone = phone
        self.mail = mail

    def createClass(self):
        print("create class")

    def createTeacher(self):
        print("createTeacher")

    def createStu():
        print("createStu")


manager = Manager("safly","男",123456,123456)

print("----设置对象属性------")
setattr(manager,"age",20)
print(manager.age)

print("----删除对象属性------")
delattr(manager,"age")
# 'Manager' object has no attribute 'age'
# print(manager.age)

print("---对象不能删除类属性---")
setattr(Manager,"country","china")
print(Manager.country)
# delattr(manager,"country")
# print(Manager.country)

print("----设置对象方法------")
def create_course(self):
    print('创建了一个课程')

setattr(manager,'create_course',create_course)
manager.create_course(manager)

def create_grade():
    print('创建了一个班级')
setattr(manager,'create_grade',create_grade)
manager.create_grade()

