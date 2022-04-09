import _setupStuff
import random

class GameObject:
    #the init takes a symbol,
            #which is a char that will be printed in the grid to show the player's location
    def __init__(self, map_repr, id_num, x, y):
        self.map_repr = map_repr
        self.id = id_num
        self.x = x
        self.y = y
               
    def setPosition(self, row, column):
        self.x = column
        self.y = row
        
    #[IN PROGRESS]
    #should return a "yes" string if a new position is valid, either with a move and then will test a push
    #otherwise, should return a string containing the issue with the move. ("Out of bounds", "Rock is blocking the way", etc.)
    def validMove(desired_x, desired_y):
        new_column = self.column_num;
        new_row = self.row_num;
        
        #first, check if there is an empty space at the spot-if so, that's an INSTANT valid
        if (objects
         
        

    #changes the piece's position
    def move(self, direction):
            #NOTE: this function uses West, East, Up, and Down
            # instead of Left, Right, Up and Down
            current_row = self.row_num
            current_column = self.column_num
            
            new_column = current_column 
            new_row = current_row

            if (direction == "UP"):
                new_row = current_row - 1

            elif (direction == "DOWN"):
                new_row = self.row_num + 1 #sets the newRow to one row down from the obj's current row
                

            elif (direction == "LEFT"):
                new_column = self.column_num - 1


            elif (direction == "RIGHT"):

                new_column - self.column_num + 1
                
           



    class  Rock:
        def __repr__():
            return self.color

    class PlayerClass:
  
        def randomly_Set_Location_(self):
            #note that randint includes both the bottom AND upper number, so we need to subtract one from
            #the rows/columns number so the included upper number won't be greater than the possible indexes
            
            rows = _setupStuff.puzzle_Board.get_Rows_()
            shortest_row_len = min(rows)
            rand_row = random.randint(0, len(_setupStuff.puzzle_Board.get_Columns_()) - 1)
            self.row_num = rand_row
            
            rand_column = random.randint(0,  shortest_row_len - 1) #defines that the col number should be in between zero and the least number of columns
            self.column_num = rand_column
            
            


        

        #[ALERT!] these next functions should use an if statement to searche the dictionary,
        #see if there are any objects with the same coordinates as the space they want to move to
        #and then run the self.push_PuzzlePiece_(puzzle_Map[str(east_row + "," + east_col) ] function instead,
        #on the object at the location the dictionarys key gives"""

        def p_Move_Up_(self):
            """moves the player up
               precondition: None
               postcondition: player.row_num is now 1 less, so when printed the player will be on the row 1 above where they were
               postcondition2: PuzzlePiece object right of the player is now moved one more square right (puzzlePieceObj.row_num - 1)
            """
            up_row = self.row_num - 1
            current_column = self.column_num

            #Makes sure there is NOT an object at the location the player wants to move
            if(f"{up_row},{column_num}" not in objs_in_Play.keys()):
                #checks if moving up is still within the rows
                if(up_row >= 0):
                    self.row_num = up_row
                else:
                    print("BigNope: going up would reach the limit")

            #self.push_PuzzlePiece_() runs if there IS an object at the location the player wants to move
            else:
                self.push_PuzzlePiece_("UP")


        def p_Move_Down_(self):
            """moves the player down
               precondition: None
               postcondition: player.row_num is now 1 more, so when printed the player will be on the row 1 below where they were
               postcondition2: PuzzlePiece object below the player is now moved one more square down (puzzlePieceObj.row_num + 1)
            """
            down_row  = self.row_num + 1
            current_column = self.column_num

            #Makes sure there is NOT an object at the location the player wants to move
            if (f"{down_row},{column_num}" not in objs_In_Play.keys()):
                #checks if moving down would still be within the rows
                num_of_rows = len(the_Board.map)
                if (down_row < num_of_rows):
                    self.row_num = down_row
                else:
                    print("BigNope: going down would reach the limit")

            #self.push_PuzzlePiece_() runs if there IS an object at the location the player wants to move
            else:
                self.push_PuzzlePiece_("DOWN")


        def p_Move_Left_(self):
            """moves the player left
               precondition: None
               postcondition: player.column_num is now 1 less, so when printed the player will be on the column left of where they were
               postcondition2: PuzzlePiece object left of the player is now one more square left (puzzlePieceObj.column_num - 1)
            """
            left_column = self.column_num - 1
            current_row = self.row_num

            #Makes sure there is NOT an object at the location the player wants to move
            if (f"{current_row},{left_column}" not in objs_in_Play.keys()):
                #checks if going left is still in bounds
                if (left_column >= 0):
                    self.column_num = left_column
                else:
                    print("BigNope: cannot go anymore to the left")

            #push_Puzzle_Piece_() runs if there IS an object at the location the player wants to move
            else:
                self.push_Puzzle_Piece_("LEFT")


        def p_Move_Right_(self):
            """moves the player right
               precondition: None
               postcondition: player.column_num is now 1 more, so when printed the player will be on the column right of where they were
               postcondition2: PuzzlePiece object right of the player is now one more square right (puzzlePieceObj.column_num + 1)
            """
            right_column = self.column_num + 1
            current_row = self.row_num

            #Makes sure there is NOT an object at the location the player wants to move
            if(f"{current_row},{right_column}" not in objs_in_Play.keys()):
                if (right_column < len(_setupStuff.puzzle_Board.map[current_row]) ):
                    self.right_column_num = right_column
                #checks if the east column is still in the range of the entire row
                #we dont want to move out beyond the row's range, so this if statement will prevent that
                #(a row with 5 spaces only has 0 up to 4), a row of 6, 0-5, a row of 2, 0-1, and so on
                else:
                    print("BigNope: cannot go anymore to the right")

            #push_Puzzle_Piece_() runs if there IS an object at the location the player wants to move
            else:
                self.push_PuzzlePiece_("RIGHT")
