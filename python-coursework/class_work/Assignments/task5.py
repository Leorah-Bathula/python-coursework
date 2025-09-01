from abc import ABC, abstractmethod

# ------------------ Base Class (Abstraction) ------------------
class Person(ABC):
    def __init__(self, name, email):
        self._name = name                # Protected attribute (Encapsulation)
        self.__email = email             # Private attribute (Encapsulation)

    @abstractmethod
    def get_role(self):
        pass

    def get_contact(self):
        return f"Name: {self._name}, Email: {self.__email}"


# ------------------ Subclasses ------------------
class Customer(Person):
    def __init__(self, name, email, license_no):
        super().__init__(name, email)
        self.license_no = license_no

    def get_role(self):  # Polymorphism
        return "Customer"


class Staff(Person):
    def __init__(self, name, email, staff_id):
        super().__init__(name, email)
        self.staff_id = staff_id

    def get_role(self):  # Polymorphism
        return "Staff"


# ------------------ Supporting Classes ------------------
class Car:
    car_count = 0  # Class attribute (shared by all)

    def __init__(self, car_id, model, rate_per_day):
        self.car_id = car_id
        self.model = model
        self.rate_per_day = rate_per_day
        self.is_available = True
        Car.car_count += 1

    @classmethod
    def total_cars(cls):
        return cls.car_count

    @staticmethod
    def rental_policy():
        return "Cars must be returned within 24 hours of rental end."


class Booking:
    def __init__(self, customer, car, days):
        self.customer = customer
        self.car = car
        self.days = days
        self.total_cost = self.car.rate_per_day * self.days


# ------------------ Controller/Manager Class ------------------
class CarRentalSystem:
    def __init__(self):
        self.customers = []
        self.cars = []
        self.bookings = []
        self.revenue = 0

    def register_customer(self, name, email, license_no):
        customer = Customer(name, email, license_no)
        self.customers.append(customer)
        print(f"Customer {name} registered successfully!")

    def add_car(self, car_id, model, rate):
        car = Car(car_id, model, rate)
        self.cars.append(car)
        print(f"Car {model} added successfully!")

    def rent_car(self, customer_name, car_id, days):
        customer = next((c for c in self.customers if c._name == customer_name), None)
        car = next((c for c in self.cars if c.car_id == car_id and c.is_available), None)

        if customer and car:
            booking = Booking(customer, car, days)
            self.bookings.append(booking)
            car.is_available = False
            self.revenue += booking.total_cost
            print(f"{customer_name} rented {car.model} for {days} days. Total: ${booking.total_cost}")
        else:
            print("Booking failed: Car not available or customer not found.")

    def show_report(self):
        print("\n--- Car Rental Report ---")
        print(f"Total Cars: {Car.total_cars()}")
        print(f"Total Revenue: ${self.revenue}")
        print("Bookings:")
        for b in self.bookings:
            print(f"{b.customer._name} booked {b.car.model} for {b.days} days -> ${b.total_cost}")


# ------------------ CLI (Command Line Interface) ------------------
def main():
    system = CarRentalSystem()

    while True:
        print("\n===== Car Rental System =====")
        print("1. Register Customer")
        print("2. Add Car")
        print("3. Rent Car")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            license_no = input("Enter license number: ")
            system.register_customer(name, email, license_no)

        elif choice == "2":
            car_id = input("Enter Car ID: ")
            model = input("Enter Model: ")
            rate = int(input("Enter Rate per day: "))
            system.add_car(car_id, model, rate)

        elif choice == "3":
            customer_name = input("Enter Customer Name: ")
            car_id = input("Enter Car ID: ")
            days = int(input("Enter No. of Days: "))
            system.rent_car(customer_name, car_id, days)

        elif choice == "4":
            system.show_report()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
