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