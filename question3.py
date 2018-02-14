def question3(graph):
    """
    Given a graph of the form represnted in the above adjacency list, this function will
    return a minimum spanning tree for the graph in the same structure as the input.
    """
    
    #Return input if graph is empty
    if graph == None or len(graph) <= 1:
        return graph
    
    #Create subgraph with 1 vertex (vertex choice doesn't matter)
    min_vert = graph.keys()[0]
    sub = {min_vert: []}
    
    #Foreign edges graph, mapping foreign nodes to their least expense
    #connectable edge tuple (domestic vert, edge weight)
    #O(n)
    foreign = {}
    for tup in graph[min_vert]:
        foreign[tup[0]] = (min_vert, tup[1])
    #For each foreign key
    #O(n)
    while len(foreign) != 0:
        #Get minimum vertex
        min_graph_vert = ""
        min_edge_val = float("inf")
        min_sub_vert = ""
        
        #O(n)
        for graph_vert in foreign:
            sub_vert = foreign[graph_vert][0]
            edge_val = foreign[graph_vert][1]
            
            #If lower weight edge
            if edge_val < min_edge_val:
                #Store subgraph vertex
                min_sub_vert = sub_vert
                #Store foreign graph vertex
                min_graph_vert = graph_vert
                #Store edge weight
                min_edge_val = edge_val
        
        #Minimum edge found
        #Add edge entry for vertex already in the subgraph
        sub[min_sub_vert].append((min_graph_vert, min_edge_val))
        #Add entry for new foreign vertex
        sub[min_graph_vert] = [(min_sub_vert, min_edge_val)]
        
        #Remove graph vert from foreign (it's now in subgraph)
        del foreign[min_graph_vert]
        
        #Check if newly added vertex has better/new edges to offer
        #O(n)
        for tup in graph[min_graph_vert]:
            graph_vert = tup[0]
            graph_vert_edge_val = tup[1]
            
            #If identified vertex isn't already in subgraph
            if graph_vert not in sub:
                #If new foreign edge, add, or if better edge for foreign vertex, replace
                if graph_vert not in foreign or graph_vert_edge_val < foreign[graph_vert][1]:
                    foreign[graph_vert] = (min_graph_vert, graph_vert_edge_val)
    return sub

q3_tests = [
    {
        'A': [('B', 2)],
        'B': [('A', 2), ('C', 5)],
        'C': [('B', 5)]
    },
    {},
    {"A": []},
    {
        'A': [('B', 2), ("C", 1)],
        'B': [('A', 2), ('C', 3)],
        'C': [("A", 1), ('B', 3)]
    },
    {
        'A': [('B', 2), ("C", 1)],
        'B': [('A', 2), ('C', 3), ("D", 4)],
        'C': [("A", 1), ('B', 3), ("D", 5)],
        "D": [("B", 4), ("C", 5)]
    }
]

q3_solns = [
    {
        'A': [('B', 2)],
        'B': [('A', 2), ('C', 5)],
        'C': [('B', 5)]
    },
    {},
    {"A": []},
    {
        'A': [('B', 2), ("C", 1)],
        'B': [('A', 2)],
        'C': [("A", 1)]
    },
    {
        'A': [('B', 2), ("C", 1)],
        'B': [('A', 2), ("D", 4)],
        'C': [("A", 1)],
        "D": [("B", 4)]
    }
]

#Test solutions
for i in range(len(q3_tests)):
    result = question3(q3_tests[i])
    
    #If correct number of vertices
    is_right = len(result) == len(q3_solns[i])
    if is_right:
        
        #Iterate over each vertex in each graph to assert set equality
        sets = [result, q3_solns[i]]
        for j in range(len(sets)):
            set_a = sets[j]
            set_b = sets[(j + 1) % len(sets)]
            for k in set_a:
                tups = set_a[k]
                for t in tups:
                    is_right = t in set_b[k]
                    if not is_right:
                        break
                if not is_right:
                    break
            if not is_right:
                break
    print("Test {} passed: {}".format(i, is_right))