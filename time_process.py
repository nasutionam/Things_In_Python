from time import time
from timeit import timeit

''' 
    USING TIME MODULE
'''
start = time()
result = sum([i for i in range(10000000)])
end = time()
total = end - start
print(f"time elapsed = : {total:.2f} seconds")

'''
    USING TIMEIT MODULE
'''
var = "sum([i for i in range(10000000)])"
result2 = timeit(var, number=1)
print(f"time elapsed = : {result2:.2f} seconds")
