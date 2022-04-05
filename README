# Text-based Puzzle-Game
A puzzle game similar to the one with sharply dressed waifus by Vanripper!
Uses text and arrays to display the visuals. 

General structure:

1. The user selects a level by inputting a number (the level number).
2. The level is found in an array of levels, and generateObjects(level_array) is run.
3. for(): each index in the level_array array, if there should be an object at that index/coordinate, a Rock() object is initialized, with x and y attributes. The x attribute will be set to the column the coordinate is in, and the y position set to the row the coordinate is in. Then the Rock() object is also assigned a value to its Id attribute, and then the object is added to the objects_in_Play array.
4. The level_array itself is then printed to the screen. 

6. The user is then prompted to input a character to represent their avatar. If more than one character is put in, the first non-whitespace character entered will be used as the user's avatar.
7. A Player() object is initialized, using the entered character as a constructor.
8. The Player() object is given the x and y positions associated with the level.
9. The user's Id attribute will be set to their avatar string instead of a number. This helps to distinguish the player from the rest of the Rock()s later.

10. The function synthesizeMap(objects_in_Play); is run. 
11. The returned Value is printed to the screen.

12. The game starts. While the user does not enter the sentinel (the string "quit") the program will:
13. Take a move from the user-either the arrow presses on the keyboard, W/A/S/D, or the words "up", "down", "left", "right" (not case sensitive)
14. Determine 
  1. If the move is valid (the new location's x and y values do not not exceed the edges of the map). If not, tell the user that the move is illegal and ask them for input again (restart the while loop).
     Else, 
     1. If there is there another object at the new location. If so, check if there is an empty space one unit after the object, in the direction the user is moving-this will be a push
     2. If there is not an object at the new location, the user will have their objects x or y value updated.
 
 15. Once a valid move has been registered, the function synthesizeMap(objects_in_Play) will be run again


Bonus features:
1. Use matplotlib or some sort of grid library to make the game have polished, colored g r a p h i c s (only a simple grid, however.)


generateObjects(level_array)
: generateObjects(level_array) takes a 2-D array, which represents all the coordinates in the level. The level array represents these positions as strings. For each position there will be a whitespace ("") value for an empty coordinate or an "O" (or some string value) to represent an object being at that position.
