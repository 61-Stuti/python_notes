game_list = [0,1,2]

#Display game
def display_game(game_list):
    print("Here's the current list: ")
    print(game_list)

display_game(game_list)

#Position choice

def position_choice():
    choice = "wrong"

    while choice not in ['0','1','2']:
        choice = input("Pick a position from 0,1,2: ")

        if choice not in ['0','1','2']:
            print("Sorry invalid choice")

    return int(choice)
y= position_choice()
print(y)

#replacement in game list at whichever position you want

def replacement_choice(game_list, position):
    
    user_replacement = input("Enter a string: ")

    game_list[position] = user_replacement

    return game_list
z = replacement_choice(game_list, 2)
print(z)

#now to see whether to keep playing the game or not

def gameon_choice():

    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Keep playing? Y or N: ")

        if choice not in ['Y', 'N']:
            print("invalid choice")

    if choice == 'Y':
        return True
    else:
        return False
    
e = gameon_choice()
print(e)

#Combination of all functions to play a game

game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()