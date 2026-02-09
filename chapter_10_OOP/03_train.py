#Note: Used LLM for the code genration
class Train:
    def __init__(self, train_name, total_seats, fare):
        self.train_name = train_name       # Name of the train
        self.total_seats = total_seats     # Total seats in the train
        self.available_seats = total_seats # Seats available initially
        self.fare = fare                   # Fare per ticket

    # Method to book tickets
    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Invalid number of tickets.")
        elif number_of_tickets > self.available_seats:
            print(f"Only {self.available_seats} seats are available. Cannot book {number_of_tickets} tickets.")
        else:
            self.available_seats -= number_of_tickets
            total_cost = number_of_tickets * self.fare
            print(f"{number_of_tickets} ticket(s) booked successfully. Total cost: ₹{total_cost}")

    # Method to get current seat status
    def get_status(self):
        print(f"Train: {self.train_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

    # Method to get fare information
    def get_fare_info(self):
        print(f"Fare per ticket in {self.train_name}: ₹{self.fare}")




# Create a Train object
train1 = Train("Rajdhani Express", 100, 1500)
train2 = Train("Pakistani fast", 150, 1400)

# Check status and fare
train1.get_status()
train1.get_fare_info()

# Book some tickets
train1.book_ticket(3)
train1.book_ticket(200)  # trying to book more than available

# Check status again
train1.get_status()
train2.get_status()