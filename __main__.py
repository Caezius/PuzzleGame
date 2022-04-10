from _setupStuff import levels, rock_repr, empty_repr, player_repr, Map, ObjectsHolder

from _gameClasses import Player, Rock

from _functions import generateObjects, objectsToMap, askForAvatar, findPlayerPosition, getMove


print("Welcome to the Puzzle Game.");


#get levels and create the map object and the Objects_in_play object ⬇️

#get a level number from the user
level_num = input("Please enter a level number: ");

#get the level itself using the entered level_num (level_num is a string)
selected_level = levels[level_num];

#create the Puzzle board, which is a map object so we can run methods on it to search itself.
Puzzle_board = Map(selected_level, empty_repr);

#create an array of objects, then assign that array to an ObjectsHolder object so we can run methods on that array.
array_of_objects = generateObjects(rock_repr, Puzzle_board.map, Rock);
Objects_in_play = ObjectsHolder()
Objects_in_play.arr = array_of_objects




#get the character's avatar ⬇️

print("please enter a letter or one character (Ex: '%' or '+') to represent your player.");

player_avatar = askForAvatar(empty_repr, rock_repr);

player_x_pos, player_y_pos = findPlayerPosition(player_repr, selected_level);

player = Player(sprite = player_avatar, id_num = player_avatar, x = player_x_pos, y = player_y_pos);

#add the player to the Objects_in_play array
Objects_in_play.arr.append(player);

time = 0;
timeout = 60;
#note: replace "time" and "timeout" counter with "endGame" boolean variable
while (time < timeout):
    #getMove() asks for a move from the user, ni the form of a key press
    move_name = getMove();

    player_index = Objects_in_play.getIndexOfObj(obj_id = player_avatar)
    player_x = Objects_in_play.arr[player_index].x;
    player_y = Objects_in_play.arr[player_index].y

    move_message = Puzzle_board.validMove(player_x, player_y, move_name)

    if (move_message == "yes." or move_message == "push."):
        player_indx = Objects_in_play.getIndexOfObj(player_avatar)
        #changes the player's coordinates, and the piece's coordinates (if needed)
        Objects_in_play.arr[player_indx].move(move_name, Puzzle_board, Objects_in_play);

    else:
        #validMove() checks the objects, the player's new position after they move, and returns the string "yes" if it is a valid move, or returns a warning message to the user.
        #so if the returned value was not "yes", then we'll just print out the error message that was returned instead.
        print(move_message);

    new_map = objectsToMap(Objects_in_play.arr, Puzzle_board.map, empty_repr, rock_repr)
    #set the Puzzle_board.map to the updated map
    Puzzle_board.map = new_map

    #print the puzzle board each turn
    print(Puzzle_board)
    time += 1
