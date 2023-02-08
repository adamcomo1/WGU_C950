import csv
import math
from datetime import timedelta

from package import Package


# Hash Map Class

class HashTable:

    # constructor for class with default initial capacity of 10
    # All buckets are initially assigned with an empty list
    def __init__(self, initial_capacity=10):
        # hash table initialized with empty buckets
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # function for inserting new item into the hash table
    def insert(self, key, item):
        # hash functions to determine which bucket the item will be placed in
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # updates the key if it already exists in the table
        for k in bucket_list:
            if k[0] == key:
                k[1] = item
                return True
        # if they key does not exist the item is inserted to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Function for searching for an item using the key in the hash table
    # Return the item if found. If not found, returns none.
    def search(self, key):
        # finds the bucket list where the key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # searches for the key in the identified bucket
        for k in bucket_list:
            if k[0] == key:
                return k[1]
        return None

    # function for deleting items from the hash table using the key

    def delete(self, key):
        # finds the bucket list where the item will be deleted
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # deletes the item form the found bucket list if it is found
        for k in bucket_list:
            if k[0] == key:
                bucket_list.remove([k[0], k[1]])


def loadPackageData(fileName, package_hash):
    with open(fileName) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            pID = int(package[0])
            paddress = package[1]
            pcity = package[2]
            pstate = package[3]
            pzip = package[4]
            pdeadline = package[5]
            pweight = package[6]
            pnote = package[7]
            # print(pID)
            p = Package(pID, paddress, pcity, pstate, pzip, pdeadline, pweight, pnote)
            package_hash.insert(pID, p)


# myHash = HashTable()
# print(myHash.table)

class Package:

    # Constructor for package class
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = 'At Hub'
        self.delivery_time = timedelta()

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, Truck %s" % (self.package_id, self.address, self.city,
                                                                 self.state, self.zip_code, self.deadline,
                                                                 self.weight, self.notes, self.status,
                                                                 self.truck_number)


class Truck:
    pass

    def add(self, package_id):
        selected_package = packages.search(package_id)
        return selected_package


packages = HashTable()
loadPackageData('PackageFile.csv', packages)

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

truck1.number = 1
truck2.number = 2
truck3.number = 3

truck1.packages_loaded = [1, 13, 15, 30, 29, 31, 34, 37, 40, 19, 14, 16, 20]
truck2.packages_loaded = [3, 18, 36, 38, 6, 25, 28, 32, 35, 39, 26, 27, 24]
truck3.packages_loaded = [9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 33]

truck1.address = "4001 South 700 East"
truck2.address = "4001 South 700 East"
truck3.address = "4001 South 700 East"

truck1.mileage = 0.0
truck2.mileage = 0.0
truck3.mileage = 0.0

truck1.departure_time = timedelta(hours=8)
truck2.departure_time = timedelta(hours=9, minutes=5)
truck3.departure_time = timedelta(hours=10, minutes=20)

truck1.current_time = truck1.departure_time
truck2.current_time = truck2.departure_time
truck3.current_time = truck3.departure_time

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
total_truck_mileage = truck1.mileage + truck2.mileage + truck3.mileage
print('\nWelcome to the Delivery Simulator!\n'
      'Simulation Complete.\n'
      'Total Miles Driven: ' + str(total_truck_mileage) + ' Miles \n')
t = ''
while t != 'q':
    t = input('\nWould you like to (Enter letter of selection) \n  '
              'a.) Search a single packages status at a given time. \n'
              '  b.) Search all package statuses at a given time.\n'
              '  q.) Quit Program\n')
    if t == 'a':
        package_ids = [int(input('Enter a package ID\n'))]
    if t == 'b':
        package_ids = range(1, 41)
    if t != 'q':
        time_input = input('Enter time (Format HH:MM) \n').split(':')
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
