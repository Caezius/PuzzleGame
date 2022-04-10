4-10/2022 edits:
1. created a player_repr variable in _setupStuff
2. figured I should just tell the user what characters not to enter at first, and keep telling them that if it's still wrong.
This is Instead of having an awkward if statement at the end that checks the same condition as the outer while loop. Instead of excluding the printing it in the first run, tell them in that first run as well as the following runs. Makes sense too-they'd pretty much be getting penalized for not following a rule they weren't told.
3. Put for loop into a function (in _functions.py_ )and fixed bug where the avatar would get set to the first character in the entered string
4. Fixed logic error of "player.move()". player.move() was accessing a variable *set* to the Player() object instead of the Player() object in the Objects_in_play array.
5. Changed bug where validMove() was used as a standalone function instead of Puzzle_board's method
6. Set the string returned by the aforemetioned validMove() to a variable, and replaced the calls to validMove() with that variable ("move_message") to increase readability. And so the ~~function~~ method is not run multiple times.
7. Coded in a code that sets the Map to the new, updated map every turn.
8. Wrote in code to print the map each turn.
9. Looks like I misremembered how to get length of arrays in Python - ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) moment. It's not list.length, it's using the len(list) function. also written differntly-len instead of lenght. ...Well, nothing a good Ctrl-F session can't fix...amirrite? Ah, turns out there were only 8 in the entire directory-I think I may have been coding this too long, feels like there should be closer to 36.4...
10. validMove(move_name) on the method "validMove(self_x, self_y, move_name)" produces the error "move_name" missing because self_x is assumed to be the object's "self" argument, the "move_name" we pass is then assumed to be self_y, leaving only move_name not given. We also need to go back and add the self argument to all our methods.
11. Fixed many a various syntax issues


"""
setup: should make a puzzle board array containing the starting board with the puzzle piece objects needed,
while startGame == True:
do_A_Turn_()
    -asks player to input a move using ask_For_Move_(), then
    runs move_Player_() to moves the player based on which key they press, and move_Player will have a couple if statements to test each direction,
       and will then run a player.move_[Direction]_ function based on which key they pressed
    
Then it should display_Board_(), which gets the puzzle_Board array but prints it as a plt.matshow matrix because f a n c y

Player class: Represents the player, has methods such as push_PuzzlePiece_() and

PuzzlePiece class: also has a location attribute [row_num, col_num], and also can be acted upon by the Player object

"""
