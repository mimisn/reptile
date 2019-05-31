# coding:utf-8


class Singleton1(object):

    name = ''

    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            print( 'creating instance of Singleton1')
            cls._instance = super(Singleton1, cls).__new__(cls)
            if len(args) > 0:
                cls.name = args[0]
            elif 'name' in kwargs:
                cls.name = kwargs['name']
        return cls._instance


class Singleton2(object):

    name = ''

    def __new__(cls, *args, **kwargs):
        if not '_instance' in vars(cls):
            print('creating instance of Singleton2')
            cls._instance = super(Singleton2, cls).__new__(cls)
            if len(args) > 0:
                cls.name = args[0]
            elif 'name' in kwargs:
                cls.name = kwargs['name']
        return cls._instance

if __name__ == '__main__':
    inst1 = Singleton1('a')
    inst2 = Singleton1(name='b')
    print( inst1 is inst2)
    print(inst1.name)
    print (inst2.name)
    print ('*' * 10)
    inst3 = Singleton2(name='b')
    inst4 = Singleton2('a')
    print (inst3 is inst4)
    print (inst3.name)
    print (inst4.name)