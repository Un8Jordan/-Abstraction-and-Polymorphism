class BMW:
    def fuel_type(self):
        print("BMW uses petrol or diesel.")

    def max_speed(self):
        print("BMW max speed is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses petrol.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")

# Polymorphism demonstration
def car_details(car):
    car.fuel_type()
    car.max_speed()

# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Use polymorphism
print("BMW Details:")
car_details(bmw_car)
print("\nFerrari Details:")
car_details(ferrari_car)