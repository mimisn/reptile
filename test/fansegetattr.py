class Manager:
    role = "管理员"
    def createClass(self):
        print("create class")

    def createStu():
        print("createStu")

m = Manager()

f = getattr(Manager,"createClass")
f(Manager)

f = getattr(Manager,"createClass")
f(m)

role = getattr(Manager,"createStu")
role()

#对象获取类属性
role = getattr(Manager,"role")
print(role)
