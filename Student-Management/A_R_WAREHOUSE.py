import WAREHOUSE_CLASS
import sys

warehouses_list = []

def add_warehouse():
    name = input("Enter warehouse's name: ")
    location = input("Enter warehouse's location: ")
    capacity = int(input("Enter capacity of warehouse: "))
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
