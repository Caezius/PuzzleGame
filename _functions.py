def findPlayerPosition(player_repr, level_arr):
    #loop through all coordinates, find which coordinate has the "X", which denotes the player's starting position
    for y in range(len(level_arr)):

        for x in range(len(level_arr[y])):

            space = level_arr[y][x];

            if (space == player_repr):
                return [x, y]


def askForLevel(levels_dict):
    validLevel = False

    while (validLevel == False):
        #get a level number from the user
        level_num = input("Please enter a level number: ");

        #get the level itself using the entered level_num (level_num is a string)

        try:
            selected_level = levels_dict[level_num];
            validLevel = True;

        except KeyError:
            print("\nSorry, that's not a valid level number. \nThese are the current level numbers: ")

            for level_number in levels_dict.keys():
                print(level_number)

    return selected_level

#pretty much the entire asking for input loop in a function-
#asks for a character as an input,
#will either take the first character in the string that is not the representations for the rocks or empty spaces,
#if it does not find a character the user will be asked to enter it again.
def askForAvatar(empty_repr, rock_repr, win_repr):
    avatar = None
    valid_avatar = False

    #while loop to get a valid avatar string from the user
    while (valid_avatar == False):

        entered_string = input(f"please input a single character that is not '{empty_repr}' or '{rock_repr}' or '{win_repr}': ");

        for letter in entered_string:
            if ( (letter != empty_repr) and (letter != rock_repr) and (letter != win_repr) ): #If statement is to avoid making the player look like an empty space or a rock
                avatar = letter; #set the player's avatar to that character
                valid_avatar = True; #this will break the outer while loop
                break; #breaks the inner for loop, stops looking for more valid characters in the string

    return avatar


#ya know, maybe instead of assuming Ive got access to a major variable, I should take it as one of the parameters
#thought I wouldnt need this function, but it appears that the arrays are printed on the same line-so this will print each row on a new line
def showBoard(twoD_Arr):
    for row in twoD_Arr:
        print(row, "\n")

#waits for an arrow  key press, then returns the move name as a string
def getMove():
    import keyboard

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


def generateObjects(repr, sprite, level_arr, object_class):
    #can we pass the object_class as an argument and stil use it to create an object in the local scope?
    assigned_id = 0
    objects_arr = []

    for y in range(len(level_arr)):

        for x in range(len(level_arr[y])):

            if (level_arr[y][x] == repr):
                new_Obj = object_class(id_num = assigned_id, x=x, y=y, sprite = sprite)
                objects_arr.append(new_Obj);
                assigned_id = assigned_id + 1 #increase the assigned id

    return objects_arr

#takes a objects_list and the map_arr, and will first clear the entire board and then add in the objects where they are needed
#edits the array, doesn't return a new copy
def objectsToMap(objects_list, map_arr, empty_repr):
    num_rows = len(map_arr)

    #loop through every position in the map_arr and set it to the empty_repr, essentially clearing the ENTIRE board
    for row in range(num_rows):
        current_row = map_arr[row]

        for column in range(len(current_row)):
            map_arr[row][column] = empty_repr

    #for each object, take it's x and Y values, and then set that location in the map array to an the representation for an object
    for each_object in objects_list:

        obj_row = each_object.y
        obj_column = each_object.x

        #set that position to have the representation for the object
        map_arr[obj_row][obj_column] = each_object.sprite

    return map_arr #return the map array with the new object representations in it

#takes in a 2D array (the map) as input, and returns an array with a random row, random column
def generate_Random_Pos_(twoD_Array):
    max_row_indx = len(twoD_Array) - 1
    rand_row = random.randint(0, max_row_indx)

    max_column_indx = len(rand_row) - 1
    rand_column = random.randint(0, max_column_indx)

    return [rand_row, rand_column]
