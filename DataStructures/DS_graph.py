class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return '\n'.join(["%s: %s"%(node, node.neighbors) for node in self.nodes])


class Node: 
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []
    
    def add_neighbors(self, other):
        if other not in self.neighbors:
            self.neighbors.append(other)
            other.neighbors.append(self)
        
    def __repr__(self):
        return self.value

if __name__ == '__main__':
    graph = Graph()
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeC.add_neighbors(nodeB)
    nodeC.add_neighbors(nodeA)
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    print(graph)