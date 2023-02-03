from datetime import timedelta


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
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city,
                                                   self.state, self.zip_code, self.deadline,
                                                   self.weight, self.notes)
