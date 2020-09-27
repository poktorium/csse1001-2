"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{LachlaN Mohr}} ({{s4481974}})"
__email__ = "l.mohr@uqconnect.edu.au"
__date__ = "27/09/2020"

# Write your code here
#display is in a2_support


class GameLogic:
    '''The game logic class
    this class is used to house the bulk of the logic that goes on throughout the game

    Constructed using GameLogic(gameX.txt) where x is what level you would like to play

    '''
    
    
    def __init__(self, dungeon_name="game1.txt"):
        """Constructor of the GameLogic class.

        Parameters:
            dungeon_name (str): The name of the level.
        """
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)
        self._dungeon_name = dungeon_name

        #you need to implement the Player class first.
        self._player = Player(GAME_LEVELS[dungeon_name])

        #you need to implement the init_game_information() method for this.
        self._game_information = self.init_game_information()

        self._win = False
        self.entity_position = {}

   
    def get_positions(self, entity):
        """ Returns a list of tuples containing all positions of a given Entity
             type.

        Parameters:
            entity (str): the id of an entity.

        Returns:
            )list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))

        return positions

    def get_dungeon_size(self):
        '''
        This is a getter method for getting the dungeon size so we don't reference any private attributes (self._dungeon_size) 
        outside of this class.
        It is called using get_dungeon_size().
        '''
        return self._dungeon_size

    def init_game_information(self):
        '''
        This is the constructor for initialising all instances within the game created.
        This method instances each entity and item (e.g. all walls, the key, door, player and moveincrease).
        This should not be called anywhere other than the start of the game.
        It is called using init_game_information() and takes so parameters.
        '''
        positions = []
        objects = []
        
        for i in range(len(self._dungeon)):
            for j in range(len(self._dungeon[i])):
                if self._dungeon[i][j] == PLAYER:
                    self._player.set_position((i, j))
                elif self._dungeon[i][j] == KEY:
                    my_tuple = tuple((i, j))
                    positions.append(my_tuple)
                    objects.append(Key())
                elif self._dungeon[i][j] == DOOR:
                    my_tuple = tuple((i, j))
                    positions.append(my_tuple)
                    objects.append(Door())
                elif self._dungeon[i][j] == WALL:
                    my_tuple = tuple((i, j))
                    positions.append(my_tuple)
                    objects.append(Wall())
                elif self._dungeon[i][j] == MOVE_INCREASE:
                    my_tuple = tuple((i, j))
                    positions.append(my_tuple)
                    objects.append(MoveIncrease())
        return dict(zip(positions, objects))
        '''
        This creates two different lists, one for positions(keys) and objects(values).
        This method uses the zip method to create a dictionary of all instanced entities and their corresponding positions 
        in the form {(position):Entity}.
        '''
            
    def get_player(self):
        '''
        Getter function such that no private attributes are called outside of the class.
        Takes no parameters, so calling it is as simple as get_player().
        '''
        return self._player
    
    def get_game_information(self):
        '''
        Also a getter function. This returns the dictionary created in get_game_information, containing all instanced entities
        and their corresponding positions. 
        Takes no arguments.
        '''
        return self._game_information

    def get_entity(self, position: tuple):
        '''
        This method returns the entity at a given position

        Parameter:
        position <tuple> : the position in which you want to check
        
        Output: outputs the entity at the given position
        '''
        return self.get_game_information().get(position)
    
    def get_entity_in_direction(self, direction: str):
        '''
        get_entity_in_direction is a method used to check what entity is in a specified direction.

        Parameter:
        direction (str): takes the given direction, and adds it to the tuple that is player's position

        Output: returns the entity in the direction
        '''

        player_current_pos = self._player.player_position
        wanted_pos = (player_current_pos[0] + DIRECTIONS.get(direction)[0], player_current_pos[1] + DIRECTIONS.get(direction)[1])
        return self._game_information.get(wanted_pos)
       
    def collision_check(self, direction: str):
        '''
        This function is used to check whether or not the player will collide with something in the given direction.

        Parameter:
        direction (str): The direction in which the player would like to move.

        Output: returns False if there will be no collision, and True if there will be.
        '''
        
        if self.get_entity_in_direction(direction) == None:
            return False
        else:
            return True
        '''
        if self.get_entity_in_direction(direction) == WALL:
            return True
        else:
            return False
        '''

    def new_position(self, direction: str):
        '''
        This method returns the new position of the player given the direction.

        Parameter:
        direction (str): This is the player input direction.

        Output: returns the position that the player would be in depending on their input direction.

        This essentially just adds the different indices of the two tuples and returns the resultant tuple.
        '''
        current_player_pos = self.get_player().player_position
        wanted_pos = (current_player_pos[0] + DIRECTIONS.get(direction)[0], current_player_pos[1] + DIRECTIONS.get(direction)[1])
        return wanted_pos
    
    def move_player(self, direction: str):
        '''
        The move_player function is used to physicall move the player instance throughout the dungeon, updating the Player() entity with the new position.
        
        Parameter:
        direction (str): This is the player defined direction (W, A, S, D)

        Output: this shouldnt output anything, other than updating the players actual position.
        '''
        current_player_pos = self.get_player().player_position
        wanted_pos = (current_player_pos[0] + DIRECTIONS.get(direction)[0], current_player_pos[1] + DIRECTIONS.get(direction)[1])
        self._player.set_position(wanted_pos)
        
    def check_game_over(self):
        '''
        This is a check for determining whether or not the game is over.
        It is dependant on the players move count, if the player has 0 left, the game is over.
        Output: Returns True if the game is over, and False if it isn't
        '''

        if self._player.moves_remaining() == 0:
                return True
        else:
            return False
        
    def set_win(self, win: bool):
        '''
        Sets the win state of the game to a variable called self._win

        Parameter:
        win (bool): Input True if player has won, False if not
        '''
        self._win = win
    
    def won(self):
        '''
        Returns the win variable of the game, reliant on set_win.
        '''
        return self._win

                
class GameApp:
    '''
    This is the GameApp class. This class handles all interaction with the user
    '''

    def __init__(self):
        '''
        constructor for Gameappp
        '''

        pass

    def play(self):
        '''
        This is where the user interacts with the game.
        Acts as a communicator for the GameLogic and Display
        '''
        invest_dict = []                  
        for key in DIRECTIONS:
            invest_dict.append(INVESTIGATE + ' ' + key)
        
        myGameLogic = GameLogic("game1.txt")

        while myGameLogic.won() == False:
            
            myDisplay = Display(myGameLogic.get_game_information(), myGameLogic.get_dungeon_size())
            myDisplay.display_game(myGameLogic.get_player().player_position)
            print(f'Moves left: {myGameLogic.get_player().moves_remaining()}')
            option = ""
            option = input('\nPlease input an action: ')

            if option not in VALID_ACTIONS and option not in invest_dict:
                print(INVALID)
                       
            if option == HELP:
                print(HELP_MESSAGE)

            if option == QUIT:
                quit_input = input("Are you sure you want to quit? (y/n): ")
                if quit_input == "y":
                    break
                elif quit_input == "n":
                    pass

            if option in invest_dict:
                if(myGameLogic.collision_check(option[-1]) == True):
                    new_pos = myGameLogic.new_position(option[-1])
                    print(f'{myGameLogic.get_game_information().get(new_pos).__str__()} is on the {option[-1]} side')
                myGameLogic.get_player().change_move_count(-1)

            elif option in list(DIRECTIONS.keys()):
                if(myGameLogic.collision_check(option) == False):
                    myGameLogic.move_player(option)

                elif(myGameLogic.collision_check(option) == True):
                    new_pos = myGameLogic.new_position(option)

                    if myGameLogic.get_entity_in_direction(option).get_id() == WALL:
                        print(INVALID)

                    if myGameLogic.get_entity_in_direction(option).get_id() == KEY:
                        '''
                        This gets the instance Key at the position, applying the on_hit method
                        '''
                        myGameLogic.get_game_information().get(new_pos).on_hit(myGameLogic)         
                        myGameLogic.move_player(option)
                        
                    elif myGameLogic.get_entity_in_direction(option).get_id() == MOVE_INCREASE:
                        '''
                        This gets the instanced MoveIncrease at the position, applying the on_hit method
                        '''
                        myGameLogic.get_game_information().get(new_pos).on_hit(myGameLogic)         
                        myGameLogic.move_player(option)
                        
                    elif myGameLogic.get_entity_in_direction(option).get_id() == DOOR:
                        '''
                        This gets the instance Door at the position, applying the on_hit method
                        '''
                        myGameLogic.get_game_information().get(new_pos).on_hit(myGameLogic)  
                        '''
                        This moves the player inside the door, winning the game (if the player has the key)
                        '''       
                        myGameLogic.move_player(option)                                      
                               
 
                myGameLogic.get_player().change_move_count(-1)
                if myGameLogic.check_game_over() == True and myGameLogic.won() == False:
                    print(LOSE_TEST)
                    break

        if myGameLogic.won() == True:
            print(WIN_TEXT)
            

    def draw(self):
        '''
        This is the draw method, this is used to create the array that the player sees
        '''

        myDisplay = Display(GameLogic().get_game_information(), GameLogic().get_dungeon_size())
        myDisplay.display_game(GameLogic()._player.player_position)

                

                
class Entity:
    '''
    This is the superclass for all objects inside the game.
    '''

    def __init__(self):
        '''
        Constructor for the Entity class.
        '''
        self._id = 'Entity'
        self._collidable = True

    def get_id(self):
        '''
        This is a getter method for returning the private attribute that is _id.
        '''
        return self._id
    
    def set_collide(self, collidable):
        '''
        set_collide sets the collision state for the entity

        Parameter:
        collidable (bool): set True if the entity can collide and False if it can not.
        '''
        self._collidable = collidable
        
    def can_collide(self):
        '''
        Returns the collision state of the entity.
        Reliant on set_collide
        '''
        return self._collidable

    def __str__(self):
        return f"Entity('{self._id}')"
    
    def __repr__(self):
        return f"Entity('{self._id}')"


class Player(Entity):
    '''
    This is the player class. It is a subclass of entity.
    '''
    
    def __init__(self, allowed_moves):
        '''
        Constructor of the player class
        '''
        self.inventory = []
        self._allowed_moves = allowed_moves
        self._id = "O"
        self._collidable = True
        self.move_count = 0
        self.player_position = None

    def get_position(self):
        '''
        This is a getter function for returning the position of the player at the current point in the game
        '''
        return self.player_position
         
    def set_position(self, position: tuple):
        '''
        The set_position method is used for setting the position of the player.
        
        Parameter:
        position <tuple>: sets the position of the player at the given tuple coordinates
        '''
        self.player_position = position
        
    def change_move_count(self, number:int):
        '''
        This function is used to change the player's move count.

        Parameter:
        number (integer): increases the move count of the player depending on the number parameter.
        '''
        
        self.move_count += number
        
    def moves_remaining(self):
        '''
        Returns how many moves the player has remaining.
        '''
        moves_remaining = self._allowed_moves + self.move_count
        return moves_remaining
        
    def add_item(self, item):
        '''
        This add_item function allows the user to add an item to their inventory.
        
        Parameter:
        item (str): adds the given item to the player's inventory
        '''
        self.inventory.append(item)
        
    def get_inventory(self):
        '''
        Returns all items inside the player's inventory
        '''
        return self.inventory
        
    def get_id(self):
        '''
        Returns the player id (private attrribute)
        '''
        return self._id

    def set_collidable(self, collidable: bool):
        '''
        Sets the collision state of the player entity.

        Parameter:
        collidable (bool): input True if the player can collide, and False if not
        '''
        self._collidable = collidable
    
    def can_collide(self):
        '''
        Returns the collision state of the player entity
        '''
        return self._collidable
    
    def __str__(self):
        return "Player('O')"

    def __repr__(self):
        return "Player('O')"


class Door(Entity):
    '''
    This is the Door class. It is a subclass of Entity.
    '''

    def __init__(self):
        '''
        Constructor for the door class.
        '''
        self._id = 'D'
        self._name = 'Door'
        self._collidable = True

    def get_id(self):
        '''
        Returns the private variable that is the Door's id.
        '''
        return self._id
    
    def set_collidable(self, collidable = bool):
        '''
        A function for setting the collision state of the door

        Parameter:
        collidable (bool): input True if the door can be collided with and False otherwise.
        '''
        self._collidable = collidable

    def can_collide(self):
        '''
        Returns the collision state of the Door class
        '''
        return self._collidable

    def on_hit(self, game: GameLogic):
        '''
        A function for what happens when the door is collided with. This function checks the player's
        inventory for the key entity. If the key is inside the player's inventory, this sets the win state
        of the game to true. Otherwise, it prints "You don't have the key!"

        Parameter:
        game (GameLogic instance): This is supposed to be an input for the given GameLogic instance
        '''
        inventory_list =  game.get_player().get_inventory()
        if inventory_list == []:
            print("You don't have the key!") 
        else:
            for i in inventory_list:
                if i.get_id() == KEY:
                    game.set_win(win=True)  
         
    def __str__(self):
        return "Door('D')"

    def __repr__(self):
        return "Door('D')"


class Item(Entity):
    '''
    This is a class for the Item entity. It is a subclass of Entity.
    '''

    def __init__(self):
        '''
        Constructor for the Item class
        '''
        self._name = 'Item'
        self._id = 'Entity'
        self._collidable = True

    def get_id(self):
        '''
        Getter function for getting the id of the Item class
        '''
        return self._id

    def get_name(self):
        '''
        Getter function for returning the name of the Item class
        '''
        return self._name
    
    def set_collide(self, collidable: bool):
        '''
        This is a function for setting the collision state of the item class

        Parameter:
        collidable (bool): Inputting True will mean the Item can not be collided with, False if it can be
        '''
        self._collidable = collidable

    def can_collide(self):
        '''
        Returns the collision state of the Item class throuh the variable self._collidable
        '''
        return self._collidable

    def on_hit(self, game: GameApp):
        '''
        on_hit class for the subclasses of items
        '''
        raise NotImplementedError

    def __str__(self):
        return f"{self._name}('Entity')"
    
    def __repr__(self):
        return f"{self._name}('Entity')"


class MoveIncrease(Item):
    '''
    MoveIncrease item. This is a subclass of the Item class.
    '''
                            
    def __init__(self, moves = 5):
        '''
        Constructor for the MoveIncrease class. The moves attribute is defaulted to 5.
        '''
        self._id = 'M'
        self._name = 'MoveIncrease'
        self.moves = moves
        self._collidable = True
    
    def get_id(self):
        '''
        Getter function for returning the ID of the MoveIncrease class.
        '''
        return self._id

    def set_collide(self, collidable: bool):
        '''
        Sets the collision state of the MoveIncrease item.

        Parameter:
        collidable (bool): Inputting True will allow the MoveIncrease to be collided with, and False if not.
        '''
        self._collidable = collidable

    def can_collide(self):
        '''
        Returns the collision state of the MoveIncrease item.
        '''
        if self._collidable == True:
            return True
        else:
            return False

    def on_hit(self, game: GameLogic):
        '''
        Defines what to do when the item has been collided with.
        This adds (by default) 5 moves to the overall move count of the player.

        Parameter:
        game (GameLogic instance): The input should be the current instance of GameLogic.
        '''
        reversed_dictionary = {value : key for (key, value) in game.get_game_information().items()}
        position = reversed_dictionary.get(self)
        game._player.change_move_count(self.moves)
        game.get_game_information().pop(position)
        
    def __str__(self):
        return f"{self._name}('{self.get_id()}')"
    
    def __repr__(self):
        return f"{self._name}('{self.get_id()}')"


class Wall(Entity):
    '''
    This is the Wall entity. It is a subclass of the Entity class.
    '''
    
    def __init__(self):
        '''
        Constructor for the Wall entity class.
        '''
        self._id = '#'
        self._name = "Wall"
        self._collidable = False

    def get_name(self):
        '''
        Getter function for returning the name of the Wall class.
        '''
        return self._name
    
    def get_id(self):
        '''
        This is a getter function for returning the ID of the Wall class.
        '''
        return self._id 
    
    def set_collide(self, collidable):
        '''
        Sets the collision state of the Wall class.

        Parameter:
        collidable (bool): Changes the self._collide variable to True if the wall can be collided with and False if not.
        '''
        self._collidable = collidable
            
    def can_collide(self):
        '''
        Returns the collision state (self._collidable) of the Wall class.
        '''
        return self._collidable

    def __str__(self):
        return f"Wall('#')"
    
    def __repr__(self):
        return f"Wall('#')"


class Key(Item):
    '''
    This is the Key item. This is a subclass of Item.
    '''

    def __init__(self):
        '''
        Constructor for the Key class.
        '''
        self._id = 'K'
        self._name = "Key" 
        self._collidable = True

    def get_id(self):
        '''
        Returns the ID of the Key class (private attribute)
        '''
        return self._id
    
    def on_hit(self, game: GameLogic):
        '''
        Decides what to do once the key has been collided with.
        This should be add the key to the players inventory.

        Parameter:
        game (GameLogic instance): This input should be the current GameLogic instance.
        '''
        reversed_dictionary = {value : key for (key, value) in game.get_game_information().items()}
        position = reversed_dictionary.get(self)
        item = game.get_game_information().get(position)
        game.get_player().add_item(item)
        game.get_game_information().pop(position)      
        
    def set_collide(self, collidable: bool):
        '''
        Sets the collision state for the key item.

        Parameter:
        collidable (bool): Inputting True will mean the key can be collided with, and False otherwise
        '''
        self._collidable = collidable

    def can_collide(self):
        '''
        Returns the collision state of the Key class, set in set_collide
        '''
        if self._collidable == True:
            return True
        else:
            return False
    

    def __str__(self):
        return f"{self._name}('{self.get_id()}')"
    
    def __repr__(self):
        return f"{self._name}('{self.get_id()}')"


def main():
    myGameApp = GameApp()
    myGameApp.play()

if __name__ == "__main__":
    main()
