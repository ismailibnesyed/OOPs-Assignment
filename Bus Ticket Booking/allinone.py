# ============================ bus.py ============================

class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

    def __str__(self):
        return (
            f"{self.number} {self.route} | "
            f"Total : {self.total_seats} | "
            f"Available : {self.available_seats()}"
        )


# ============================ passenger.py ============================

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

    def __str__(self):
        return (
            f"Passenger Name : {self.name} | "
            f"Passenger Phone Number : {self.phone} | "
            f"Passenger Bus : {self.bus.number} | "
            f"Route : {self.bus.route}"
        )


# ============================ bussystem.py ============================

fare = 700


class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print(f"{bus.number} Already existed.")
                return

        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)

        print(f"{new_bus} Bus added Successfully.")

    def book_ticket(self, bus_number, name, phone):

        found_bus = None

        for bus in self.buses:
            if bus.number == bus_number:
                found_bus = bus
                break

        if found_bus is None:
            print(f"{bus_number} is not found")
            return

        if found_bus.book_seat():

            new_passenger = Passenger(name, phone, found_bus)
            self.passengers.append(new_passenger)

            print("\nBangladesh Bus Ticket\n")

            print(f"Name : {name}")
            print(f"Phone : {phone}")
            print(f"Bus : {found_bus.number}")
            print(f"Route : {found_bus.route}")
            print(f"Fare : {fare}")
            print(f"Available Seat : {found_bus.available_seats()}")

        else:
            print(f"Sorry {bus_number} has no seat")

    def show_buses(self):

        if len(self.buses) == 0:
            print("No Buses are available")
            return

        print("\n\nAvailable Buses\n\n")
        print("Number-----------Route----------Available\n")

        for bus in self.buses:
            print(f"{bus.number}-------{bus.route}-------{bus.available_seats()}")

        print("\n")


# ============================ admin.py ============================

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.max_attempts = 3

    def login(self, entered_username, entered_password):

        if (
            self.username == entered_username
            and self.password == entered_password
        ):
            return True

        return False


# ============================ user.py ============================

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


# ============================ main.py ============================

system = BusSystem()

admin = Admin("admin", "1234")


# Default buses
system.add_bus("Hanif-01", "Dhaka - Chittagong", 40)
system.add_bus("ENA-01", "Bogura - Dhaka", 35)
system.add_bus("Hanif-02", "Bogura - Chittagong", 45)
system.add_bus("Shah Fatah Ali-01", "Dhaka - Cox's Bazar", 50)
system.add_bus("SR-01", "Dhaka - Cox's Bazar", 50)
system.add_bus("Sadia-01", "Dhaka - Cox's Bazar", 50)


# Run Program
user_menu(system, admin)