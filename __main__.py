from _setupStuff import levels, rock_repr, empty_repr, Map

print("Welcome to the Puzzle Game.");


#get a level number from the user
level_num = input("Please enter a level number: ");

#get the level itself using the entered level_num
selected_level = levels[level_num];

#create the Puzzle board, which is a map object so we can run methods on it to search itself.
Puzzle_board = Map(selected_level, empty_repr);

array_of_objects = generateObjects(Puzzle_board.map);
Objects_in_play = ObjectHolder(array_of_objects)


print("please enter a letter or one character (Ex: '%' or '+') to represent your player.");

#boolean value to check if the user's avatar is legit (as in, a single character that is not a whitespace and is not the same as the rock_repr string.
valid_avatar = False; 

#while loop to get a valid avatar string from the user
while (valid_avatar == False):
    
    entered_string = input("please input a single character: ");

    for letter in entered_string:
        if ( (letter != " ") and (letter != rock_repr) ): #If statement is to avoid making the player look like an empty space (" ") or the representation for a Rock object ("O")
            player_avatar = entered_string[0]; #set the player's avatar to that character.
            valid_avatar = True; #breaks the outer while loop
            break; #stops looking for valid characters in the string.
    
    #if the avatar is still not valid, print a warning message.
    if (valid_avatar == False):
        print("Please re-enter a single, non-whitespace character-or a string that does not start with whitespace.");
        

player_position = None;

player_x_pos, player_y_pos = findPlayerPosition(selected_level);
            
player = Player(sprite = player_avatar, id = player_avatar, x = player_x_pos, y = player_y_pos);
objects_in_Play.add(player);

while (endGame = False):
    #getMove() asks for a move from the user, ni the form of a key press
    move_name = getMove();
    
    if (Puzzle_board.validMove(move_name) == "yes." or Puzzle_board.validMove(move_name) == "push."):
        #changes the player's coordinates, and the piece's coordinates (if needed)
        player.move(move_name, Puzzle_board, Objects_in_play);
        
    else:
        #validMove() checks the objects, the player's new position after they move, and returns the string "yes" if it is a valid move, or returns a warning message to the user.
        #so if the returned value was not "yes", then we'll just print out the error message that was returned instead.
        print(validMove(move_name));
        
