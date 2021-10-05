from queue import Queue 

def BFS(graph, root='A'):
    queue = Queue()
    queue.put(root)
    visited = []
    while not queue.empty():
        node = queue.get()
        visited.append(node)
        for ne in graph[node]:
            if ne not in visited:
                queue.put(ne)
    return visited

def DFS(graph, root='A'):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        for ne in graph[node]:
            if ne not in visited :
                stack.append(ne)
    return visited
    


if __name__ == '__main__':
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    print(BFS(graph))
    
    print(DFS(graph))
    