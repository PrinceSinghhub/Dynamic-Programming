def shortestDist(graph,N):

    # this algo work in start lasts node find min path
    dist = [0] * N
    dist[N - 1] = 0

    print(dist)
    for i in range(N - 2, -1, -1):

        # Initialize distance from
        # i to destination (N-1)
        dist[i] = INF

        # Check all nodes of next stages
        # to find shortest distance from
        # i to N-1.
        for j in range(N):

            # Reject if no edge exists
            if graph[i][j] == INF:
                continue

            # We apply recursive equation to
            # distance to target through j.
            # and compare with minimum
            # distance so far.
            dist[i] = min(dist[i],
                          graph[i][j] + dist[j])

    print(dist)
    return dist[0]

# N: number of nodes
N = 12
INF = 99999999999  #temp value

# mygraph value
# graph = [[INF, 1, 2, 5, INF, INF, INF, INF],
#          [INF, INF, INF, INF, 4, 11, INF, INF],
#          [INF, INF, INF, INF, 9, 5, 16, INF],
#          [INF, INF, INF, INF, INF, INF, 2, INF],
#          [INF, INF, INF, INF, INF, INF, INF, 18],
#          [INF, INF, INF, INF, INF, INF, INF, 13],
#          [INF, INF, INF, INF, INF, INF, INF, 2]]

graph = [[INF,9, 7, 3, 2,INF,INF, INF, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 4,2,7, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 2, 7, INF, INF, INF, INF,INF],
         [INF, INF, INF, INF, INF, INF, INF, 11, INF, INF, INF,INF],
         [INF, INF, INF, INF, INF, INF, 11, 8, INF, INF, INF,INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 6, 5, INF,INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 4, 3, INF,INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, 6,INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,INF, 4,],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,2],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,5]]

print(shortestDist(graph,N))