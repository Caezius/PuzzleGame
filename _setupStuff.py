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


class Map:
    def __init__(self, level_array, empty_repr):
        self.map = level_array
        self.empty_repr = empty_repr #empty_repr is the character in a level array that represents and empty space - " " (whitespace) should be the empty_repr, but it could also be changed.
        
    #when the map object is printed, it should print its "map" attribute, the array inside of it.
    def __repr__(self):
        return str(self.map)



    #should return a "yes." string if a new position is valid with a move.
    #will return a "push." if a push needs to happen. 
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
            return "push." #we use "push." instead of "yes." to differentiate between when we need to update the object versus when to update another block
             
