#import matplotlib as plt
import _setupStuff
from _setupStuff import puzzle_Board as the_Board
import _gameClasses
import keyboard

#ya know, maybe instead of assuming Ive got access to a major variable, I should take it as one of the parameters
def do_A_Turn_(playerObj):
    show_Board_(the_Board.map)

    check_For_Player_Move_(playerObj)
    reset_Board_(the_Board.map) #after the player moves, reset the board then-
    add_Objects(the_Board.map, _setupStuff.objs_In_Play) #add the new objects

    show_Board_(the_Board.map)

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


def check_For_Player_Move_(playerObj):
    print("Press an arrow key to move")

    move_Pressed = False #var we make to see if the player has made a move, turns true when the player presses the right arrow
    while move_Pressed == False :
        if(keyboard.is_pressed("up")):
            playerObj.p_Move_Up_
            move_Pressed = True
        elif(keyboard.is_pressed("down")):
            playerObj.p_Move_Down_
            move_Pressed = True
        elif(keyboard.is_pressed("left")):
            playerObj.p_Move_Left_
            move_Pressed = True
        elif(keyboard.is_pressed("right")):
            playerObj.p_Move_Right_
            move_Pressed = True
        else:
            continue

#Note to self: add try and except catches if the obj doesnt have the colNum or rowNum attributes
#also, these functions will act on objects of the PuzzlePiece class, (with player piece having the go_Direction method)
#and all depend on the obj to have the current_location attribute

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


#all these following functions are the ones that modify either the row_num or col_num

def move_Piece_(puzzlePieceObj, direction):
    if (direction == "up"):
        move_Up_(puzzlePieceObj)
    elif (direction == "down"):
        move_Down_(puzzlePieceObj)
    elif (direction == "left"):
        move_Left_(puzzlePieceObj);
    elif (direction == "right"):
        move_Right_(puzzlePieceObj)
    else:
        print("oop, move_Piece didnt get a direction, somethings not allright mate")

def move_Up_(puzzlePieceObj):
    up_row = puzzlePieceObj.row_num - 1
    if(up_row >= 0):
        puzzlePieceObj.row_num = up_row

def move_Down_(gameObj):
    down_row = gameObj.row_num + 1
    if (down_row < len(_setupStuff.puzzle_Board)): #checks if moving down would still be within the rows
        gameObj.row_num = down_row

def move_Left_(gameObj):
    west_column = obj.column_num - 1
    if (west_column >= 0): #checks if the westward column would greater than
        obj.col_num = west_column

def move_Right_(gameObj):
    east_column = obj.column_num + 1
    current_row = obj.row_num

    if (east_column < len(the_Board.map[current_row]) ):
        #checks if the east column is still in the range of the entire row
        #we dont want to move out beyond the row's range, so this if statement will prevent that
        #(a row with 5 spaces only has 0 up to 4), a row of 6, 0-5, a row of 2, 0-1, and so on
        if (f"{current_row}, {east_column}" not in _setupStuff.puzzle_Board.keys() ):
            obj.column_num = east_column
        else:
            print("there is an object where you wish to go")


def get_Obj_At_(coordinates_arr):
    """This function takes an array with two values,
    [rowNumber, columnNumber] and returns a pointer to the object at the
    Map[rowNumber][colNumber]"""

    row = coordinates_arr[0]
    column = coordinates_arr[1]
    objKey = f"{row}, {column}"
    if (objKey in _setupStuff.objs_In_Play.keys()):
        obj = _setupStuff.objs_In_Play[objKey]
        return obj
    else:
        print("There is no object at the given coordinates")
        return None
    #objPointer = &Map[row][column]
    #return objPointer #uh, so newsflash-python...isnt a pointer language.
