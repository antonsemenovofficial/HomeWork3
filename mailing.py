from address import Address

to_address = ''
from_address = ''
cost = ''
track = ''

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
    class Address:
        def __init__(self, index, city, street, build, flat):
            self.index = index
            self.city = city
            self.street = street
            self.build = build
            self.flat = flat


mailing2 = Mailing(1, 2, 5, 112233445566)

print(mailing2)