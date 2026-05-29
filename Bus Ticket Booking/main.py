from bussystem import *
from admin import *
from user import *


system = BusSystem()

admin = Admin("admin", "1234")


# Default buses
system.add_bus("Hanif-01", "Dhaka - Chittagong", 40)
system.add_bus("ENA-01", "Bogura - Dhaka", 35)
system.add_bus("Hanif-02", "Bogura  Chittagong", 45)
system.add_bus("Shah Fatah Ali 01", "Dhaka - Cox's Bazar", 50)
system.add_bus("SR-01", "Dhaka - Cox's Bazar", 50)
system.add_bus("Sadia-01", "Dhaka - Cox's Bazar", 50)


# Run Program
user_menu(system, admin)