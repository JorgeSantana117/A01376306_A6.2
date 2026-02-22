"""
This module contains the data models for the Hotel Management System.
"""


class Hotel:
    """
    Represents a Hotel entity.
    """

    def __init__(self, hotel_id, name, location, total_rooms):
        """Initializes a Hotel instance."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.occupied_rooms = 0

    def to_dict(self):
        """Returns the dictionary representation of the hotel."""
        return self.__dict__


class Customer:
    """
    Represents a Customer entity.
    """

    def __init__(self, customer_id, name, email):
        """Initializes a Customer instance."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Returns the dictionary representation of the customer."""
        return self.__dict__


class Reservation:
    """
    Represents a Reservation entity.
    """

    def __init__(self, reservation_id, customer_id, hotel_id):
        """Initializes a Reservation instance."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Returns the dictionary representation of the reservation."""
        return self.__dict__