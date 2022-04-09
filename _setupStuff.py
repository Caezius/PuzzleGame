class Map:
    def __init__(self, level_array, empty_repr):
        self.map = level_array
        self.empty_repr = empty_repr #empty_repr is the character in a level array that represents and empty space - " " (whitespace) should be the empty_repr, but it could also be changed.
        
    #when the map object is printed, it should print its "map" attribute, the array inside of it.
    def __repr__(self):
        return str(self.map)

    def get_Columns_(self):
        cols_in_each_row = []
        row_index = 0
        for row in self.map:
            cols_in_each_row.append(len(row))
        return cols_in_each_row

    
    

    #should return a "yes." string if a new position is valid, either with a move and then will test a push
    #otherwise, should return a string containing the issue with the move. ("Out of bounds", "Rock is blocking the way", etc.)
    def validMove(self_x, self_y, move_name):
        #determine what space the object is trying to go to using the move name.
        desired_x = self_x
        desired_y = self_y
        
        if(move_name == "UP"){
            desired_y = self_y - 1;
            push_spot = [self_x, self_y - 2]; #set the spot that, if this is a push move, we can check if it's valid using the moved position.
            
        elif (move_name == "DOWN"):
            desired_y = self_y + 1;
            push_spot = [self_x, self_y + 2];
        
        elif (move_name == "LEFT"):
            desired_x = self_x - 1;
            push_spot = [self_x - 2, self_y];
        
        elif(move_name == "RIGHT"):
            desired_x = self_x + 1;
            push_spot = [self_x + 2, self_y];
            
        else:
            return "something went wrong. Invalid move passed to validMove() function. Should be \"UP\", \"DOWN\", \"LEFT\" or \"RIGHT\". "

        num_columns = self.map[desired_y].length
        num_rows = self.map.length
            
            
        #CHECKING THE DIFFERENT VALID/INVALID MOVES  ⬇️   
        #Strategy: check all the bad conditions first, then all the good ones. Increases chance we'll catch something bad before allowing it.
          
            
        #if either the x or y is too great or too small (ie, if the move will move the player out of bounds) then return a "no"
        if (desired_x < 0 or desired_y < 0):
            return "out of bounds."
        elif (desired_x >= num_columns or desired_y >= num_rows):
            return "out of bounds."
        else: 
            continue;      
             
        push_x = push_spot[0];
        push_y = push_spot[1];
                
        #first, check if there is an empty space at the desired spot-if so, that's an INSTANT valid
        if (self.map[desired_y][desired_x] == empty_repr):
            return "yes.";     
            
        #now we know that space in front of the player is NOT an empty space. So it can either be no space (the user trying to move past the edge of the map),
        #or can be a block BLOCK-ing the way 😏
            
        #next, check if this can be a push move. So we'll check if there is an empty square one square up/down/left/right past the desired position.
            
        #if the push position is out of bounds, that's an invalid since we already checked that there wasnt an empty space right next to the object. 
        #So the player can't move forward,
        #and there's not an empty space beyond the obstructing block to push it.   
            
        elif ((push_x >= num_columns or push_y >= num_rows)  or (push_x < 0 or push_y < 0):
            return "no. There is no space for the block to be pushed to."
        
        #if the push position is in bounds, then check if there is a block there.  If there is another block beyond, we can't push.         
        elif (self.map[push_y][push_x] != empty_repr):
            return "no. There is another block behind your immediate block, so you can't push that block.";
            
        else:    
            return "yes."
              
        
           
        
        
    
        
         

global puzzle_Board
puzzle_Board = Map ([
 #an array representing all the spaces of the grid, will be edited by nearly every Class, method_, or function_
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
])

#<a few days later> *Realizes* Its probably a better idea to put the most important variables in the main file,
#because if each time you use something its an instance from an imported file,
#different calls could be editing different variables in the systems memory, as each time the import _module.object will just give a new copy of the object
#so Its better to just have your variable defined in the main, so it will always be kept track of and accessible to all the functions you use in that main

#this function returns the number of columns in each row of puzzle_Board, in a 1D array


#maybe we should have a dictionary containing all of the pieces, with the location as their key
#"row_num, col_num": PuzzlePiece("Some colour")
#and then we can just go through each item, get the value it holds, and split its key so we know where to put that value in the array

#a dictionary containing every obj added to the grid,
#will get added to for new players, deleted from for cleared pieces,
#and should get all items compleyely deleted (reset_Board_()) when we reset the board for a new game/round
objs_In_Play = {
}

display_list = [
""" [(R, G, B), (R, G, B)],
    [(R, G, B), (R, G, B)],
    [(R, G, B), (R, G, B)] """
] #holds RBG values that will get displayed
