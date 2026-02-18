
from functools import reduce

l=[11,43,76,98,34,56]
def greater(a,b):
    if(a>b):
     return a
    return b

print(reduce(greater,l))

