#       Tail Recursion

#If a recursive function calling itself and 
#that recursive call is the last statement in the function then it’s known as Tail Recursion. 
# After that call the recursive function performs nothing. 

def fun(n):
	if (n > 0):
		print(n, end=" ")
		# Last statement in the function
		fun(n - 1)

# Driver Code
x = 3
fun(x)