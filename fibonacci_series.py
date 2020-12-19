# fibonacci_series.py

"""
import time 

def fibonacci_series(inp):
	
	if (inp < 2) or (inp == 2):
		return 1 

	return fibonacci_series(inp-1) + fibonacci_series(inp-2)

inp = [1,3,6,13,20,25]
for i in inp:
	starting = time.time()
	result = fibonacci_series(i)
	ending = time.time()
	print( str(i) + ' Result : '+ str(result) + ' Estimated time: %s seconds' %(ending - starting))

# without dynamic programming

# 1 Result : 1 Estimated time: 0.0 seconds
# 3 Result : 2 Estimated time: 0.0 seconds
# 6 Result : 8 Estimated time: 0.0 seconds
# 13 Result : 233 Estimated time: 0.0 seconds
# 20 Result : 6765 Estimated time: 0.0020270347595214844 seconds
# 25 Result : 75025 Estimated time: 0.021943092346191406 seconds
"""


import time 

def fibonacci_series(inp, memo={}):
	
	if (inp < 2) or (inp == 2):
		return 1 
	if inp in memo:
		return memo[inp]

	memo [inp] = fibonacci_series(inp-1) + fibonacci_series(inp-2)
	return memo[inp]

inp = [1,3,6,13,20,25,50,100]
for i in inp:
	starting = time.time()
	result = fibonacci_series(i)
	ending = time.time()
	print( str(i) + ' Result : '+ str(result) + ' Estimated time: %s seconds' %(ending - starting))

# with dynamic programming

# 1 Result : 1 Estimated time: 0.0 seconds
# 3 Result : 2 Estimated time: 0.0 seconds
# 6 Result : 8 Estimated time: 0.0 seconds
# 13 Result : 233 Estimated time: 0.0 seconds
# 20 Result : 6765 Estimated time: 0.0 seconds
# 25 Result : 75025 Estimated time: 0.0 seconds
# 50 Result : 12586269025 Estimated time: 0.0 seconds
# 100 Result : 354224848179261915075 Estimated time: 0.0 seconds



