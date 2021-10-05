import heapq
from collections import defaultdict
from heapdict import heapdict

def prim(graph):
    new_edges = []
    adjacent_edges = defaultdict(list)
    for w, s, t in graph['edges']:
        adjacent_edges[s].append((w, s, t))
        adjacent_edges[t].append((w, t, s))
    queue = []
    nodes = graph['vertices']
    curr = nodes[0]
    linked = {curr}
    
    while True:
        for item in adjacent_edges[curr]:
            if item[2] not in linked:
                heapq.heappush(queue, item)
        edge = heapq.heappop(queue)
        while edge[2] in linked:
            edge = heapq.heappop(queue)
        linked.add(edge[2])
        curr = edge[2]
        new_edges.append(edge)
        if len(linked) == len(nodes):
            break
        
    return {'vertices': graph['vertices'], 'edges': new_edges} 

def prim_advanced(graph):
    new_edges = []
    queue = heapdict()
    start_v = graph['vertices'][0]
    from_where = dict()
    adjacent_edges = defaultdict(list)

    for w, s, t in graph['edges']:
        adjacent_edges[s].append((w, s, t))
        adjacent_edges[t].append((w, t, s))
    
    for vertice in graph['vertices']:
        queue[vertice] = float('Inf')
        from_where[vertice] = None
    
    queue[start_v] = 0
    from_where[start_v] = start_v
    
    while queue: 
        node, curr_weight = queue.popitem()
        new_edges.append((curr_weight, from_where[node], node))
        for w, s, t in adjacent_edges[node]:
            if t in queue and queue[t] > w:                    
                queue[t] = w
                from_where[t] = s

    return {'vertices': graph['vertices'], 'edges': new_edges[1:]} 

if __name__ == '__main__':
    graph = {
        'vertices': ['A','B','C','D','E','F','G'],
        'edges': [
            (7, 'A', 'B'),
            (5, 'A', 'D'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (5, 'C', 'E'),
            (7, 'D', 'E'),
            (6, 'D', 'F'),
            (5, 'E', 'C'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (11, 'F', 'G'),
        ]
    }
    print(prim_advanced(graph))