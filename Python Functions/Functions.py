# def name of function():                      lowercase words only- snake casing
# a function is some stored codethat we use. A function takes some input and produces an output
def name_of_function(name):
    print("Hello " +name)

name_of_function("Jose")



def even_check(number):
    return number %2==0

print(even_check(21))



def addition(x,y):                            #return allows to save the result of the variable which print does not
    z=x+y
    return z

print(addition(2,3))


def check_even_list(num_list):
     for number in num_list:
         if number % 2==0:
             return True
         else:
             pass                   #if we put return false in else statement then it will check only the 1st element and will return the value false and will not check the next element
     return False

b= check_even_list([1,1,5,3])
print(b)



def check_even_list(num_list):
     even_list=[]
     for number in num_list:
         if number % 2==0:
             even_list.append(number)
         else:
             pass                   

b= check_even_list([1,2,4,3])
print(b)

### TUPLE UNPACKING
def best_employee(work_hours):

    hours_max=0
    employee_name=''

    for employee,hours in work_hours:
        if hours > hours_max:
            hours_max = hours
            employee_name = employee
        else:
            pass
    return employee_name,hours_max
    
name, hours = best_employee([('abby',400),('billy', 4000),('gracy',100)])
print(name)
print(hours)

#Join
def master_yoda(text):
   word = text.split()
   result = (word[::-1])
   statement = " ".join(result)
   print(statement)
master_yoda("I am Home")



