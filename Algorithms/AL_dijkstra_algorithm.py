
import heapq

def dijkstra(graph, root):
    path_dict = {node: [float('inf'), node] for node in graph}
    path_dict[root][0] = 0
    
    pri_q = []
    heapq.heappush(pri_q, (0, root))
    
    while pri_q:
        dist, node = heapq.heappop(pri_q)
        if dist > path_dict[node][0]:
            continue
        for neighbor, weight in graph[node].items():
            if path_dict[neighbor][0] > dist + weight:
                # 우선순위큐에 넣기 
                heapq.heappush(pri_q, (dist + weight, neighbor))
                # 거리 업데이트 
                path_dict[neighbor][0] = dist + weight
                path_dict[neighbor][1] = node
    
    return path_dict


def get_path(path_dict, root, dest):
    if root == dest:
        return ""
    node = dest
    path = []
    path.append(' 🚩 %s (dest)'%(dest))
    while not root == path_dict[node][1]:
        path.append(' 🚩 %s'%(path_dict[node][1]))
        node = path_dict[node][1]
    path.append('(start) %s'%(root))
    path.reverse()
    return ''.join(path)

if __name__ == '__main__':
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }
    start = 'A'
    result = dijkstra(graph, start)
    for dest in graph.keys():
        print(get_path(result, start, dest))
