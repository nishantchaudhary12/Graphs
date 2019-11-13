#DFS Traversal pf Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        if src != dest:
            self.graph[dest].append(src)

    def display(self):
        for each in self.graph:
            print('Vertex', each)
            print('Root ->', end="")
            for i in self.graph[each]:
                print(i, '->' ,end="")
            print('/','\n')

    def traverse(self, val, visited):
        visited[val] = True
        print(val, end=' ')
        for i in self.graph[val]:
            if not visited[i]:
                self.traverse(i, visited)

    def dfs(self, val):
        visited = [False] * len(self.graph)
        self.traverse(val, visited)


def main():
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 1)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(3, 4)
    graph.addEdge(2, 3)
    graph.addEdge(5, 6)
    graph.addEdge(6, 4)
    graph.addEdge(5, 2)
    graph.display()
    graph.dfs(2)


main()
