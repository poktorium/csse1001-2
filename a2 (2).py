"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""

# Write your code here
#display is in a2_support


class GameLogic:
    
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
        return self._dungeon_size

    def init_game_information(self):
        entity_position = {}
        for i in range(len(self._dungeon)):
            for j in range(len(self._dungeon[i])):
                if self._dungeon[i][j] == PLAYER:
                    self._player.set_position((self._dungeon[i], self._dungeon[j]))
                    my_player_tuple = (self._dungeon[i], self._dungeon[j])
                    entity_position.update( {my_player_tuple : self._player} )
                elif self._dungeon[i][j] == KEY:
                    my_key_tuple = (self._dungeon[i], self._dungeon[j])
                    entity_position.update( {my_key_tuple : Key()} )
                elif self._dungeon[i][j] == DOOR:
                    my_door_tuple = (self._dungeon[i], self._dungeon[j])
                    entity_position.update( {my_door_tuple : Door()} )
                elif self._dungeon[i][j] == WALL:
                    my_wall_tuple = (self._dungeon[i], self._dungeon[j])
                    entity_position.update( {my_wall_tuple : Wall()} )
                elif self._dungeon[i][j] == MOVE_INCREASE:
                    my_movinc_tuple = (self._dungeon[i], self._dungeon[j])
                    entity_position.update( {my_movinc_tuple : MoveIncrease()} )
        return entity_position
            

            
    
    def get_game_information(self):
        for i in self._dungeon:
            if i == Entity():
                entity_dict = {Entity.get_position():Entity.__str__()}
                self.entity_position.update(entity_dict)
        return self.entity_position
    
    def get_player(self):   
        return Entity.get_id(Player)

    def get_entity(self, position: tuple):
        entity_dict = self.init_game_information()
        return entity_dict.get(position)

    
    def get_entity_in_direction(self, direction: str):
        allowed_direction = ["W", "A", "S", "D"]
        if direction in allowed_direction:
            player_position = Player.get_position()
            direction_position = DIRECTIONS.get(direction)
            entity_direction = (player_position[0] + direction_position[0], player_position[1] + direction_position[1])
            
        else:
            return None

    def collision_check(self, direction: str):
        allowed_direction = ["W", "A", "S", "D"]
        if self.get_entity_in_direction() == None:
            return False
        elif direction in allowed_direction:
            if Player.get_position() + DIRECTIONS.get(direction) == Entity():
                if Entity.can_collide() == True:
                    return True
                elif Entity.can_collide() == False:
                    return False
            else:
                return False 
    
    def new_position(self, direction: str):
        player_position = Player.get_position() + DIRECTIONS.get(direction)
        return player_position
    
    def move_player(self, direction: str):
        Player.set_position((Player.get_position() + DIRECTIONS.get(direction)))

    def check_game_over(self):
        if Player.moves_remaining() == 0:
                return True
        else:
            return False
        
    def set_win(self, win: bool):
        if win == True:
            return True
        elif win == False:
            return False
        else:
            print("Invalid Command")
    
    def won(self):
        return self.set_win()

                
            
        



class GameApp:


    def play(self):
        player_choice = input("Pleae choose a level, game1.txt, game2.txt or game3.txt: ")
        print(player_choice)
        if Player.won() == False:
            if player_choice == "game1.txt":
                game = load_game(game1.txt)
                current_game = Display(game_information, len(load_game(game1.txt)))
            
            elif player_choice == "game2.txt":
                game = load_game(game2.txt)
                current_game = Display(game_information, len(load_game("game2.txt")))

            elif player_choice == "game3.txt":
                pass
            else:
                print("invalid")
        else:
            pass


class Entity:
    will_collide = None
    def __init__(self):
        self._id = 'Entity'
        self._collidable = True

    def get_id(self):
        return self._id
    
    def set_collide(self, collidable):
        self._collidable = collidable
        
    def can_collide(self):
        return self._collidable

    def __str__(self):
        return f"Entity('{self._id}')"
    
    def __repr__(self):
        return f"Entity('{self._id}')"


class Player(Entity):
    
    inventory = []
    id = "O"

    def __init__(self, allowed_moves):
        self._allowed_moves = allowed_moves
        self.id = id
        self._collidable = True
        self.move_count = 0
        self.player_position = None

    def get_position(self):
        return self.player_position
        #this could also return set_position as that is the method defining the players position at that time 

    def set_position(self, position: tuple):
        self.player_position = position
        #this should set the players position

    def change_move_count(self, number:int):
        #ifself.move_count + number < self._allowed_moves:
        self.move_count += number
        
    def moves_remaining(self):
        moves_remaining = self._allowed_moves + self.move_count
        return moves_remaining
        #Returns an int representing how many moves the player has left

    def add_item(self, item):
        self.inventory.append(item)
        #this adds an item to the players inventory
    
    def get_inventory(self):
        return self.inventory
        #returns a list of what's in the players inventory
    
    def get_id(self):
        return "O"

    def set_collidable(self, collidable: bool):
        self._collidable = collidable
    
    def can_collide(self):
        return self._collidable
    
    def __str__(self):
        return "Player('O')"

    def __repr__(self):
        return "Player('O')"



class Door(Entity):

    def __init__(self, name = 'Door', id='D'):
        self._id = id
        self._name = name
        self._collidable = True

    def get_position(self):
        return (self.x,self.y)
    
    def get_id(self):
        return self._id
    
    def set_collidable(self, collidable = bool):
        self._collidable = collidable

    def can_collide(self):
        return self._collidable
    
    def __str__(self):
        return "Door('D')"

    def __repr__(self):
        return "Door('D')"


class Item(Entity):
    def __init__(self, name = 'Item'):
        self._name = name
        self._collidable = True

    def get_id(self):
        return 'Entity'

    def get_name(self):
        return self._name
    
    def set_collide(self, collidable: bool):
        self._collidable = collidable

    def can_collide(self):
        return self._collidable

    def on_hit(self, game=GameApp):
        raise NotImplementedError

    def __str__(self):
        return f"{self._name}('Entity')"
    
    def __repr__(self):
        return f"{self._name}('Entity')"

class MoveIncrease(Item):
    
    def __init__(self, moves = 5, id='M', name = "MoveIncrease"):
        self._id = id
        self._name = name
        self.moves = moves
        self._collidable = True
    
    def get_cooridnate(self):
        return (self._x,self._y)
        
    def get_id(self):
        return 'M'

    def set_collide(self, collidable: bool):
        self._collidable = collidable

    def can_collide(self):
        if self._collidable == True:
            return True
        else:
            return False

    def __str__(self):
        return f"{self._name}('{self.get_id()}')"
    
    def __repr__(self):
        return f"{self._name}('{self.get_id()}')"


class Wall(Entity):
    
    def __init__(self):
        self._id = '#'
        self._name = "Wall"
        self._collidable = False

    def get_name(self):
        return self._name
    
    def get_cooridnate(self):
        return (self._x,self._y)

    def get_id(self):
        return self._id 
    
    def set_collide(self, collidable):
        self._collidable = collidable
            
    def can_collide(self):
        return self._collidable
        

    def __str__(self):
        return f"Wall('#')"
    
    def __repr__(self):
        return f"Wall('#')"


class Key(Item):

    def __init__(self, id='K', name = 'Key'):
        self._id = id
        self._name = name 
        self._collidable = True

    def get_cooridnate(self):
        return (self._x,self._y)

    def get_id(self):
        return self._id
    
    def set_collide(self, collidable):
        self._collidable = collidable

    def can_collide(self):
        if self._collidable == True:
            return True
        else:
            return False

    def on_hit(self, game = GameApp):
        #this needs to be added to the players inventory once collected 
        return None
    

    def __str__(self):
        return f"{self._name}('{self.get_id()}')"
    
    def __repr__(self):
        return f"{self._name}('{self.get_id()}')"


def main():
    GameApp()

if __name__ == "__main__":
    main()