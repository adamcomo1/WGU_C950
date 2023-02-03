from datetime import timedelta
import hash_table
from package import Package


class Truck:
    pass

    def add(self, package_id):
        selected_package = packages.search(package_id)
        return selected_package


packages = hash_table.HashTable()
hash_table.loadPackageData('PackageFile.csv', packages)

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

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
