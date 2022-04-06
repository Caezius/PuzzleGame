print("Welcome to the Puzzle Game.");
level_1 = [
    [" ", " ", "W"],
    ["O", "O", " "],
    ["X", "O", " "]
]

levels = {
    "1": level_1
    
}

#character representing the Rock() objects
rock_repr = "O";

#get a level number from the user
level_num = input("Please enter a level number: ");

#get the level itself using the entered level_num
selected_level = levels[level_num];

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

#loop through all coordinates, find which coordinate has the "X", which denotes the player's starting position
for y in range(selected_level.length):
    for x in range(selected_level[y]):
        position = selected_level[y][x];
        if (position == "X"):
            player_x_pos, player_y_pos = x, y;
            
player = Player(sprite = player_avatar, id = player_avatar, x = player_x_pos, y = player_y_pos);
objects_in_Play.add(player);

while (endGame = False):
    #getMove() asks for a move from the user
    move = getMove();
    if (validMove(move) == "yes"):
        #changes the player's coordinates, and the piece's coordinates (if needed)
        moveObjects(move);
    else:
        #validMove() checks the objects, the player's new position after they move, and returns the string "yes" if it is a valid move, or returns a warning message to the user.
        #so if the returned value was not "yes", then we'll just print out the error message that was returned instead.
        print(validMove(move));
        
        
    
    

