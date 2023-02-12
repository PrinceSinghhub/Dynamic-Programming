from sys import maxsize
from itertools import permutations

V = 4


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    print(vertex)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize   #garbage value
    print(min_path)

    # all permutations of vertex
    next_permutation = permutations(vertex)
    for i in next_permutation:
        print(i)

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path

graph = [[0,1,1,3], [2, 0,5,1],
             [1,4,0,3], [4,3,2,0]]
s = 0
print(travellingSalesmanProblem(graph, s))