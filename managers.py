"""
This module manages the persistence and business logic for the
Hotel Management System, handling JSON file operations.
"""

import json
import os
from models import Hotel, Customer, Reservation


# pylint: disable=too-few-public-methods

class BaseManager:
    """Handles generic file persistence behavior."""

    def __init__(self, filename):
        """Initializes the manager with a specific JSON file path."""
        self.filename = filename

    def _load(self):
        """Loads data from the JSON file. Handles invalid data per Req 5."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, ValueError) as err:
            print(f"Error: Invalid data in {self.filename}. {err}")
            return []

    def _save(self, data):
        """Saves a list of dictionaries to the JSON file."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


class HotelManager(BaseManager):
    """Manages hotel-related operations and data persistence."""

    def create_hotel(self, hotel_id, name, location, rooms):
        """Creates a new hotel and saves it to the file."""
        data = self._load()
        data.append(Hotel(hotel_id, name, location, rooms).to_dict())
        self._save(data)

    def delete_hotel(self, hotel_id):
        """Removes a hotel from the system by its ID."""
        data = [h for h in self._load() if h['hotel_id'] != hotel_id]
        self._save(data)

    def display_hotel(self, hotel_id):
        """Prints and returns hotel information for a specific ID."""
        hotels = self._load()
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                print(f"Hotel Info: {hotel}")
                return hotel
        print("Hotel not found.")
        return None

    def modify_hotel(self, hotel_id, **kwargs):
        """Modifies existing hotel information."""
        data = self._load()
        for hotel in data:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(kwargs)
        self._save(data)

    def reserve_room(self, hotel_id):
        """Decrements available room count when a reservation is made."""
        data = self._load()
        for hotel in data:
            if hotel['hotel_id'] == hotel_id:
                if hotel['occupied_rooms'] < hotel['total_rooms']:
                    hotel['occupied_rooms'] += 1
                    self._save(data)
                    return True
        return False

    def cancel_room_reservation(self, hotel_id):
        """Increments available room count when a reservation is cancelled."""
        data = self._load()
        for hotel in data:
            if hotel['hotel_id'] == hotel_id:
                if hotel['occupied_rooms'] > 0:
                    hotel['occupied_rooms'] -= 1
                    self._save(data)
                    return True
        return False


class CustomerManager(BaseManager):
    """Manages customer-related operations and data persistence."""

    def create_customer(self, customer_id, name, email):
        """Creates a new customer record."""
        data = self._load()
        data.append(Customer(customer_id, name, email).to_dict())
        self._save(data)

    def delete_customer(self, customer_id):
        """Deletes a customer record by ID."""
        data = [c for c in self._load() if c['customer_id'] != customer_id]
        self._save(data)

    def display_customer(self, customer_id):
        """Prints and returns customer information."""
        for customer in self._load():
            if customer['customer_id'] == customer_id:
                print(f"Customer: {customer}")
                return customer
        return None

    def modify_customer(self, customer_id, **kwargs):
        """Modifies existing customer information."""
        data = self._load()
        for customer in data:
            if customer['customer_id'] == customer_id:
                customer.update(kwargs)
        self._save(data)


class ReservationManager(BaseManager):
    """Manages the creation and cancellation of reservations."""

    def create_reservation(self, res_id, cust_id, hotel_id, hotel_mgr):
        """Creates a reservation if the hotel has vacancy."""
        if hotel_mgr.reserve_room(hotel_id):
            data = self._load()
            data.append(Reservation(res_id, cust_id, hotel_id).to_dict())
            self._save(data)
            return True
        return False

    def cancel_reservation(self, res_id, hotel_id, hotel_mgr):
        """Cancels a reservation and updates hotel occupancy."""
        data = self._load()
        if any(r['reservation_id'] == res_id for r in data):
            data = [r for r in data if r['reservation_id'] != res_id]
            self._save(data)
            hotel_mgr.cancel_room_reservation(hotel_id)
            return True
        return False
