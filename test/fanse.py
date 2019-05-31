import test.mokuai as mokuai
print(getattr(mokuai,"a"))
method = getattr(mokuai,"method")
ret = method(8888)
print(ret)
#print(mokuai.__dict__)

print(vars(mokuai))

aa = 11
def method():
    print("---method---")
import sys

print(sys.modules[__name__])
print(getattr(sys.modules[__name__],"aa"))
f = getattr(sys.modules[__name__],"method")
f()







