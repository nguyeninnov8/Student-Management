import A_R_WAREHOUSE
import WAREHOUSE_CLASS

def write_to_file():
    with open("Warehouses.txt", "w") as f:
        for warehouse in A_R_WAREHOUSE.warehouses_list:
            f.write(f"{warehouse.name},{warehouse.location},{warehouse.capacity}\n")
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                f.write(f"{dest_warehouse},{cost}\n")

            f.write("\n")

def delete_from_file():
    with open("Warehouses.txt", "w") as f:
        f.truncate(0)

def update_into_file():
    delete_from_file()
    write_to_file()

def read_from_file():
    with open("Warehouses.txt", "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            name, location, capacity = lines[i].strip().split(",")
            new_warehouse = WAREHOUSE_CLASS.Warehouse(name, location, int(capacity))
            A_R_WAREHOUSE.warehouses_list.append(new_warehouse)
            i += 1
            while i < len(lines) and lines[i].strip():
                if len(lines[i].strip().split(",")) == 2:
                    dest_warehouse, cost = lines[i].strip().split(",")
                    new_warehouse.add_transportation_cost(dest_warehouse, int(cost))
                else:
                    print(f"Ignoring line {i + 1} due to invalid format")
                i += 1  
            i += 1

