class Warehouse:
    def __init__(self, name, location, capacity) -> None:
        self.name = name
        self.location = location
        self.capacity = capacity
        self.transportation_cost = {}
        pass
    
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