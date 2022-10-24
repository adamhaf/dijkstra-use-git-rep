# dijkstra-use-git-rep

# Introdaction
Today, as we all know we have apps that help us navigate.
But, sometimes when we are in an enormous building (like a hospital mall, etc.…) the GPS isn’t precise enough to help us navigate.
So, I develop a small program that can find the shortest path to our destination.\
I assume that I have this knowledge about the building: location of the junctions (hallways intersections), rooms, and stairs, and the distance between them, so then I can build a graph that represents the building pathways, then the program uses Dijkstra's algoritem to find the shortest path to the user's destination.

Code files:

## Building-Infrastructure:
I define here the classes for nodes, floors, and buildings. 

### Node-Class:
```python
        """
        :param type: junction, stairs, room
        :param level: which level the node is in
        :param building_number:
        :param vertex: list of neighbors
        """
        self.type = type
        self.level = level
        self.building_number = building_number
        self.initial = finding_initial(type)
        self.neighbors = neighbors
```

Floor-Class:
```python
        self.level = level # the floor level
        self.ptr_floor = ptr_floor # a pointer to one of the nodes (usually junction number 1)
        self.edges = {} # the edges of the graph stored in a dictionary (initial, weight)
        self.nodes = rooms_and_junc_to_dic(ptr_junc_list,ptr_room_list) #the nodes of the floor (junction stairs and room)
```

Building-Class:
```python 
     self.name = name #name of the building
     self.floor_list = floor_list # a list of ptr floor.
     # the list is organized at position 0 we will find floor number 1 and so on.
```

## Text-To-Graph:

Taking text files that represent the graph (according to the assumption down below) and making form it a graph.

## Path-Finder:

This script manages the text-to-graph file, it sends information about the location of the files to Text-to-graph, then Text-to-graph returns the building graph. After creating the graph it uses Dijkstra to find the shortest path and return a string of it.

## Graph Assumptions:

The Graph is undirected and weighted, for each floor we will have a separate text file. For each file we will work with that assumption for describing the floor: 
(line number)
1)	Building number
2)	Number of junctions
3)	Number of stairs
4)	Level number
5)	for each junction or room that is represented by a node, we will write a separate line that starts with the type and number of this node, 
then after **one** space, each neighbor of this node will be separated by one space.
##### format:
Current junction/room (initial of neighbors 1) (weight of neighbors 1) (initial of neighbors 2) (weight of neighbors 2) ….
```diff
For example: j1 r1 3 r2 3
from left to right ->
j1 is the current node (junction 1)
r1 is the neighbor of j1 with a weight of 3
r2 is the neighbor of j1 with a weight of 3
```
## Stairs Assumptions:

First, like in all ordinary buildings' stairs are connected, also we will assume that the stairs are connected only to junction 1 on each floor (this assumption isn't mandatory, it`s just for the added example).

1)	Building number
2)	Number of stairs 
3)	Next lines will be in this format: current level [ next node, weight, next node level]

For example: s1 1 j2 3 2 j1 3 \
from left to right -> \
s1 is the current level \
s1 is connected to j2 with a weight of 3 \
j1 of the second floor connected to s1 with a weight of 3
