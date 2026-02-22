class Hotel:
    def __init__(self, hotel_id, name, location, total_rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.occupied_rooms = 0

    def to_dict(self):
        return self.__dict__

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        return self.__dict__

class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        return self.__dict__