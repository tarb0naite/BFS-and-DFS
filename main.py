from collections import defaultdict
import time


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start, goal):
        visited = set()
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for adjacent in self.graph[node]:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
        return None

    def DFS(self, start, goal):
        visited = set()
        stack = [[start]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                for adjacent in self.graph[node]:
                    new_path = list(path)
                    new_path.append(adjacent)
                    stack.append(new_path)
                visited.add(node)
        return None


def data_function(algorithm, data, start, goal):
    start_time = time.time()
    path = algorithm(start, goal)
    end_time = time.time()

    if path:
        print(f"Path found by {algorithm.__name__}: {path}")
        print(f"Time taken: {end_time - start_time} seconds")
    else:
        print(f"No path found by {algorithm.__name__}")


if __name__ == "__main__":
    graph_data = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [''],
        'E': [''],
        'F': ['']
    }

    print("Graph Data:")
    for node, neighbors in graph_data.items():
        print(f"{node}: {neighbors}")

    graph = Graph()
    for node, neighbors in graph_data.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)

    start_node = 'A'
    goal_node = 'F'

    print("Breadth First Search (BFS): ")
    data_function(graph.BFS, graph_data, start_node, goal_node)

    print("\nDepth First Search (DFS): ")
    data_function(graph.DFS, graph_data, start_node, goal_node)