import matplotlib.pyplot as plt
import networkx as nx
import time


class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph = graph_dict

    def bfs(self, start, goal):
        visited = set()
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for adjacent in self.graph.get(node, []):
                    if adjacent not in visited:
                        new_path = list(path)
                        new_path.append(adjacent)
                        queue.append(new_path)
        return None

    def dfs(self, start, goal):
        visited = set()
        stack = [[start]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for adjacent in self.graph.get(node, []):
                    if adjacent not in visited:
                        new_path = list(path)
                        new_path.append(adjacent)
                        stack.append(new_path)
        return None


def visualize_search(graph, path):
    g = nx.Graph(graph)
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=800)
    nx.draw_networkx_nodes(g, pos, nodelist=path, node_color='red', node_size=800)
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='red', width=2)
    plt.show()


def evaluate_algorithm(algorithm, data, start=None, goal=None):
    start_time = time.time()
    path = algorithm(start, goal)
    end_time = time.time()
    if path:
        print(f"Path found by {algorithm.__name__}: {path}")
        print(f"Time taken: {end_time - start_time} seconds")
    else:
        print(f"No path found by {algorithm.__name__}")


if __name__ == "__main__":
    while True:
        graph_data_set1 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['B', 'F'],
            'D': ['C', 'E'],
            'E': ['D', 'F'],
            'F': ['C', 'E']
        }

        graph_data_set2 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['E'],
            'D': ['F'],
            'E': ['C'],
            'F': []
        }

        graph_data_set3 = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'F'],
            'D': [],
            'E': [],
            'F': ['C']
        }

        algorithms = {
            "bfs": Graph(graph_data_set1).bfs,
            "dfs": Graph(graph_data_set1).dfs
        }

        print("Available Graph Data Sets:")
        print("1: Graph Data Set 1")
        print("2: Graph Data Set 2")
        print("3: Graph Data Set 3")
        choice = int(input("Enter the number of the graph data set you want to visualize: "))
        if choice == 1:
            chosen_graph_data = graph_data_set1
        elif choice == 2:
            chosen_graph_data = graph_data_set2
        elif choice == 3:
            chosen_graph_data = graph_data_set3
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")
            continue

        print("\nAvailable Algorithms:")
        for algorithm_name in algorithms.keys():
            print(algorithm_name)

        algorithm_choice = input("Enter the name of the algorithm you want to use: ")
        chosen_algorithm = algorithms.get(algorithm_choice)

        if chosen_algorithm:
            start_node = 'A'
            goal_node = 'F'

            print(f"\nEvaluation of {algorithm_choice} on Chosen Graph Data Set:")
            evaluate_algorithm(chosen_algorithm, chosen_graph_data, start_node, goal_node)

            path = chosen_algorithm(start_node, goal_node)
            if path:
                visualize_search(chosen_graph_data, path)
        else:
            print("Invalid algorithm choice. Please select from the available algorithms.")

        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == 'yes':
            break
