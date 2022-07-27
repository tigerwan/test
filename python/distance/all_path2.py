def find_all_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for connected_node in graph[start]:
        if connected_node not in path:
            paths += find_all_paths(graph, connected_node, end, path)
    return paths


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["D"],
        "D": ["C"],
        "E": ["F"],
        "F": ["C"],
    }
    print(find_all_paths(graph, 'A', 'D', []))
