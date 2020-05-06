from connected_components.graph import Graph


def main():
    graph = Graph("test.csv")

    print(graph.get_connected_components())


if __name__ == "__main__":
    main()
