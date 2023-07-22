#DISPLAYING INFORMATION

row1= [' ', ' ', ' ']
row2= [' ', ' ', ' ']
row3= [' ', ' ', ' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    
display(row1, row2, row3)

#modify the element in row2
row2[1] = 'X'

display(row1, row2, row3)

result = input("enter a number: ")
result_int = int(result)
print(result_int)
    

#take the position input and then print the row
position_index = int(input("enter a no"))
new_row1 = row1[position_index]
print(new_row1)

#convert the input from string to int
def user_choice():

    choice = input("Please select a number from (0-10): ")

    return int(choice)
y = user_choice()
print(y)

#check whether the input is int or not
def user_choice():

    choice = "WRONG"
    while choice.isdigit() == False:
        choice = input("Please select a number from (0-10): ")

        if choice.isdigit() == False:
            print("Sorry not a digit")
        
        else:
            print(choice)

user_choice()


#to check whether the number is in digit and in range
choice = "wrong choice"
acceptable_values = range (0,10)
within_range = False

while choice.isdigit() == False or within_range == False:
    choice = input("enter the numberrr: ")
    
    #digit check
    if choice.isdigit() == False:
        print("number is not a digit")

    #range check
    if choice.isdigit() == True:
        if int(choice) in acceptable_values:
            within_range = True
        else:
            print("not in range")
            within_range = False



