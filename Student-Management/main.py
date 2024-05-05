import A_R_WAREHOUSE
import FIND_OPTIMAL_ROUTE

def main():
    while True:
        init_graph, nodes = initialize_graph()
        init_graph = remove_duplicates(init_graph)
        graph = Graph(nodes, init_graph)
        print("\n======= Supply Chain Management System =======")
        print("1. Add new warehouse to system")
        print("2. Remove warehouse")
        print("3. Find optimal route")
        print("4. Update warehouse")
        print("5. Display warehouse list")
        print("6. Display Transportation network")
        print("7. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_warehouse()
        elif choice == "2":
            remove_warehouse()
        elif choice == "3":
            start_node, end_node = node_input()
            init_graph, nodes = initialize_graph()
            graph = Graph(nodes, init_graph)
            previous_nodes, shortest_path = dijkstra_algorithm(graph, start_node)
            print_result(previous_nodes, shortest_path, start_node, end_node)
        elif choice == "4":
            update_warehouse()
        elif choice == "5":
            display_warehouse_list()
        elif choice == "6":
            display_transportation_network()
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose again!")

if __name__ == "__main__":
    main()
