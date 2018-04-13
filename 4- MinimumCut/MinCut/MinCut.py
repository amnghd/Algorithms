# importing require packages
import random
import numpy as np

# importing vertices (into dictionary)
input_file = 'kargerMinCut.txt'
with open(input_file, 'r') as data:
    line = data.read().strip().split("\n")


def pick_two_vertices(graph):
    """ This function gets a graph as a dictionary and output
    two vertixes randomly chosen, we need to assure that vertices are
    connected"""
    M = len(graph.keys()) # calculating length of the dictionary keys
    i = random.randint(0, M-1) # choose a random index of the keys
    vert1 = list(graph.keys())[i] # choosing the first vertix
    N = len(graph[vert1]) # calculate the length of the random key
    j = random.randint(0, N-1) # choose a random index of values
    vert2 = list(graph[vert1])[j] # choosing the second verticx
    return [vert1, vert2]



def combiner(graph, vert1, vert2): # we dont need to return anything as python changes graph inside the function
    """ This function combines two vertixes into one, assures that all the graph is updated """
    vert2_connections = list(graph[vert2]) # getting the values of the vertix to be merged
    vert1_connections = (list(graph[vert1])+(vert2_connections)) # extending vert1 connection to include vert2
    graph.pop(vert2, None) # drop vert2
    for key, values in graph.items(): # replace vert 2 in all the connections with vert 1
        graph[key] = [vert1 if x == vert2 else x for x in list(values)]
    vert1_connections = [x  for x in vert1_connections if (x != vert1 and x != vert2)] # removing self loop
    graph[vert1] = vert1_connections # updating vert1 connections to include vert2

def min_cut_single_try(graph):
    """ This function reduces the graph recursively untill it gets to two edges """
    while len(graph.keys())>2 :
        vert1, vert2 = pick_two_vertices(graph) #picking two vertixes using
        combiner(graph, vert1, vert2)
    list_of_vertices = list(graph.values())[0]
    return len(list_of_vertices)




#### main #####

minimum_cut = 200
for i in range(200): # run this code for the total number of vertices
    graph_dict = {}
    # here we read the data
    for element in line:
        line_list = list(map(int, element.strip().split("\t")))
        graph_dict[line_list[0]] = line_list[1:]
    min_value = min_cut_single_try(graph_dict)
    minimum_cut = min(min_value, minimum_cut)

print("The minimum cut includes {} edges.".format(minimum_cut)) # here we output the minimum cut
