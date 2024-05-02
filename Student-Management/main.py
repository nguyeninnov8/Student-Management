import lib

def _menu_():
    while True:
        print("======== Choose your choice ========")
        print("1. Add new warehouse to system")
        print("2. Remove warehouse")
        print("3. Update costs between warehouses")
        print("4. Find optimal cost between warehouses")
        print("5. Display warehouses list")
        print("6. Display Transportation Network")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            # Call function to add new warehouse
            pass
        elif choice == "2":
            # Call function to remove warehouse
            pass
        elif choice == "3":
            # Call function to update costs between warehouses
            pass
        elif choice == "4":
            # Call function to find optimal cost between warehouses
            pass
        elif choice == "5":
            # Call function to display warehouses list
            pass
        elif choice == "6":
            # Call function to display transportation network
            pass
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

# Example usage
_menu_()

