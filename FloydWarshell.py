# Floyd Warshell 演算法
# All-All Shortest Path Algorithm
# Negative Forbidden
def FloydWarshellAlgorithm(G):
    
    V = len(G)
    dist = [[float('inf')] * V for _ in range(V)] # 2D

    # 創建 V 為主的圖形
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif G[i][j] != 9999:
                dist[i][j] = G[i][j]

    # O(n^3)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist