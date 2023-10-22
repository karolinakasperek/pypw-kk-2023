class Car:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.speed = 0

    def drive(self):
        self.speed += 10

    def __repr__(self):
        return f"Car({self.registration_number})"


car = Car("WAW-12345432")
car.drive()
print(car)