
import heapq

def dijkstra(graph, root):
    # path_dict = dict()
    # for key in graph.keys():
    #     if key == root:
    #         path_dict[key] = 0
    #     else:
    #         path_dict[key] = 'INF'
    
    path_dict = {node: float('inf') for node in graph}
    path_dict[root] = 0
    
    pri_q = []
    heapq.heappush(pri_q, (0, root))
    
    while pri_q:
        dist, node = heapq.heappop(pri_q)
        if dist > path_dict[node]:
            continue
        for neighbor, weight in graph[node].items():
            if path_dict[neighbor] == 'INF' or path_dict[neighbor] > dist + weight:
                # 우선순위큐에 넣기 
                heapq.heappush(pri_q, (dist + weight, neighbor))
                # 거리 업데이트 
                path_dict[neighbor] = dist + weight
    return path_dict

if __name__ == '__main__':
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }
    print(dijkstra(graph, 'A'))