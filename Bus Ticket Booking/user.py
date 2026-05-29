def admin_menu(system):
    while True:

        print("\n-----Admin Menu----\n")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")
        print("-----------------------")

        choice = int(input("Select Option : "))

        # Add Bus
        if choice == 1:

            number = input("Enter Bus Number : ")
            route = input("Enter Route : ")
            seats = int(input("Enter Total seats : "))

            system.add_bus(number, route, seats)

        # View Buses
        elif choice == 2:
            system.show_buses()

        # Logout
        elif choice == 3:
            print("Logout Successfully!!!")
            break

        else:
            print("Invalid Keyword! Enter Valid keyword.")


def admin_login(system, admin):

    print("\n----Admin Login----")

    attempts = 0

    while attempts < admin.max_attempts:

        entered_username = input("Username : ")
        entered_password = input("Password : ")

        if admin.login(entered_username, entered_password):

            print("Login Successfully")
            admin_menu(system)
            return

        else:

            attempts += 1
            remain = admin.max_attempts - attempts

            if remain > 0:
                print(f"Try again. You can try {remain} times")

            else:
                print("Too many attempts.")
                break


def user_menu(system, admin):

    while True:

        print("\nBangladesh Bus System\n")

        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        print("\n")

        choice = int(input("Select Option : "))

        # Admin Login
        if choice == 1:
            admin_login(system, admin)

        # Book Ticket
        elif choice == 2:

            bus_number = input("Enter Bus Number : ")
            name = input("Enter Your Name : ")
            phone = input("Enter Your Phone : ")

            system.book_ticket(bus_number, name, phone)

        # View Buses
        elif choice == 3:
            system.show_buses()

        # Exit
        elif choice == 4:
            print("Thank You!!! Exit Successfully.")
            break

        else:
            print("Invalid Keyword! Please select 1 to 4.")