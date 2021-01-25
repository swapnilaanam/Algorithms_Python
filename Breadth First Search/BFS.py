# Importing the Queue class from queue module to work with queue data structure

from queue import Queue

# declaring all the global variable such as dictionaries, list as empty

adjacent_list = {}
visited = {}
parent = {}
level = {}
bfs_traversed_path = []


# This is our main bfs traversal function, by this we traverse the given graph
# We explore elements from queue one by one and add their children to queue

def bfs_traversal():
    current_node = queue.get()  # This method removes / pops the first element from queue and return it in variable
    bfs_traversed_path.append(current_node)

    for child_node in adjacent_list[current_node]:   # by this loop we get all the children of current explored node
        if not visited[child_node]:     # we check if the children is already visited or not to avoid adding them again
            queue.put(child_node)       # This method inserts new child node to queue at the back/end
            visited[child_node] = True  # marking it as visited
            level[child_node] = level[current_node] + 1  # giving the level number on which child node is on from source
            parent[child_node] = current_node  # keeping track of parent of the added child node

    while not queue.empty():  # Looping and calling the function until the queue empty so that to traverse all the node
        bfs_traversal()       # connected to source


# Function to print the minimum edges needed to reach all the nodes(except source) from source

def min_edge(node):
    min_edge_num = level[node]  # we are finding out minimum edge number needed for reaching a node from source node

    if min_edge_num != -1:      # checking if our node is reachable or not from source node
        print("Minimum", min_edge_num, "edges needed to reach", node)
    else:
        print(node, "is not reachable.")


# Function to print the path taken by all the nodes(except source) from source to itself

def print_path(node):
    if parent[node] != None:  # checking if the node is reachable/ connected to the source by checking it's parent node
        path = []
        path.append(node)
        current_node = parent[node]

        # backtracking from our node(parameter) to source using parent node and adding them in a list

        while current_node != None:   # checking if we reached the source node or not ( as it will have None )
            path.append(current_node)
            current_node = parent[current_node]

        path.reverse()  # as we backtracked from certain node to source, we reverse the list

        print("Path taken:", end=" ")

        for node_name in path:
            print(node_name, end=" ")

        print()


# taking input for node and edge number in a single line
# as python takes input as string we are separating the inputted string by a space into two value
# as assigning them to the variable

node_number, edge_number = input().split()

node_number = int(node_number)  # as input is taken as string, converting it to int
edge_number = int(edge_number)

for i in range(node_number):  # initializing all variable for all the nodes as empty, False, 0 values as not visited yet
    adjacent_list[i] = []
    visited[i] = False
    parent[i] = None
    level[i] = -1

# inputting all the edges running a loop

for i in range(edge_number):
    u, v = input().split()  # we are taking both parent and child node input in one line
    u = int(u)  # as nodes are number, converting string to int
    v = int(v)
    adjacent_list[u].append(v)  # as our graph is bi-directional, we are adding both input as
    adjacent_list[v].append(u)  # child of each other in our adjacent_list dict

start_node = int(input())  # inputting the staring node

queue = Queue()  # creating a new queue object using Queue Class (constructor)

queue.put(start_node)  # inserting start node in the end of the queue
visited[start_node] = True  # marking it as visited
level[start_node] = 0  # as start node is our root, we are giving it a level of 0

bfs_traversal()  # calling our bfs_traversal() function (located upwards) and running a bfs on the given graph

print()
print("From the source", start_node, ":")
print()

# After running our bfs traversal, we are printing minimum edge to reach all nodes (expect source)
# from source and printing its path from source using loop

for i in range(node_number):
    if i == start_node:
        continue

    min_edge(i)
    print_path(i)
    print()

print("Bonus: ")

# printing all the child our bfs traversed on level by level basis (considering root as level 1)

child_by_level = {}  # dictionary for soring all the child of a level

# initializing all the level as empty list (no child)

for level_number in level.values():
    if level_number == -1:  # checking if it's visited or not
        continue
    child_by_level[level_number] = []  # adding 1 as we are considering root as level 1

# access our previously stored level dict and from that adding all the child of one particular level
# on the list of that level's list using key value pair

for child in bfs_traversed_path:
    level_number = level[child]
    if level_number == -1:
        continue
    child_by_level[level_number].append(child)

# print all child of a level one by one

for level_number in sorted(child_by_level.keys()):  # sorted the dict based on key values
    print("Level", level_number + 1, end="")   # as we are considering root as level 1
    print(": ", end="")
    for child in child_by_level[level_number]:
        print(child, end=",")
    print()
