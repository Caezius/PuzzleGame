class GameObject:
    #the init takes a symbol,
            #which is a char that will be printed in the grid to show the player's location
    def __init__(self, sprite, id_num, x, y):
        self.sprite = sprite
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
                push_pos = [self.x, new_y - 1]

            elif (direction == "DOWN"):
                new_y = self.y + 1 #sets the y position to one row down from the obj's current row
                push_pos = [self.x, new_y + 1]

            elif (direction == "LEFT"):
                new_x = self.x - 1
                push_pos = [new_x - 1, self.y]


            elif (direction == "RIGHT"):
                new_x = self.x + 1
                push_pos = [new_x + 1, self.y]


            #next, use the validMove() method to see if that is a valid move.
            validity = mapObj.validMove(self.x, self.y, direction);

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

                #alternatively to findObjAndSet, we could use this statement:
                #index = objs_arr.getIndexOfObjAt(new_x, new_y)
                #objs_arr[index].move(direction) #move the affected piece in the direction the player was going
                #We'll use the other one to avoid running this move twice and moving multiple objects and having to check their neighbors for each one.
                #We already checked if the push_pos was empty in this move function
                #and checking the pushed object's neighbors may cause errors if the object's new location will be at the edge of the map.
                #That will mean push_pos will be off the map, though it shouldn't matter because this move function should check if there is an empty space right next to the object first...
                #Well, this way we can avoid recursion, if there is an error and it happens to somehow push another object,.
                #Then we'll have to call move again and I don't like the idea of even possible recursion. So we'll just set it like this-though I should have faith/actually check my code to confirm if this error is possible.

            else:
                print("something went wrong with checking the move's validity.")
                return -1;

    def __repr__():
        return self.sprite


class Rock(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);

class Player(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);

class WinElement(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite = sprite, id_num = "WIN", x = x, y = y)

#function that checks if a certain position has a win object
def checkForWin(objects_arr, x, y):
    for object in objects_arr:

        if (object.x == x and object.y == y and object.id_num == "WIN"):
            return True;


                self.setPosition(new_x, new_y);

            elif (validity == "push."):

                #If we need to push an object aside from the current player,
                #we'll use the findObjAndSet() method on the objects array that gets a location,
                #looks through itself to see which object has that location,
                #and then changes that object's x and y to a new x and y.
                objs_arr.findObjAndSet(new_x, new_y, push_pos[0], push_pos[1])

                #alternatively to findObjAndSet, we could use this statement:
                #index = objs_arr.getIndexOfObjAt(new_x, new_y)
                #objs_arr[index].move(direction) #move the affected piece in the direction the player was going
                #We'll use the other one to avoid running this move twice and moving multiple objects and having to check their neighbors for each one.
                #We already checked if the push_pos was empty in this move function
                #and checking the pushed object's neighbors may cause errors if the object's new location will be at the edge of the map.
                #That will mean push_pos will be off the map, though it shouldn't matter because this move function should check if there is an empty space right next to the object first...
                #Well, this way we can avoid recursion, if there is an error and it happens to somehow push another object,.
                #Then we'll have to call move again and I don't like the idea of even possible recursion. So we'll just set it like this-though I should have faith/actually check my code to confirm if this error is possible.
            else:
                print("something went wrong with checking the move's validity.")
                return -1;

    def __repr__():
        return self.sprite


class Rock(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);

class Player(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);


            elif (validity == "push."):

                #If we need to push an object aside from the current player,
                #we'll use the findObjAndSet() method on the objects array that gets a location,
                #looks through itself to see which object has that location,
                #and then changes that object's x and y to a new x and y.
                objs_arr.findObjAndSet(new_x, new_y, push_pos[0], push_pos[1])

                #alternatively to findObjAndSet, we could use this statement:
                #index = objs_arr.getIndexOfObjAt(new_x, new_y)
                #objs_arr[index].move(direction) #move the affected piece in the direction the player was going
                #We'll use the other one to avoid running this move twice and moving multiple objects and having to check their neighbors for each one.
                #We already checked if the push_pos was empty in this move function
                #and checking the pushed object's neighbors may cause errors if the object's new location will be at the edge of the map.
                #That will mean push_pos will be off the map, though it shouldn't matter because this move function should check if there is an empty space right next to the object first...
                #Well, this way we can avoid recursion, if there is an error and it happens to somehow push another object,.
                #Then we'll have to call move again and I don't like the idea of even possible recursion. So we'll just set it like this-though I should have faith/actually check my code to confirm if this error is possible. 


    def __repr__():
        return self.sprite


class Rock(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);

class Player(GameObject):
    def __init__(self, sprite, id_num, x, y):
        GameObject.__init__(self, sprite, id_num, x, y);
