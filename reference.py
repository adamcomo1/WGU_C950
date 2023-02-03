import csv, time, json, pprint, datetime, os, sys

print("Demo")

class Truck:
    pass

truck1 = Truck()
truck1.mileage = 0.0
truck1.address = "HUB"
truck1.package = [1,2,3,4]
truck1.departure_time = truck1.current_time = datetime.timedelta(hours=8)

class Package:
    def update_status(self, input_time):
        if input_time < self.departure_time:
            self.status = "at hub"
        elif input_time < self.delivered_time:
            self.status = "en route"
        else:
            self.status = "delivered at %s" % self.delivered_time

1. load data

2. assign packages to truck

3. sort packages into a route

4. simulate delivery route

5. user interface for verification

# distances

if distances[offset1][offset2] == "":
    distances[offset2][offset1]

rowData = distance[row]
distance = rowData[col]

# Dijkstra's - great for edge weights, toll roads

edges = {
    vertex1(hub): [ vertex2(195 W oakland), vertex3(police station), ],
    vertex2: [],
}

# Nearest Neighbor - great for quicker deliveries

nearest_package = None
nearest_distance = 9999
for package in truck.packages:
    if distance(truck.address, package.address) < nearest_distance:
        nearest_distance = distance(truck.address, package.address)
        nearest_package = package
print(nearest_package)