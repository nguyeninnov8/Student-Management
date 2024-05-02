import lib
def _menu_():
    scm = SupplyChainManager()
    while True:
        print("======== Choose your choice ========")
        print("1. Add new warehouse to system")
        print("2. Remove warehouse")
        print("3. Update costs between warehouses")
        print("4. Find optimal cost between warehouses")
        print("5. Display warehouses list")
        print("6. Display Transportation Network")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            scm.add_warehouses()
        elif choice == "2":
            scm.remove_warehouse()
        elif choice == "3":
            scm.update_costs_between_warehouses()
        elif choice == "4":
            scm.find_optimal_cost_between_warehouses()
        elif choice == "5":
            scm.display_warehouses_list()
        elif choice == "6":
            scm.display_transportation_network()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")
