from functools import reduce


# REDUCE

product = reduce((lambda x, y: x*y), [1,2,3,4])
#grabs first 2, then grabs result times next, then result times next, etc
# 1*2, 2*3, 6*4
print(product)


# MAP 
# map(function_object, iterable1, iterable2, etc)
result = list(map(lambda x,y: x+y, [1,2], [4,5,6]))
# [1+4, 5+2]
print(result)