from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


#############

# Build a dictionary of rooms explored and their connections:
explored = {}

# Build a list for the path traversed from the start of the list
path = []

# initialize with starting room


# Upon entering a room:
    # get room id

    # check if room id is in keys of dictionary
    # if it is not:
        # get exits of new(current) room
        # add entry for room and exits
    
    # if directions for previous not filled in:
        # get direction of last move from traversal path
        # add current room as last room, direction
        # add last room as current room, opposite direction
    
    # if any directions for current room are '?'
    # in order N, E, S, W:
        #add current room id to path
        #store direction to move in traversal path
        #travel to unexplored room

    # if all exits explored:
        # if last room id on path is this room id, delete it
        # move to exit
        
        

        
        











# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
