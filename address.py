index = ''
city = ''
street = ''
build = ''
flat = ''
class Address:
    def __init__(self, index, city, street, build, flat):
        self.index = index
        self.city = city
        self.street = street
        self.build = build
        self.flat = flat

to_address1 = Address(111000, "Moscow", "Sadovay", 15, 122)
from_address1 = Address(111222, "Moscow", "Sadovay", 22, 333)

print(to_address1)
