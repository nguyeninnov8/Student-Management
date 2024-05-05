import A_R_WAREHOUSE
import FIND_OPTIMAL_ROUTE

def main():
    while True:
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
            A_R_WAREHOUSE.add_warehouse()
        elif choice == "2":
            A_R_WAREHOUSE.remove_warehouse()
        elif choice == "3":
            start_node, end_node = FIND_OPTIMAL_ROUTE.node_input()
            graph = FIND_OPTIMAL_ROUTE.graph
            previous_nodes, shortest_path = FIND_OPTIMAL_ROUTE.dijkstra_algorithm(graph, start_node)
            FIND_OPTIMAL_ROUTE.print_result(previous_nodes, shortest_path, start_node, end_node)
        elif choice == "4":
            A_R_WAREHOUSE.update_warehouse()
        elif choice == "5":
            A_R_WAREHOUSE.display_warehouse_list()
        elif choice == "6":
            A_R_WAREHOUSE.display_transportation_network()
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose again!")

if __name__ == "__main__":
    main()
