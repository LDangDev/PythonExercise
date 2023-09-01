import random


# 9. Fundamentals of object-oriented programming
# Ex 1
class Car:
    def __init__(
        self, registration_number, maximum_speed, current_speed=0, traveled_distance=0
    ):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance


new_car = Car("ABC-123", 142)
str = f"Plate number is: {new_car.registration_number}, "
str += (
    f"max speed: {new_car.maximum_speed}, current speed is: {new_car.current_speed}, "
)
str += f"traveled distance is: {new_car.traveled_distance}"
print(str)


# Ex 2
class Car:
    def __init__(
        self, registration_number, maximum_speed, current_speed=0, traveled_distance=0
    ):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate(self, change_of_speed):
        if (
            self.current_speed + change_of_speed >= 0
            and self.current_speed + change_of_speed <= self.maximum_speed
        ):
            self.current_speed = self.current_speed + change_of_speed
        return


# Ex 3
class Car:
    def __init__(
        self, registration_number, maximum_speed, current_speed=0, traveled_distance=0
    ):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate(self, change_of_speed):
        if (
            self.current_speed + change_of_speed >= 0
            and self.current_speed + change_of_speed <= self.maximum_speed
        ):
            self.current_speed += change_of_speed
        return

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours
        return


car_lists = []
for i in range(10):
    max_speed = random.randint(100, 200)
    car = Car(f"ABC-{i + 1}", max_speed)
    car_lists.append(car)

while True:
    for car in car_lists:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        print(
            f"{car.registration_number} accelerate {car.current_speed} has traveled distance: {car.traveled_distance}"
        )
        if car.traveled_distance >= 10000:
            break
    # condition to exit while True. This condition will reference to the nearest car where the traveled_distance >= 10000
    if car.traveled_distance >= 10000:
        print(f"{car.registration_number} has reached 10,000 km.")
        break
