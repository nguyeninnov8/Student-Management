import WAREHOUSE_CLASS
import sys

warehouses_list = []

def add_warehouse():
    name = input("Enter warehouse's name: ")
    location = input("Enter warehouse's location: ")
    capacity = int(input("Enter capacity of warehouse: "))
    new_warehouse = WAREHOUSE_CLASS.Warehouse(name, location, capacity)
    if len(warehouses_list) == 0:
        new_warehouse = WAREHOUSE_CLASS.Warehouse(name, location, capacity)
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

def update_warehouse():
    name = input("Enter the name of the warehouse to update: ")
    for warehouse in warehouses_list:
        if warehouse.name == name:
            new_capacity = int(input("Enter new capacity of warehouse: "))
            warehouse.capacity = new_capacity
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                new_cost = int(input(f"Enter new transportation cost from {warehouse.name} to {dest_warehouse}: "))
                warehouse.update_transportation_cost(dest_warehouse, new_cost)
                for warehouse in warehouses_list:
                    warehouse.update_transportation_cost(name, new_cost)
            break
    else:
        print("Warehouse not found!")

def display_warehouse_list():
    print("List of warehouses:")
    for warehouse in warehouses_list:
        print(f"Name: {warehouse.name}, Location: {warehouse.location}, Capacity: {warehouse.capacity}")
        print("Transportation costs:")
        for dest_warehouse, cost in warehouse.transportation_costs.items():
            print(f"{dest_warehouse}: {cost}")
        print()

def display_transportation_network():
    print("Transportation network:")
    for warehouse in warehouses_list:
        print(f"Name: {warehouse.name}")
        for dest_warehouse, cost in warehouse.transportation_costs.items():
            print(f"-> {dest_warehouse}: {cost}")
        print()
