from fooditem import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from order import Order

res = Restaurent('Vai Vai Restaurent')

def customer_menu():
    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter your Address : ")

    customer = Customer(name = name, email= email, phone = phone, address=address)


    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))

        # 1. View Menu
        if choice == 1:
            customer.view_menu(res)
        # 2. Add item to cart
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(res, item_name, item_quantity)
        # 3. View Cart 
        elif choice == 3:  
            customer.view_cart()
        # 4. PayBill
        elif choice == 4: 
            customer.pay_bill()
        # 5. Exit 
        elif choice == 5: 
            print("Exit Succesfully!!! Thank you.")
            break
        # Others 
        else:  
            print("Invalid Input. Please Enter correct keyword.")

def admin_menu():
    name = input("Enter your name : ")
    email = input("Enter your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter your Address : ")

    admin = Admin(name = name, email= email, phone = phone, address=address)


    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))

        # 1. Add New Item
        if choice == 1:
            item_name = input("Enter New Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_menu_item(res, item)

        # 2. Add New Employee
        elif choice == 2:
            name = input("Enter Employee name  : ")
            phone = input("Enter employee Phone Number : ")
            email = input("Enter employee Email id : ")
            address = input("Enter employee Address : ")
            age = input("Enter employee age : ")
            designation = input("Enter employee designation : ")
            salary = int(input("Enter employee salary : "))
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(res, employee)
        # 3. View Employee 
        elif choice == 3:  
            admin.view_employee(res)
        # 4.  View Item
        elif choice == 4: 
            admin.view_menu(res)
        # 5. Delete Item
        elif choice == 5:
            item_name = input("Enter Item Name : ")
            admin.remove_item(res, item_name)
        # 6. Exit 
        elif choice == 6: 
            print("Exit Succesfully!!! Thank you.")
            break
        # Others 
        else:  
            print("Invalid Input. Please Enter correct keyword.")


while True:
    print(f"WelCome ")
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
    else:
        print("Invalid Input. Enter Valid Keyword.")

