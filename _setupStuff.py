class Map:
    def __init__(self, twoD_array):
        self.map = twoD_array
        objects_Dict = {}

    def put_In_Obj(object, old_row, old_column):
       row_num = object.row_num
       column_num = object.column_num
       old_position = f""
       for position in objects_Dict.keys():
           if position == object_position:
               self.map[row_num, column_num] = object

           elif position == old_pos: #if the key is equal to the old
               self.map[old_row][old_column] = " "




    def __repr__(self):
        return str(self.map)

    def get_Columns_(self):
        cols_in_each_row = []
        row_index = 0
        for row in self.map:
            cols_in_each_row.append(len(row))
        return cols_in_each_row


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
