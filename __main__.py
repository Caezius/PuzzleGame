# File: Hello.py
#started 10-9/2021
import _setupStuff
import _gameClasses
import _functions
import keyboard
import time
#these guys are in the same directory, so you can just use their names without needing the full path

# 4-01/2022
# Setup
#
# 1. Have a universal 2d list containing the strings representing characters. It is the visual map that will be prined
# 2. Using a preset level list, intitialize Rock() variables, and add them to the Objects_in_play list

# add Rock objects to the Map list
#       (for each of the non-spaces in the level list, create a Rock() object with its location attributes the same as the given list's)
# 3. Set the User's position
# 4. Each turn, get a move from the user (a single key press)
# 5. After that key press, determine
#       a. if the direction the user moved is valid (kickable object there, not going out of the map's bounds)
#       b. If a piece should be moved by "kicking" it (need to check if there's a space past the object, in the direction the user is moving/kicking)
#6. Update the user's new position in the objects list, or display an error message.
#7.

#Object lists: stores all objects. each of them have their own location.
#NEW IDEA! The Rock objects will have an ID attribute, which is just their index in the list of objects
# objects_in_play[9] = Rock() object with an id attribute of 9;
#Use that id to find the same object, even if it's in a different position in the Map twoD_array
#for objects in Map

#Map: stores strings, each representing a game object or a spaces, that gets directly printed
#Objects_in_play: stores the actual game objects, though not in any meaningful order.
#To get an object located at a position on the map, one get's that visual marker's indexes,
#then loops through the objects_in_play list to find an object with the same location attributes as the visual marker


# 3. Take those game objects
start_Game = False
#!TEST CODE print("h"[0])
#!TEST CODE input()
print("ello")
#!TEST CODE var = input("input sumthn")
#!TEST CODE print(var[0])
print("Press \"Enter\" to start the game.")

#continues running until the enter key is pressed
while start_Game == False:
    if(keyboard.is_pressed("enter")):
        start_Game = True
        break
input() #for some reason, if you do this it stops the input() statement later from taking input instantly

print("Loading...") #a message to print while we stop the program for 3 seconds,
                    #so it doesnt take the enter key the user just pressed as the input (which will make an error, as the user will have pressed "enter" with no input typed)

time.sleep(2) #(if you leave your finger on enter, itll enter on the input statement for the inputtedSymbol variable)

print(("Type a key to represent your character, then press enter"))

inputtedSymbol = input("Type a key to represent your character, then press enter\nPlayer Symbol entered: ")

#!TEST CODE print("heel"[0])
playerSymbol = inputtedSymbol[0] #makes sure there is only one character used to represent the player, if the user entered a string this will only take the first letter

#OOP OK so now I remember why Player() wont work-you need to specify which m o d u l e the function is from
#Error 2: OK in the file where I defined the Player class, I put init() instead of __init__(), so THATS why there's an error about "Player() takes no arguments"
#Arrites Error 3: turns out (as observed when I printed out spawn_location) that when you use keyword args, their values are in a dictionary, with {"keyword_name": value}
#so I gotta go spawn_location["spawn_location"] to get the value
thePlayer = _gameClasses.GameObjectClass().PlayerClass(playerSymbol, spawn_location = [0, 0]) #the array [0, 0] is really just a filler, but is needed when we restart the player

thePlayer.randomly_Set_Location_()
#well, since the variable in _setupStuff can be accessed by any other file,
#we can just go ahead and use _setupStuff.puzzle_Board in any module each time we want to change the puzzle_Board's contents

#since imports in each file have no idea whats going on in another file, (each import is only in that file's scope) we can just import _setupStuff over and over in each module and not worry about import conflicts
#so it wont care if, in an imported module, we import a module we already imported in the main file-when importing, itll only look at that file's content, forgetting what happened in the file it had been imported in
_functions.update
_functions.show_Board_(_setupStuff.puzzle_Board)


while (start_Game == True):
    _functions.do_A_Turn_(thePlayer);


print("End Of Game. Noice.")








#________STYLING__________
#variable: list_of_things = [delicious]
#under_scores

#important/major program variable: the_Burger_Franchise
#camelCase_With_Underscores

#Functions: eat_Good_Food_(burger) <-also legal
#camelCase_With_Underscores_ but with an underscore at the end, marking it as a function


#class: class BestBurgers <-legal
#UpperUpper

#object: theWhopperBurger = BestBurgers("louisianian starduck")
#camelCaseBoiis

#module: import _burger_module
#_lower_case_with_starting_underscore

#Ex:
#anObject.get_Fries_With_That(num_of_fries);
