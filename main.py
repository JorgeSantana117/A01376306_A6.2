import os
from managers import HotelManager, CustomerManager, ReservationManager

def main_menu():
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

def hotel_menu(hm):
    print("\n-- Hotel Menu --")
    print("a. Create Hotel\nb. Delete Hotel\nc. Display Hotel\nd. Modify Hotel")
    sub_choice = input("Select: ")
    
    if sub_choice == 'a':
        h_id = input("Hotel ID: ")
        name = input("Name: ")
        loc = input("Location: ")
        rooms = int(input("Total Rooms: "))
        hm.create_hotel(h_id, name, loc, rooms)
    elif sub_choice == 'b':
        h_id = input("Hotel ID to delete: ")
        hm.delete_hotel(h_id)
    elif sub_choice == 'c':
        h_id = input("Hotel ID to display: ")
        hm.display_hotel(h_id)
    elif sub_choice == 'd':
        h_id = input("Hotel ID to modify: ")
        new_name = input("New Name (leave blank to skip): ")
        if new_name: hm.modify_hotel(h_id, name=new_name)

def customer_menu(cm):
    print("\n-- Customer Menu --")
    print("a. Create Customer\nb. Delete Customer\nc. Display Customer")
    sub_choice = input("Select: ")
    
    if sub_choice == 'a':
        c_id = input("Customer ID: ")
        name = input("Name: ")
        email = input("Email: ")
        cm.create_customer(c_id, name, email)
    elif sub_choice == 'b':
        c_id = input("Customer ID to delete: ")
        cm.delete_customer(c_id)
    elif sub_choice == 'c':
        c_id = input("Customer ID to display: ")
        cm.display_customer(c_id)

def reservation_menu(rm, hm):
    print("\n-- Reservation Menu --")
    print("a. Create Reservation\nb. Cancel Reservation")
    sub_choice = input("Select: ")
    
    if sub_choice == 'a':
        r_id = input("Reservation ID: ")
        c_id = input("Customer ID: ")
        h_id = input("Hotel ID: ")
        if rm.create_reservation(r_id, c_id, h_id, hm):
            print("Reservation Successful!")
        else:
            print("Reservation Failed (Check Hotel ID or Vacancy).")
    elif sub_choice == 'b':
        r_id = input("Reservation ID to cancel: ")
        h_id = input("Associated Hotel ID: ")
        rm.cancel_reservation(r_id, h_id, hm)
        print("Reservation Canceled.")

if __name__ == "__main__":
    main_menu()