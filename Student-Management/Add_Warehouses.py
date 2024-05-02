import lib

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
    new_warehouse = Warehouse(name, location, capacity)
    warehouses_list.append(new_warehouse)

    for warehouse in warehouses_list:
        dest_warehouse = input(f"Enter destination warehouse for {warehouse.name}: ")
        cost = int(input(f"Enter transportation cost to {dest_warehouse}: "))
        new_warehouse.add_transportation_cost(dest_warehouse, cost)

def remove_warehouse():
    name = input("Enter the name of the warehouse to remove: ")
    global warehouses_list
    warehouses_list = [warehouse for warehouse in warehouses_list if warehouse.name != name]
    for warehouse in warehouses_list:
        warehouse.remove_transportation_cost(name)

def write_to_file():
    
    None

def delete_from_file():
    None

def rewrite_to_file():
    None