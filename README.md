# dijkstra-use-git-rep


Today, as we all know we have apps that help us navigate.
But, sometimes when we are in an enormous building (like a hospital mall, etc.…) the GPS isn’t precise enough to help us navigate.
So, I develop a small program that can find the shortest path to our destination.
I assume that I have this knowledge about the building: location of the junctions, rooms, and stairs, and the distance between them, so then I can build a graph that represent the building pathways, Then the program uses algorithm Dijkstra to find the shortest path to the user destination.

Code files:

Building-Infrastructure:
I define here the classes for nodes, floor, and building. 

Node-Class:

type – stairs/junction/rooms
level – of the floor that this node is belong
building number - of the building that this node is belong
initial – that represent this node first we will write the initial of the type and then the number of the stairs/junction/rooms. 
Example j1(junction number one) s2 ( stairs number 2)
neighbors – a dictionary(key=initial ,value=weight) of the neighbors for this node

Floor-Class:

Level – the floor level
Ptr Floor – a pointer to one of the nodes (usually junction number 1)
edges – the edges of the graph stored in a dictionary (initial, weight)
nodes – the nodes of the floor (junction stairs and room)

Building-Class:

name – the name of the building
floor list – a python list of ptr floor, the list is organized that means that at position 0 we will find floor number 1 and so own.

Text-To-Graph:

Taking test files that represent the graph (according to the assumption down below) and making form it a graph.
Path-Finder:

This script manages the text-to-graph file, its send the information about the location of the files. After creating the graph its uses Dijkstra to find the shortest path and return it.

Graph Assumptions:

The Graph is undirected and weighted, for each floor we will have a separate text file. For each file we will work with those assumption for describing the floor: 
(line number)
1)	Building number
2)	Number of junctions
3)	Number of stairs
4)	Level number
5)	for each junction or room, we will write a separate line that start with the type and then the number, 
then sperate with space we write each neighbor of this node.
format:
Current junction/room (initial of neighbors 1) (weight of neighbors 1) (initial of neighbors 2) (weight of neighbors 2) ….
For example: j1 r1 3 r2 3
Red: current floor
Blue: j1 is a neighbor of r1 with weight of 3
Orange: j1 is a neighbor of r2 with weight of 3
	
Stairs Assumptions:
First, we like in all "normal" buildings' stairs are connected, also we will assume that the stairs are connected only to junction 1 on each floor (this assumption isn`t mandatory, it`s just for the added example).
1)	Building number
2)	Number of stairs 
3)	Next lines we be on this format: current level [ next node, weight, next node level]
For example: s1 1 j2 3 2 j1 3
Black: s1 is the current level
Red: s1 is connected to j2 with weight of 3
Orange: j1 of the second floor (underline-bold orange) connected to s1 with weight of 3



