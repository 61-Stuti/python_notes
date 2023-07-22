def func_one(n):
    return [str(num) for num in range(n)]
print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))
print(func_two(10))


import time
#current time before code
start_time = time.time()

#run code
result1 = func_one(10000)

#current time after the code
end_time = time.time()

#elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

##########################
#current time before code
start_time = time.time()

#run code
result = func_two(100000)

#current time after the code
end_time = time.time()

#elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)
