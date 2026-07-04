# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways


import random
class train:

    def __init__(self,train_NO):
        self.train_NO=train_NO

    def book_tickets(self, source , destination):
        print(f"ticket is booked in train number: {self.train_NO} from {source} to {destination}")

    def get_status(self):
        print(f"train number {self.train_NO} is running on time")


    def get_fare_info(self , source , destination):
        print(f"Ticket fare in train number: {self.train_NO} from {source} to {destination} is {random.randint(100,1000)}")

T=train(random.randint(100000,999999))
T.book_tickets("khanpur","delhi")
T.get_status()
T.get_fare_info("khanpur","delhi")

