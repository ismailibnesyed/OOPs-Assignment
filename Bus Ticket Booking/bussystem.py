from bus import *
from passenger import *

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