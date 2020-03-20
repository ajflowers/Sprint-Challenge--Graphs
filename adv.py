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
path_back = []

# list of opposite directions for later reference:
opp_dirs = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# initialize with starting room
current_room = player.current_room.id
explored[current_room] = {}

current_exits = player.current_room.get_exits()
for dir in current_exits:
    explored[current_room][dir] = '?'

path_back.append(current_room)

print(current_room)
print(explored)

# travel to first unexplored room
for dir in ['n', 'e', 's', 'w']:
    if explored[current_room][dir] == '?':
        traversal_path.append(dir)
        player.travel(dir)
        break




# loop until all rooms explored:
while len(explored) < len(room_graph):

# Upon entering a room:
    # get room id

    current_room = player.current_room.id
    
    # get exits of new(current) room
    current_exits = player.current_room.get_exits()

    # check if room id is in keys of dictionary
    # if it is not:
    if explored.get(current_room)  is None:
        # add entry for room
        explored[current_room] = {}
        
        #for each exit add a '?':
        for dir in current_exits:
            explored[current_room][dir] = '?'
            


        
        
    # get direction of last move from traversal path
    last_move =  traversal_path[-1]
    opp_move = opp_dirs[last_move]
    print(last_move)
    print(opp_move)
    # if directions for previous not filled in:
    if explored[current_room][opp_move] == '?':
        # add current room as last room, direction moved
        explored[path_back[-1]][last_move] = current_room
        # add last room as current room, opposite direction
        explored[current_room][opp_move] = path_back[-1]

    print(f"in room {current_room}, exits: {current_exits} - visited {len(room_graph)} rooms")
    # print(explored)
    
   
    # if any directions for current room are '?'
    # in order N, E, S, W:
        #add current room id to path
        #store direction to move in traversal path
        #travel to unexplored room
    if '?' in explored[current_room].values():
        for dir in current_exits:
            # print(dir)
            # print(explored[current_room].get(dir))
            if explored[current_room].get(dir) is not None and explored[current_room][dir] == '?':
                print(f"moving {dir} to unexplored")
                path_back.append(current_room)
                traversal_path.append(dir)
                player.travel(dir)
                break


    # if all exits explored:
        # if last room id on path is this room id, delete it
        # find last room on path among directions
        # add direction to traversal path
    # elif len(explored) < len(room_graph):
    else:
        print(path_back, current_room)
        if path_back[-1] == current_room:
            del path_back[-1]
        for dir in current_exits:
            print(dir)
            if explored[current_room].get(dir) is not None and explored[current_room][dir] == path_back[-1]:
                traversal_path.append(dir)
                player.travel(dir)
                break

    
        

        
        











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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
