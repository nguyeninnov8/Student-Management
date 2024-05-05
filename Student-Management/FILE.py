import A_R_WAREHOUSE
def write_to_file():
    with open("Warehouses.txt", "w") as f:
        for warehouse in A_R_WAREHOUSE.warehouses_list:
            f.write(f"{warehouse.name},{warehouse.location},{warehouse.capacity}\n")
            for dest_warehouse, cost in warehouse.transportation_costs.items():
                f.write(f"{dest_warehouse},{cost}\n")

def delete_from_file():
    open("Warehouses.txt", "w").close()