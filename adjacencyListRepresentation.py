#adjacency list representation of Graphs


class Node:
    def __init__(self, val):
        self.node = val
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def addEdge(self, src, dest):
        new = Node(dest)
        temp = self.graph[src]
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new
        else: self.graph[src] = new

    def display(self):
        for i in range(self.vertices):
            temp = self.graph[i]
            print('Vertex', i)
            print('Root ->', end="")
            while temp:
                print(temp.node, '->' ,end="")
                temp = temp.next
            print('/','\n')


def main():
    vertices = 7
    graph = Graph(vertices)
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


main()
