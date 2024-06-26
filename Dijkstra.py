import heapq

def dijkstra(G, start):
    
    V = len(G)
    dist = [float('inf')] * V # D[v]
    prev = [None] * V # C[v]
    dist[start] = 0
    priority_queue = [(0, start)]  # ConstructQ(D, n-1)、(distance, vertex)

    while priority_queue:
        
        current_dist, k = heapq.heappop(priority_queue) # ExtractMin(Q)，current_dist：D[k]
        print('priority_queue: ', priority_queue,': current_dist: ', current_dist, 'k: ',k)

        # 如果pop的距離已經大於當前記錄的距離，則表示這個節點已經處理過
        if current_dist > dist[k]:
            continue

        for v, weight in enumerate(G[k]):
            if weight != 9999:  # 9999 代表無限大，表示沒有直接連接
                distance = current_dist + weight # current_dist：D[k]、weight：w[k, v]
                if distance < dist[v]: # dist[v]：D[v]
                    dist[v] = distance # 更新D[v]
                    prev[v] = k # 更新C[v]
                    heapq.heappush(priority_queue, (distance, v))

    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []