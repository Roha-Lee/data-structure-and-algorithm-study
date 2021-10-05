class DisjointSet:
    def __init__(self, values):
        self.parent = dict()
        self.rank = dict()
        
        # 초기화 
        for node in values:
            self.parent[node] = node
            self.rank[node] = 0
        
    def find(self, node):
        if self.parent[node] != node: 
           self.parent[node] = self.find(self.parent[node])
        return self.parent[node]    
        
    def union(self, src, trg):
        if self.rank[src] == self.rank[trg]:
            self.rank[trg] += 1
            self.parent[self.find(src)] = self.find(trg)
        elif self.rank[src] < self.rank[trg]:
            self.parent[self.find(src)] = self.find(trg)
        else:
            self.parent[self.find(trg)] = self.find(src)

def kruskal(graph):
    parent = dict()
    rank = dict()

    # edge를 sort
    new_edges = []
    sorted_edges = sorted(graph['edges'])
    dis = DisjointSet(graph['vertices'])
    for edge in sorted_edges:
        _, src, dst = edge
        if dis.find(src) == dis.find(dst):
            continue
        dis.union(src, dst)
        new_edges.append(edge)

    return {'vertices': graph['vertices'], 'edges': new_edges} 

if __name__ == '__main__':
    graph = {
        'vertices': ['A','B','C','D','E','F','G'],
        'edges': [
            (7, 'A', 'B'),
            (5, 'A', 'D'),
            (7, 'B', 'A'),
            (8, 'B', 'C'),
            (9, 'B', 'D'),
            (8, 'C', 'B'),
            (5, 'C', 'E'),
            (5, 'D', 'A'),
            (9, 'D', 'B'),
            (7, 'D', 'E'),
            (6, 'D', 'F'),
            (5, 'E', 'C'),
            (7, 'E', 'D'),
            (8, 'E', 'F'),
            (9, 'E', 'G'),
            (6, 'F', 'D'),
            (8, 'F', 'E'),
            (11, 'F', 'G'),
            (9, 'G', 'E'),
            (11, 'G', 'F'),
        ]
    }
    print(kruskal(graph))