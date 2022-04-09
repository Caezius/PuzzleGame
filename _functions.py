#import matplotlib as plt
import _setupStuff
from _setupStuff import puzzle_Board as the_Board
import _gameClasses
import keyboard


def getPlayerPosition(player_repr, level_arr):
    #loop through all coordinates, find which coordinate has the "X", which denotes the player's starting position
    for y in range(level_arr.length):
        
        for x in range(level_arr[y].length):
            
            space = level_arr[y][x];
            
            if (space == player_repr):
                return [x, y]
            

#ya know, maybe instead of assuming Ive got access to a major variable, I should take it as one of the parameters
def show_Board_(twoDArr):
    print(twoDArr)

def reset_Board_(twoDArr):
    num_of_rows = len(twoDArr)
    print(num_of_rows)
    for row in range(0, num_of_rows):
        num_of_columns = len(twoDArr[row])
        print(num_of_columns)
        for column in range(0, num_of_columns):
            twoDArr[row][column] = " "

#waits for an arrow  key press, then returns the move name as a string
def checkFor(playerObj):
    print("Press an arrow key to move")

    move_Pressed = False #var we make to see if the player has made a move, turns true when the player presses the right arrow
    name_of_move = None; #the name we return
    
    while move_Pressed == False:
        if(keyboard.is_pressed("up")):
            name_of_move = "UP"
            move_Pressed = True
            
        elif(keyboard.is_pressed("down")):
            name_of_move = "DOWN"
            move_Pressed = True
            
        elif(keyboard.is_pressed("left")):
            name_of_move = "LEFT"
            move_Pressed = True
            
        elif(keyboard.is_pressed("right")):
            name_of_move = "RIGHT"
            move_Pressed = True
            
        else:
            continue
            
    return name_of_move


#loops through the objects that we know are in play, and updates each of their location attributes
def update_Objects_():
    for position in _setupStuff.objs_In_Play.keys(): #loops through every object in play
        obj = _setupStuff.objs_In_Play[position] #gets object at the objs_In_Play position
        current_Obj_Location = [obj.row_num, obj.column_num] #gets the location of the object, puts in an array

        removed_key = _setupStuff.objs_In_Play.pop(position, "(in update_All_() function) Error: No Such Position in objs_In_Play array") #gets rid of the old position key in objs_In_Play
        #and sets the removed object at that position to removed_key, or if this position key isnt in objs_In_Play, sets it
        objs_In_Play[f"{current_Obj_Location}"] = obj #stores the object at the object's location

def add_Objects():
    for key in _setupStuff.objs_In_Play.keys():
        row_num, column_num = key.split(",")
        the_Board.map[row_num][column_num] = objs_In_Play[key]

#takes in a 2D array (the map) as input, and returns an array with a random row, random column
def generate_Random_Pos_(twoD_Array):
    max_row_indx = len(twoD_Array) - 1
    rand_row = random.randint(0, max_row_indx)

    max_column_indx = len(rand_row) - 1
    rand_column = random.randint(0, max_column_indx)

    return [rand_row, rand_column]

