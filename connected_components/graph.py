from queue import Queue


class Graph:
    def __init__(self, file_name):
        self.nodes = set()
        self.neighbours = dict()
        with open(file_name, "r") as file:
            for line in file.readlines():
                source, destination = line.strip().split(" ")

                self.nodes.add(source)
                self.nodes.add(destination)

                self.add_neighbour(source, destination)
                self.add_neighbour(destination, source)

    def get_neighbours(self, node):
        return self.neighbours.get(node, list())

    def get_connected_components(self):
        visited = dict()

        no_components = 0

        for node in self.nodes:
            if not visited.get(node, False):
                no_components += 1
                self.visit(node, visited)

        return no_components

    def visit(self, node, visited):
        visited[node] = True
        for n in self.neighbours.get(node, list()):
            if not visited.get(n, False):
                self.visit(n, visited)

    def add_neighbour(self, source, destination):
        neighbours = self.neighbours.pop(source, list())
        neighbours.append(destination)
        self.neighbours.update({source: neighbours})
