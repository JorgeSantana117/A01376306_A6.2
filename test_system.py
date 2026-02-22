"""
Unit tests for the Hotel Management System.
This suite exercises Hotel, Customer, and Reservation management logic.
"""

import unittest
import os
from managers import HotelManager, CustomerManager, ReservationManager


class TestHotelManagement(unittest.TestCase):
    """Test suite for validating CRUD operations and file persistence."""

    def setUp(self):
        """Initialize managers and temporary test filenames."""
        self.h_file = "t_hotels.json"
        self.c_file = "t_customers.json"
        self.r_file = "t_res.json"
        self.hm = HotelManager(self.h_file)
        self.cm = CustomerManager(self.c_file)
        self.rm = ReservationManager(self.r_file)

    def tearDown(self):
        """Clean up temporary JSON files created during testing."""
        for filename in [self.h_file, self.c_file, self.r_file]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_hotel_crud(self):
        """Test creating, modifying, displaying, and deleting a hotel."""
        self.hm.create_hotel("H1", "Test Hotel", "London", 10)
        self.hm.modify_hotel("H1", name="Updated Hotel")
        hotel = self.hm.display_hotel("H1")
        self.assertEqual(hotel['name'], "Updated Hotel")
        self.hm.delete_hotel("H1")
        self.assertIsNone(self.hm.display_hotel("H1"))

    def test_customer_crud(self):
        """Test creating, modifying, displaying, and deleting a customer."""
        self.cm.create_customer("C1", "John", "john@test.com")
        self.cm.modify_customer("C1", name="John Smith")
        customer = self.cm.display_customer("C1")
        self.assertEqual(customer['name'], "John Smith")
        self.cm.delete_customer("C1")
        self.assertIsNone(self.cm.display_customer("C1"))

    def test_reservation_flow(self):
        """Test the logic for booking and canceling rooms."""
        self.hm.create_hotel("H1", "Res Hotel", "Paris", 1)
        # Successfully reserve
        success = self.rm.create_reservation("R1", "C1", "H1", self.hm)
        self.assertTrue(success)
        # Try to reserve when full
        fail = self.rm.create_reservation("R2", "C1", "H1", self.hm)
        self.assertFalse(fail)
        # Cancel
        self.rm.cancel_reservation("R1", "H1", self.hm)
        hotel = self.hm.display_hotel("H1")
        self.assertEqual(hotel['occupied_rooms'], 0)

    def test_invalid_data_handling(self):
        """Test that the system handles corrupted JSON gracefully (Req 5)."""
        with open(self.h_file, 'w', encoding='utf-8') as file:
            file.write("invalid json{")
        # Should print error via Manager logic but not crash
        res = self.hm.display_hotel("H1")
        self.assertIsNone(res)

    def test_delete_nonexistent_hotel(self):
        """Negative Test 1: Deleting a hotel that doesn't exist."""
        # Should not crash even if ID is missing
        self.hm.delete_hotel("NON_EXISTENT")
        self.assertIsNone(self.hm.display_hotel("NON_EXISTENT"))

    def test_modify_nonexistent_customer(self):
        """Negative Test 2: Modifying a customer that doesn't exist."""
        # Logic should skip modification without error
        self.cm.modify_customer("MISSING_CUST", name="No One")
        self.assertIsNone(self.cm.display_customer("MISSING_CUST"))

    def test_cancel_nonexistent_reservation(self):
        """Negative Test 3: Canceling a reservation that doesn't exist."""
        # Should return False or handle gracefully
        result = self.rm.cancel_reservation("FAKE_RES", "H1", self.hm)
        self.assertFalse(result)

    def test_reserve_nonexistent_hotel(self):
        """Creating a reservation for a hotel that doesn't exist."""
        result = self.rm.create_reservation("R1", "C1", "999", self.hm)
        self.assertFalse(result)

    def test_cancel_room_when_zero(self):
        """Canceling a room when occupied_rooms is already 0."""
        self.hm.create_hotel("H2", "Empty Hotel", "City", 10)
        # Should not go into negative numbers
        self.hm.cancel_room_reservation("H2")
        hotel = self.hm.display_hotel("H2")
        self.assertEqual(hotel['occupied_rooms'], 0)


if __name__ == '__main__':
    unittest.main()
