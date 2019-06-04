from multiprocessing import Process  # 创建进程的模块

def task(name):
    print(name)

if __name__ == '__main__':
    # 开启子进程  参数1：方法名(不要带括号)   参数2：参数（元祖）      返回对象
    p = Process(target=task, args=('子进程1',))
    p.start()  # 只是给操作系统发送了一个就绪信号，并不是执行。操作系统接收信号后安排cpu运行
    print(p.pid)
    print('主进程')

    # 输出：主进程--> 子进程