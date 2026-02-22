import json
import os
from .models import Hotel, Customer, Reservation

class BaseManager:
    def __init__(self, filename):
        self.filename = filename

    def _load(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError) as e:

            print(f"Error: Invalid data in {self.filename}. {e}")
            return []

    def _save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

class HotelManager(BaseManager):
    def create_hotel(self, hotel_id, name, location, rooms):
        data = self._load()
        data.append(Hotel(hotel_id, name, location, rooms).to_dict())
        self._save(data)

    def delete_hotel(self, hotel_id):
        data = [h for h in self._load() if h['hotel_id'] != hotel_id]
        self._save(data)

    def display_hotel(self, hotel_id):
        hotels = self._load()
        for h in hotels:
            if h['hotel_id'] == hotel_id:
                print(f"Hotel Info: {h}")
                return h
        print("Hotel not found.")
        return None

    def modify_hotel(self, hotel_id, **kwargs):
        data = self._load()
        for h in data:
            if h['hotel_id'] == hotel_id:
                h.update(kwargs)
        self._save(data)

    def reserve_room(self, hotel_id):
        data = self._load()
        for h in data:
            if h['hotel_id'] == hotel_id:
                if h['occupied_rooms'] < h['total_rooms']:
                    h['occupied_rooms'] += 1
                    self._save(data)
                    return True
        return False

    def cancel_room_reservation(self, hotel_id):
        data = self._load()
        for h in data:
            if h['hotel_id'] == hotel_id:
                if h['occupied_rooms'] > 0:
                    h['occupied_rooms'] -= 1
                    self._save(data)
                    return True
        return False