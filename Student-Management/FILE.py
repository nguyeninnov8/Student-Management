import A_R_WAREHOUSE
import WAREHOUSE_CLASS
def write_to_file():
    with open("Warehouses.txt", "w") as f:
        for warehouse in A_R_WAREHOUSE.warehouses_list:
            f.write(f"{warehouse.name},{warehouse.location},{warehouse.capacity}\n")
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                f.write(f"{dest_warehouse},{cost}\n")

def read_from_file():
    with open("Warehouses.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            name, location, capacity = lines[i].strip().split(",")
            new_warehouse = WAREHOUSE_CLASS.Warehouse(name, location, int(capacity))
            A_R_WAREHOUSE.warehouses_list.append(new_warehouse)
            for dest_warehouse, cost in lines[i + 1].strip().split(","):
                new_warehouse.add_transportation_cost(dest_warehouse, int(cost))

def delete_from_file():
    open("Warehouses.txt", "w").close()