from _setupStuff import levels, rock_sprite, empty_sprite, win_sprite, Map, ObjectsHolder

from _gameClasses import Player, Rock, GameObject

from _functions import askForLevel, askForAvatar, generateObjects, objectsToMap, findPlayerPosition, getMove, showBoard

import time
#move = getMove()
#print(move);


print("Welcome to the Puzzle Game.");


#get levels and create the map object and the Objects_in_play object ⬇️

selected_level = askForLevel(levels)

#create the Puzzle board, which is a map object so we can run methods on it to search itself.
Puzzle_board = Map(selected_level["array"], empty_sprite);

#create an array of objects, then assign that array to an ObjectsHolder object so we can run methods on that array.
array_of_objects = generateObjects(repr = selected_level["rock_representation"], sprite = rock_sprite, level_arr = Puzzle_board.map, object_class = Rock);
Objects_in_play = ObjectsHolder()
Objects_in_play.arr = array_of_objects

win_element = generateObjects(repr = selected_level["win_representation"], sprite = win_sprite, level_arr = Puzzle_board.map, object_class = GameObject)
win_element = win_element[0]

Objects_in_play.arr.append(win_element)
#get the character's avatar ⬇️

print("please enter a letter or one character (Ex: '%' or '+') to represent your player.");


player_sprite = askForAvatar(empty_sprite, rock_sprite, win_sprite);

player_x_pos, player_y_pos = findPlayerPosition(selected_level["player_representation"], selected_level["array"]);

player = Player(sprite = player_sprite, id_num = player_sprite, x = player_x_pos, y = player_y_pos);

#add the player to the Objects_in_play array
Objects_in_play.arr.append(player);

new_map = objectsToMap(Objects_in_play.arr, Puzzle_board.map, empty_sprite)
#set the Puzzle_board.map to the updated map
Puzzle_board.map = new_map



moves_left = 6;
continueGame = True;

print("\nGood Day. Your mission: get that fat 'W'. \nMove into blocks to push them around. \nBut be careful. \nYou have limited moves, and wrong moves will still cost you as well.\n")
while (continueGame == True):

    #print the puzzle board at the START of each turn
    showBoard(Puzzle_board.map)
    print("moves left:", moves_left)
    #getMove() asks for a move from the user, ni the form of a key press
    move_name = getMove();

    player_index = Objects_in_play.getIndexOfObj(obj_id = player_sprite)
    player_x = Objects_in_play.arr[player_index].x;
    player_y = Objects_in_play.arr[player_index].y

    move_message = Puzzle_board.validMove(player_x, player_y, move_name)

    if (move_message == "WIN"):
        print("\nAYYY YOU GOT THAT W!!!!!!!!!!!!!!!\n")
        Puzzle_board.map[player_y][player_x] = empty_sprite #clear the player's last position off the board.
        Puzzle_board.map[win_element.y][win_element.x] = player_sprite #replace where the win sprite is with the player sprite in the printed array
        break;

    elif (move_message == "yes." or move_message == "push."):
        player_indx = Objects_in_play.getIndexOfObj(player_sprite)
        #changes the player's coordinates, and the piece's coordinates (if needed)
        Objects_in_play.arr[player_indx].move(move_name, Puzzle_board, Objects_in_play);

    else:
        #validMove() checks the objects, the player's new position after they move, and returns the string "yes" if it is a valid move, or returns a warning message to the user.
        #so if the returned value was not "yes", then we'll just print out the error message that was returned instead.
        print(move_message);

    new_map = objectsToMap(Objects_in_play.arr, Puzzle_board.map, empty_sprite)
    #set the Puzzle_board.map to the updated map
    Puzzle_board.map = new_map

    moves_left = moves_left - 1;
    if (moves_left <= 0):
        continueGame = False

    time.sleep(1)


showBoard(Puzzle_board.map)
print("End of game.")
