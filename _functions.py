#import matplotlib as plt
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
    
#waits for an arrow  key press, then returns the move name as a string
def checkForMove(playerObj):
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


def generateObjects(obj_repr, level_arr, objects_holder):
    assigned_id = 0
    
    for y in range(level_arr.length):
        
        for x in range(level_arr[y].length):
            
            if (level_arr[y][x] == object_repr):
                new_rockObj = Rock(id = assigned_id, x=x, y=y, repr = object_repr)
                objects_holder.append(new_rockObj);
                assigned_id = assigned_id + 1 #increase the assigned id
                
                
#takes a objects_list and the map_arr, and will first clear the entire board and then add in the objects where they are needed    
#edits the array, doesn't return a new copy
def objectsToList(empty_repr, obj_repr, objects_list, map_arr):
    num_rows = map_arr.length
    
    #loop through every position in the map_arr and set it to the empty_repr, essentially clearing the ENTIRE board
    for row in range(num_rows):
        current_row = map_arr[row]
        
        for column in range(current_row.length):
            map_arr[row][column] = empty_repr
    
    #for each object, take it's x and Y values, and then set that location in the map array to an the representation for an object
    for each_object in objects_list:
        
        obj_row = each_object.y
        obj_column = each_object.x 
        
        #set that position to have the representation for the object 
        map_arr[obj_row][obj_column] = obj_repr

    
#takes in a 2D array (the map) as input, and returns an array with a random row, random column
def generate_Random_Pos_(twoD_Array):
    max_row_indx = len(twoD_Array) - 1
    rand_row = random.randint(0, max_row_indx)

    max_column_indx = len(rand_row) - 1
    rand_column = random.randint(0, max_column_indx)

    return [rand_row, rand_column]




