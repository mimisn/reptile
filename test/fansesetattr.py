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

    def createStu(self):
        print("createStu")


manager = Manager("safly","男",123456,123456)

print("----设置类属性------")
setattr(Manager,"country","china")
print(Manager.country)

print("----删除类属性------")
delattr(Manager,"country")
# #删除报错
# print(Manager.country)
print("----设置类方法------")
def Method(parm):
    print("我是被绑定的class之外的方法parm--",parm)

setattr(Manager,"Method",Method)
Manager.Method("saf")
Manager.Method(Manager)
Manager.Method(manager)

def Method():
    print("我是被绑定的class之外的方法parm--")
setattr(Manager,"Method",Method)
Manager.Method()
