from developers_functions import *
from mr_blackstar import *

print(dev_fun_1())
print(dev_fun_2())
print(dev_fun_3())


def recusrsion():
    if recusrsion() == 1:
        return 0
    else:
        return 1 + recusrsion()
