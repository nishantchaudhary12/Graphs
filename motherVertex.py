#mother vertex

from collections import defaultdict

class Graph:
    def __init__(self, num):
        self.graph = defaultdict(list)
        self.vertices = num

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def display(self):
        for each in self.graph:
            print('Vertex', each)
            print('Root ->', end="")
            for i in self.graph[each]:
                print(i, '->' ,end="")
            print('/','\n')

    def traverse(self, val, visited):
        visited.add(val)
        # print(val, end=" ")
        # print(self.graph[val])
        for each in self.graph[val]:
            if each not in visited:
                self.traverse(each, visited)

    def motherVertex(self, val):
        visited = set()
        self.traverse(val, visited)
        for i in range(self.vertices):
            if i not in visited:
                self.traverse(i, visited)
                last = i
        print('Mother Vertex:',last)


def main():
    vertices = (7)
    graph = Graph(7)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 3)
    graph.addEdge(4, 1)
    graph.addEdge(6, 4)
    graph.addEdge(5, 6)
    graph.addEdge(5, 2)
    graph.addEdge(6, 0)
    graph.display()
    graph.motherVertex(2)


main()