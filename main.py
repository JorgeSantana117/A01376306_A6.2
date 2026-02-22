"""
This module provides a Command Line Interface (CLI) for the Hotel System.
It allows users to interact with Hotel, Customer, and Reservation data.
"""

import os
from managers import HotelManager, CustomerManager, ReservationManager


def main_menu():
    """
    Main entry point for the CLI. Handles top-level navigation.
    """
    data_dir = 'data'

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    hm = HotelManager(os.path.join(data_dir, 'hotels.json'))
    cm = CustomerManager(os.path.join(data_dir, 'customers.json'))
    rm = ReservationManager(os.path.join(data_dir, 'reservations.json'))

    while True:
        print("\n--- Hotel Management System ---")
        print("1. Manage Hotels")
        print("2. Manage Customers")
        print("3. Manage Reservations")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            hotel_menu(hm)
        elif choice == '2':
            customer_menu(cm)
        elif choice == '3':
            reservation_menu(rm, hm)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def hotel_menu(hotel_mgr):
    """
    Sub-menu for Hotel-related operations.
    """
    print("\n-- Hotel Menu --")
    print("a.Create Hotel\nb.Delete Hotel\nc.Display Hotel\nd.Modify Hotel")
    sub_choice = input("Select: ")

    if sub_choice == 'a':
        h_id = input("Hotel ID: ")
        name = input("Name: ")
        loc = input("Location: ")
        try:
            rooms = int(input("Total Rooms: "))
            hotel_mgr.create_hotel(h_id, name, loc, rooms)
        except ValueError:
            print("Error: Total rooms must be a number.")
    elif sub_choice == 'b':
        h_id = input("Hotel ID to delete: ")
        hotel_mgr.delete_hotel(h_id)
    elif sub_choice == 'c':
        h_id = input("Hotel ID to display: ")
        hotel_mgr.display_hotel(h_id)
    elif sub_choice == 'd':
        h_id = input("Hotel ID to modify: ")
        new_name = input("New Name (leave blank to skip): ")
        if new_name:
            hotel_mgr.modify_hotel(h_id, name=new_name)


def customer_menu(cust_mgr):
    """
    Sub-menu for Customer-related operations.
    """
    print("\n-- Customer Menu --")
    print("a. Create Customer\nb. Delete Customer\nc. Display Customer")
    sub_choice = input("Select: ")

    if sub_choice == 'a':
        c_id = input("Customer ID: ")
        name = input("Name: ")
        email = input("Email: ")
        cust_mgr.create_customer(c_id, name, email)
    elif sub_choice == 'b':
        c_id = input("Customer ID to delete: ")
        cust_mgr.delete_customer(c_id)
    elif sub_choice == 'c':
        c_id = input("Customer ID to display: ")
        cust_mgr.display_customer(c_id)


def reservation_menu(res_mgr, hotel_mgr):
    """
    Sub-menu for Reservation-related operations.
    """
    print("\n-- Reservation Menu --")
    print("a. Create Reservation\nb. Cancel Reservation")
    sub_choice = input("Select: ")

    if sub_choice == 'a':
        r_id = input("Reservation ID: ")
        c_id = input("Customer ID: ")
        h_id = input("Hotel ID: ")
        if res_mgr.create_reservation(r_id, c_id, h_id, hotel_mgr):
            print("Reservation Successful!")
        else:
            print("Reservation Failed (Check Hotel ID or Vacancy).")
    elif sub_choice == 'b':
        r_id = input("Reservation ID to cancel: ")
        h_id = input("Associated Hotel ID: ")
        res_mgr.cancel_reservation(r_id, h_id, hotel_mgr)
        print("Reservation Canceled.")


if __name__ == "__main__":
    main_menu()
