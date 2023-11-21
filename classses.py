class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_running = True
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_running = False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")


# Example usage:
my_car = Car(make="Toyota", model="Camry", year=2022)

# Start the car
my_car.start()

# Try to start the car again
my_car.start()

# Stop the car
my_car.stop()

# Try to stop the car again
my_car.stop()
