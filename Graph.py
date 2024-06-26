import networkx as nx

# 繪製圖形
def networkplot(G):
    # 使用networkx來創建圖
    G_nx = nx.Graph()

    # 添加節點
    V = len(G)
    for i in range(V):
        G_nx.add_node(i)

    # 添加邊和權重
    for i in range(V):
        for j in range(i+1, V):
            if G[i][j] != 9999:
                G_nx.add_edge(i, j, weight=G[i][j])