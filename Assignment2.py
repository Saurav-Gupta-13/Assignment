traffic_light = "Green"

speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."
        print(message)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make

    def start_engine(self):
        message = "Car engine started."
        print(message)

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type

    def start_engine(self):
        message = "Bike engine started."
        print(message)

def main():
    car = Car("Toyota")
    bike = Bike("Mountain")
    vehicles = [car, bike]

    for vehicle in vehicles:
        vehicle.start_engine()

    print(f"Global variable traffic light: {traffic_light}")
    print(f"Module level variable speed limit: {speed_limit}")

if __name__ == "__main__":
    main()
