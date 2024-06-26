from Dijkstra import dijkstra, reconstruct_path


def Bekeretal(G, emptylocation, levels, start_point, end_point, L):
    
    n = len(emptylocation)
    m = len(levels)
    
    for i in range(1, n):

        # Shortest path for start point & end point for vertex i
        start_shortest_path, start_path = dijkstra(G, start_point, emptylocation[i])
        end_shortest_path, end_path = dijkstra(G, end_point, emptylocation[i])
        print("node: ", i)
        print("Lstart: ", start_shortest_path)
        print("Lend: ", end_shortest_path)

        height = 0
        j = levels[i] # 有多高
        for m in range(1, j):
            height = height + L[m, j]

        startoutput_cost = start_shortest_path + height
        endoutput_cost = end_shortest_path + height
        total_cost = startoutput_cost + endoutput_cost

        print(f"Output cost from start point to vertex {i} is: ",startoutput_cost)
        print(f"Output cost from vertex {i} to end point is: ",endoutput_cost)
        print(f"Total Output cost for vertex {i} is: ",total_cost)

        for start_node in range(len(G)):
            if start_shortest_path[start_node] == float('inf'):
                print(f"Node {i} to Node {start_node}: No path")
            else:
                path = reconstruct_path(start_path, i, start_node)
                path_str = " -> ".join(map(str, path))
                print(f"Node {i} to Node {start_node}: Distance = {start_shortest_path[start_node]}, Path = {path_str}")

        for end_node in range(len(G)):
            if end_shortest_path[end_node] == float('inf'):
                print(f"Node {i} to Node {end_node}: No path")
            else:
                path = reconstruct_path(end_path, i, end_node)
                path_str = " -> ".join(map(str, path))
                print(f"Node {i} to Node {end_node}: Distance = {end_shortest_path[end_node]}, Path = {path_str}")