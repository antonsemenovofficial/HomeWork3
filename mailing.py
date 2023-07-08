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
 
    def sayMailing(self):
        print(self.to_address, self.from_address, self.cost, self.track)


mailing2 = Mailing(1, 2, 5, 112233445566)

mailing2.sayMailing()