import _setupStuff
import random

class GameObjectClass:
    def update_Location_(self):
        self.location = [self.row_num, self.column_num]
    def set_Position_(self, row, column):
        self.row_num = row
        self.column_num = column
        self.location = [row, column]


    class  PuzzlePieceClass:
        def __init__(self, color, location = [0, 0]):
           self.color = color #type: string, such as "blue" or "purple"
           self.location = location #<- [row_Num, column_num] (both starting from 0)

           self.row_num = self.location[0]
           self.column_num = self.location[1]

           symbol = ""

        #if we use the self (which is the obj itself) and put .color,
        #it should equal the color var we used to intalize the puzzlePiece obj
        def __repr__():
            return self.color

    class PlayerClass:
        def __init__(self, symbol, **spawn_location): #the init takes a symbol,
            #which is a char that will be printed in the grid to show the player's location
            print(spawn_location)
            spawn_location = spawn_location["spawn_location"]
            self.spawn_location = spawn_location #an Array with the player's starting [row_Num, column_num] in the gird
            #the location will change,
            #but when the player is first intalized the player's location is equal to the spawnLocation given
            #<a few days later> HOWEVER, dont make the mistake I did and put self.location = spawn_location-becauses that will make self.location always spawn location,
            #and it also WONT create a variable called "location"
            location = spawn_location
            self.location = location

            row_num = spawn_location[0]
            self.row_num = row_num

            column_num = spawn_location[1]
            self.column_num = column_num


        def randomly_Set_Location_(self):
            #note that randint includes both the bottom AND upper number, so we need to subtract one from
            #the rows/columns number so the included upper number won't be greater than the possible indexes
            shortest_row_len = min(_setupStuff.puzzle_Board.get_Columns_())
            rand_column = random.randint(0,  shortest_row_len - 1  ) #defines that the col number should be in between zero and the least number of columns
            self.column_num = rand_column

            rand_row = random.randint(0, len(_setupStuff.puzzle_Board.get_Columns_()) - 1)
            self.row_num = rand_row


        def push_PuzzlePiece_(self, direction):
            #NOTE: this function uses West, East, Up, and Down
            # instead of Left, Right, Up and Down
            row_num = self.row_num
            column_num = self.column_num

            if (direction == "UP"):
                up_coordinates = [row_num - 1, column_num]

            elif (direction == "DOWN"):
                new_row = self.row_num + 1 #sets the newRow to one row down from the obj's current row
                down_coordinates = [new_row, column_num]

            elif (direction == "LEFT"):
                west_coordinates = [row_num, column_num - 1]

                if(the_Board.map[west_coordinates] == "■"): #checks if there is a puzzlePiece to the left
                #if there is a square to the left, then we need to move the square
                    west_pc_coordinates = get_Obj_At_(the_Board.map[west_coordinates])
                else:
                    print("there is not a puzzle piece east of you")

            elif (direction == "RIGHT"):
                east_coordinates = [row_num, column_num + 1]

                if (type(  ) == PuzzlePiece): #checks if the obj at the east sqace is a puzzlePiece obj
                    east_piece = get_Obj_At_(the_Board.map[east_coordinates])

                    if (east_piece.column_num + 1 == " "): #checks if the eastpiece can be moved east
                        east_piece.location = east_coordinates
                    else:
                        print("Piece cannot be moved east")

                else:
                     print("Err: There is not a puzzle piece east of you to push")

            else:
                print("invalid move direction")



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
