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