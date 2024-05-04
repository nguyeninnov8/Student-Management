import GRAPH_CLASS
import A_R_WAREHOUSE
import sys

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
for warehouse in A_R_WAREHOUSE.warehouses_list:
    nodes.append(warehouse.name)
    init_graph[warehouse.name] = {}
    for dest_warehouse, cost in warehouse.transportation_costs.items():
        init_graph[warehouse.name][dest_warehouse] = cost

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
  
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

graph = GRAPH_CLASS.Graph(nodes, init_graph)

def node_input():
    node_start = str(input("Enter starting node"))
    node_end = str(input("Enter ending node"))
    return node_start, node_end


    
