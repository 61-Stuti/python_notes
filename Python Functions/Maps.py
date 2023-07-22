#maps
def splicer(nums):                             

    if len(nums)%2 == 0:                        #map passes an argument/function so no () required 
        return "EVEN"
    else:
        return nums[0]
    


names=["sally", "bella", "john"]
e=  list(map(splicer,names))
print(e)

for item in map(splicer,names):
    print(item)



#filter
def check_even(numbers):                         
    return numbers%2 == 0

my_nums = [1,2,3,4,5,6]

f= list(filter(check_even,my_nums))
print(f)

for item in filter(check_even,my_nums):
    print(item)




square = lambda num: num ** 2                     #lambda is anonymous function
print(square(5))

my_nums = [1,2,3,4,5,6]
a= list(map(lambda num: num ** 2, my_nums))                     # lambda using map
print(a)

b= list(filter(lambda num: num % 2 == 0, my_nums))               # lambda using filter
print(b)


names=["sally", "bella", "john"]
f = list(map(lambda x: x[-1], names))
print(f)