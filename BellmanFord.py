# 定義 Edge 類別
class Edge:
    def __init__(self, u, v, w):
        self.u = u # 起點
        self.v = v # 終點
        self.w = w # 權重

# Bellman Ford 演算法
# single-source Shortest Path Algorithm
# Negative Allowed
def BellmanFordAlgorithm(G, Node):
    
    V = len(G)

    # 初始化距離陣列，設為無限大
    dist = [float('inf')] * V
    dist[Node] = 0
    
    # 創建edge為主的圖形向量
    edges = []
    for u in range(V):
        for v, w in enumerate(G[u]):
            if w != 9999 and u != v:
                edges.append(Edge(u, v, w)) 
    
    # 放鬆所有邊 (V-1) 次
    for _ in range(V - 1):
        for edge in edges:
            if dist[edge.u] != float('inf') and dist[edge.u] + edge.w < dist[edge.v]:
                dist[edge.v] = dist[edge.u] + edge.w

    # 檢查是否存在負迴圈
    for edge in edges:
        if dist[edge.u] != float('inf') and dist[edge.u] + edge.w < dist[edge.v]:
            print("Graph contains negative weight cycle")
            return None
    
    return dist