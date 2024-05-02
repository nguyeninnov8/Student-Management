import lib

class SupplyChainManager:
    def __init__(self):
        self.warehouses = []

    def add_warehouse(self, name, location, capacity):
        self.warehouses.append(Warehouse(name, location, capacity))

    def add_warehouses(self):
        name = input("Enter warehouse's name: ")
        location = input("Enter warehouse's location: ")
        capacity = int(input("Enter capacity of warehouse: "))
        self.add_warehouse(name, location, capacity)

        # Assuming you want to add transportation cost after adding the warehouse
        for warehouse in self.warehouses:
            dest_warehouse = input(f"Enter destination warehouse for {warehouse.name}: ")
            cost = int(input(f"Enter transportation cost to {dest_warehouse}: "))
            warehouse.add_transportation_cost(dest_warehouse, cost)

    def remove_warehouse(self):
        name = input("Enter the name of the warehouse to remove: ")
        self.warehouses = [warehouse for warehouse in self.warehouses if warehouse.name != name]
        for warehouse in self.warehouses:
            warehouse.remove_transportation_cost(name)

    def update_costs_between_warehouses(self):
        source = input("Enter the name of the source warehouse: ")
        dest = input("Enter the name of the destination warehouse: ")
        new_cost = int(input(f"Enter the new transportation cost from {source} to {dest}: "))
        for warehouse in self.warehouses:
            if warehouse.name == source:
                warehouse.update_transportation_cost(dest, new_cost)

    def find_optimal_cost_between_warehouses(self):
        source = input("Enter the name of the source warehouse: ")
        dest = input("Enter the name of the destination warehouse: ")
        # Implement logic to find optimal cost between warehouses
        pass

    def display_warehouses_list(self):
        print("Warehouses List:")
        for warehouse in self.warehouses:
            print(f"Name: {warehouse.name}, Location: {warehouse.location}, Capacity: {warehouse.capacity}")

    def display_transportation_network(self):
        print("Transportation Network:")
        for warehouse in self.warehouses:
            print(f"Warehouse: {warehouse.name}")
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                print(f"   -> Destination: {dest_warehouse}, Cost: {cost}")