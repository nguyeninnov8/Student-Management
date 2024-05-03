import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]

class Warehouse:
    def __init__(self, name, location, capacity) -> None:
        self.name = name
        self.location = location
        self.capacity = capacity
        self.transportation_costs = {}

    def add_transportation_cost(self, dest_warehouse, cost):
        self.transportation_costs[dest_warehouse] = cost

    def remove_transportation_cost(self, dest_warehouse):
        if dest_warehouse in self.transportation_costs:
            del self.transportation_costs[dest_warehouse]

    def update_transportation_cost(self, dest_warehouse, new_cost):
        if dest_warehouse in self.transportation_costs:
            self.transportation_costs[dest_warehouse] = new_cost

    def get_transportation_cost(self, dest_warehouse):
        return self.transportation_costs.get(dest_warehouse, float('inf'))

warehouses_list = []

def add_warehouse():
    name = input("Enter warehouse's name: ")
    location = input("Enter warehouse's location: ")
    capacity = int(input("Enter capacity of warehouse: "))
    if len(warehouses_list) == 0:
        new_warehouse = Warehouse(name, location, capacity)
        warehouses_list.append(new_warehouse)
    else:
        for warehouse in warehouses_list:
                choice = input(f"Is there any path to {warehouse.name}? Yes/No")
                if choice == "Yes":
                    cost = int(input(f"Enter transportation from {new_warehouse.name} cost to {warehouse.name}: "))
                    new_warehouse.add_transportation_cost(warehouse.name, cost)
                    warehouse.add_transportation_cost(new_warehouse.name, cost)
                elif choice == "No":
                    cost = sys.maxsize
                    new_warehouse.add_transportation_cost(warehouse.name, cost)
                    warehouse.add_transportation_cost(new_warehouse.name, cost)
                else:
                    print("Please choose again!")
        warehouses_list.append(new_warehouse)
    

def remove_warehouse():
    name = input("Enter the name of the warehouse to remove: ")
    global warehouses_list
    warehouses_list = [warehouse for warehouse in warehouses_list if warehouse.name != name]
    for warehouse in warehouses_list:
        warehouse.remove_transportation_cost(name)

def write_to_file():
    with open("Warehouses.txt", "w") as f:
        for warehouse in warehouses_list:
            f.write(f"{warehouse.name},{warehouse.location},{warehouse.capacity}\n")
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                f.write(f"{dest_warehouse},{cost}\n")

def delete_from_file():
    open("Warehouses.txt", "w").close()

def remove_duplicates(graph):
    unique_graph = {}
    for source, destinations in graph.items():
        unique_destinations = {}
        for dest, cost in destinations.items():
            if dest not in unique_graph or source not in unique_graph[dest]:
                unique_destinations[dest] = cost
        unique_graph[source] = unique_destinations
    return unique_graph

init_graph = {}
nodes = []
for warehouse in warehouses_list:
    nodes.append(warehouse.name)
    init_graph[warehouse.name] = {}
    for dest_warehouse, cost in warehouse.transportation_costs.items():
        init_graph[warehouse.name][dest_warehouse] = cost

# Remove duplicates
init_graph = remove_duplicates(init_graph)

def print_result(previous_nodes, shortest_path, start_node, target_node):
    if shortest_path[target_node] == sys.maxsize:
        print("No path found from {} to {}.".format(start_node, target_node))
    else:
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
        path.append(start_node)
        print("Optimal route from {} to {}: {}".format(start_node, target_node, " -> ".join(reversed(path))))
    
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    shortest_path = {}
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

graph = Graph(nodes, init_graph)

def node_input():
    node_start = str(input("Enter starting node"))
    node_end = str(input("Enter ending node"))
    return node_start, node_end

def main():
    while True:
        print("\n======= Supply Chain Management System =======")
        print("1. Add new warehouse to system")
        print("2. Remove warehouse")
        print("3. Find optimal route")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_warehouse()
        elif choice == "2":
            remove_warehouse()
        elif choice == "3":
            start_node, end_node = node_input()
            previous_nodes, shortest_path = dijkstra_algorithm(graph, start_node)
            print_result(previous_nodes, shortest_path, start_node, end_node)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose again!")

if __name__ == "__main__":
    main()
