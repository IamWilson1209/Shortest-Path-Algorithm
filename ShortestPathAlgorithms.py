from Dijkstra import dijkstra, reconstruct_path
from FloydWarshell import FloydWarshellAlgorithm 
from BellmanFord import BellmanFordAlgorithm
from Graph import networkplot


# 執行FloydWarshell演算法
def RunFloydWarshell(G):

    # 使用Floyd-Warshall演算法計算最短路徑
    distances = FloydWarshellAlgorithm(G)

    # 列印最短路徑矩陣
    print("Floyd Warshell Shortest path: ")
    for i, row in enumerate(distances):
        print(f"Node {i}")
        for j, dist in enumerate(row):
            print(f"From Node {i} - {j} : {dist}")

# 執行BellmanFord演算法
def RunBellmanFord(G, Node):

    # 使用Bellman-Ford演算法計算最短路徑
    distances = BellmanFordAlgorithm(G, Node)

    # 列印最短路徑
    if distances:
        print("Bellman Ford Shortest path from node", Node)
        for i, distance in enumerate(distances):
            print(f"Node {Node} - {i} : {distance}")

# 執行Dijkstra演算法
def Dijkstra(G, node):
    
    # 使用Dijkstra演算法計算最短路徑
    distances, predecessors = dijkstra(G, node)

    # 列印最短路徑和路徑
    print(f"Dijkstra Shortest Path from node {node}:")
    for end_node in range(len(G)):
        if distances[end_node] == float('inf'):
            print(f"Node {node} to Node {end_node}: No path")
        else:
            path = reconstruct_path(predecessors, node, end_node)
            path_str = " -> ".join(map(str, path))
            print(f"Node {node} to Node {end_node}: Distance = {distances[end_node]}, Path = {path_str}")


if __name__ == '__main__':

    # 定義圖的鄰接矩陣
    G = [
        [0, 3, 9999, 9999, 6, 15],
        [3, 0, 1, 9999, 9999, 9999],
        [9999, 1, 0, 5, 9999, 9999],
        [9999, 9999, 5, 0, 2, 3],
        [6, 9999, 9999, 2, 0, 2],
        [15, 9999, 9999, 3, 2, 0]
    ]

    Node = 2
    # RunFloydWarshell(G)
    # RunBellmanFord(G, Node)
    Dijkstra(G, Node)
    networkplot(G)