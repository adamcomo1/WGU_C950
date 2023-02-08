import csv
from datetime import timedelta

from truck import packages, truck2, truck3
from truck import truck1

package_status_list = []


def load_distance_data(filename):
    distance_array = []
    with open(filename) as distances:
        distance_data = csv.reader(distances, delimiter=',')
        for distance in distance_data:
            distance_array.append(distance)
        return distance_array


def deliver_package(truck):
    for i in truck.packages_loaded:
        current_package = packages.search(i)
        distance_traveled = 0.0
        if truck.address == current_package.address:
            distance_traveled = 0.0
        else:
            distance_traveled = get_distance(truck.address, current_package.address)
        truck.mileage += distance_traveled
        truck.address = current_package.address
        # print(truck.address)
        # current_package.status = 'Delivered'
        truck.current_time += timedelta(hours=distance_traveled / 18)
        current_package.delivery_time = truck.current_time
        current_package.departure_time = truck.departure_time
        current_package.truck_number = truck.number
        # print(current_package.package_id, current_package.delivery_time)
        # package_status_list.append([current_package, current_package.status, current_package.delivery_time])
    distance_traveled = get_distance(truck.address, "4001 South 700 East")
    truck.mileage += distance_traveled
    truck.current_time += timedelta(hours=distance_traveled / 18)
    # print(truck.current_time)


def load_address_data(filename):
    address_dict = {}
    with open(filename) as addresses:
        address_data = csv.reader(addresses, delimiter=',')
        counter = 0
        for address in address_data:
            address_dict[address[2]] = counter
            counter += 1
        return address_dict


address_dict = load_address_data('AddressTable.csv')
distance_data = load_distance_data('DistanceTable.csv')


# Will make algorithm here
def get_distance(address, address1):
    index = address_dict[address]
    index1 = address_dict[address1]
    if distance_data[index][index1] == "":
        return float(distance_data[index1][index])
    return float(distance_data[index][index1])


def routing_algorithm(truck):
    old_list = truck.packages_loaded
    new_list = []
    while old_list:
        nearest_package = None
        nearest_distance = 9999
        for package_id in old_list:
            package = packages.search(package_id)
            # print(package_id, 'howdy', package)
            distance = get_distance(truck.address, package.address)
            if distance < nearest_distance:
                nearest_package = package
                nearest_distance = distance
        truck.address = nearest_package.address
        new_list.append(nearest_package.package_id)
        old_list.remove(nearest_package.package_id)
    truck.packages_loaded = new_list


# print('truck 1\n')
# print(truck1.packages_loaded)
routing_algorithm(truck1)
# print(truck1.packages_loaded)

# print('\ntruck 2')
# print(truck2.packages_loaded)
routing_algorithm(truck2)
# print(truck2.packages_loaded)

# print('\ntruck3')
# print(truck3.packages_loaded)
routing_algorithm(truck3)
# print(truck3.packages_loaded)
deliver_package(truck1)
deliver_package(truck2)
deliver_package(truck3)
# print(truck1.mileage + truck2.mileage + truck3.mileage)
t = input('Choice')
if t == 'a':
    package_ids = [int(input('Enter a package ID'))]
if t == 'b':
    package_ids = range(1, 41)
time_input = input('Enter time (Format HH:MM').split(':')
input_time = timedelta(hours=int(time_input[0]), minutes=int(time_input[1]))
for i in package_ids:
    package = packages.search(i)
    if input_time < package.departure_time:
        package.status = "At the Hub"
    elif input_time < package.delivery_time:
        package.status = "En route"
    else:
        package.status = "Delivered %s" % package.delivery_time
    print(package)
