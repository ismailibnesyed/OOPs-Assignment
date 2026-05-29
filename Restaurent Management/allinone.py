# ============================ fooditem.py ============================

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# ============================ menu.py ============================

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print(f'{item_name} item removed.')
        else:
            print(f'{item_name} item not found.')

    def show_menu(self):
        print('**** Menu *******')
        print('Name\tPrice\tQuantity')

        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


# ============================ order.py ============================

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):

        if item in self.items:
            self.items[item] += item.quantity

        else:
            self.items[item] = item.quantity

    def remove(self, item):

        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}


# ============================ restaurent.py ============================

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self, restaurent):

        print("Employee List!!!")

        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)


# ============================ users.py ============================

from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):

        item = restaurent.menu.find_item(item_name)

        if item:

            if quantity > item.quantity:
                print("Item Quantity exceeded!!")

            else:
                item.quantity = quantity
                self.cart.add_item(item)

                print(f'{item_name} item is added successfully')

        else:
            print(f"{item_name} not found")

    def view_cart(self):

        print("**** View Cart *****")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total Price {self.cart.total_price} paid successfully!!! Thank you")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)

        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee(restaurent)

    def add_menu_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

# ============================ main.py ============================

res = Restaurent('Vai Vai Restaurent')


def customer_menu():

    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter your Address : ")

    customer = Customer(
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    while True:

        print(f"Welcome {customer.name}!!")

        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))

        # View Menu
        if choice == 1:
            customer.view_menu(res)

        # Add Item To Cart
        elif choice == 2:

            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))

            customer.add_to_cart(res, item_name, item_quantity)

        # View Cart
        elif choice == 3:
            customer.view_cart()

        # Pay Bill
        elif choice == 4:
            customer.pay_bill()

        # Exit
        elif choice == 5:
            print("Exit Successfully!!! Thank you.")
            break

        else:
            print("Invalid Input. Please Enter correct keyword.")


def admin_menu():

    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter your Address : ")

    admin = Admin(
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    while True:

        print(f"Welcome {admin.name}!!")

        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))

        # Add Item
        if choice == 1:

            item_name = input("Enter New Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))

            item = FoodItem(item_name, item_price, item_quantity)

            admin.add_menu_item(res, item)

        # Add Employee
        elif choice == 2:

            name = input("Enter Employee name : ")
            phone = input("Enter employee Phone Number : ")
            email = input("Enter employee Email id : ")
            address = input("Enter employee Address : ")
            age = input("Enter employee age : ")
            designation = input("Enter employee designation : ")
            salary = int(input("Enter employee salary : "))

            employee = Employee(
                name,
                email,
                phone,
                address,
                age,
                designation,
                salary
            )

            admin.add_employee(res, employee)

        # View Employee
        elif choice == 3:
            admin.view_employee(res)

        # View Item
        elif choice == 4:
            admin.view_menu(res)

        # Delete Item
        elif choice == 5:

            item_name = input("Enter Item Name : ")

            admin.remove_item(res, item_name)

        # Exit
        elif choice == 6:
            print("Exit Successfully!!! Thank you.")
            break

        else:
            print("Invalid Input. Please Enter correct keyword.")


while True:

    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        customer_menu()

    elif choice == 2:
        admin_menu()

    elif choice == 3:
        print("Exit Successfully!!! Thank you.")
        break

    else:
        print("Invalid Input. Enter Valid Keyword.")