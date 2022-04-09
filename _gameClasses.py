class GameObject:
    #the init takes a symbol,
            #which is a char that will be printed in the grid to show the player's location
    def __init__(self, map_repr, id_num, x, y):
        self.map_repr = map_repr
        self.id = id_num
        self.x = x
        self.y = y
               
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        

    #changes the piece's position
    def move(self, direction, mapObj, objs_arr):
            #NOTE: this function uses West, East, Up, and Down
            # instead of Left, Right, Up and Dow
            
            new_x = self.x
            new_y = self.y

            if (direction == "UP"):
                new_y = self.y - 1
                push_pos = [self.x, new_y]

            elif (direction == "DOWN"):
                new_y = self.y + 1 #sets the y position to one row down from the obj's current row
                push_pos = self.x, new_y

            elif (direction == "LEFT"):
                new_x = self.x - 1


            elif (direction == "RIGHT"):
                new_x - self.x + 1
                
            #next, use the validMove() method to see if that is a valid move.
            validity = mapObj.validMove(self.x, self.y, direction)
            
            #if it returns the confirmation string, then we can go ahead and set it to the new position
            #but we should be able to distinguish between valid because of a push() move and valid because it's a regular move. 
            #We'll have to run different functions based on which type of effect the move has.
            if (validity == "yes."):
                
                self.setPosition(new_x, new_y);
                
            elif (validity == "push."):
                             
                #If we need to push an object aside from the current player,
                #we'll use the findObjAndSet() method on the objects array that gets a location,
                #looks through itself to see which object has that location, 
                #and then changes that object's x and y to a new x and y. 
                objs_arr.findObjAndSet(new_x, new_y, push_pos[0], push_pos[1])               
                
    
    def __repr__():
        return self.map_repr


class Rock(GameObject):
    def __init__(self, map_repr, id_num, x, y):
        GameObject.__init__(self, map_repr, id_num, x, y);
    
    
class PlayerClass(GameObject):
    def __init__(self, map_repr, id_num, x, y):
        GameObject.__init__(self, map_repr, id_num, x, y);
        
               
