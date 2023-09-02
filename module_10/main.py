import random
from tabulate import tabulate

# 10. Association
# Ex 1


class Elevator:
    def __init__(self, number_bottom, number_top, current_floor=1):
        self.number_bottom = number_bottom
        self.number_top = number_top
        self.current_floor = current_floor
        self.total_move = 0

    def go_to_floor(self, target_floor):
        print(f"You are at: {self.current_floor }")
        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
                print(f"You are at: {self.current_floor }")
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()
                print(f"You are at: {self.current_floor } floor")
        else:
            print(f"You are already at {target_floor}")
        print(f"You need {self.total_move} move to reach {target_floor}")
        self.total_move = 0
        return

    def floor_up(self):
        self.current_floor += 1
        self.total_move += 1
        return

    def floor_down(self):
        self.current_floor -= 1
        self.total_move += 1
        return


# Ex 2


class Building:
    def __init__(self, number_bottom, number_top, number_of_elevator):
        self.number_bottom = number_bottom
        self.number_top = number_top
        self.number_of_elevator = number_of_elevator
        self.elevators = []
        for i in range(number_of_elevator):
            new_elevator = Elevator(number_bottom, number_top)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)


b = Building(1, 10, 2)
e1 = Elevator(1, 10)
e2 = Elevator(1, 10)
b.run_elevator(1, 5)
print("----------------------------------")
b.run_elevator(2, 7)


# Ex 3
class Building:
    def __init__(self, number_bottom, number_top, number_of_elevator):
        self.number_bottom = number_bottom
        self.number_top = number_top
        self.number_of_elevator = number_of_elevator
        self.elevators = []
        for i in range(number_of_elevator):
            new_elevator = Elevator(number_bottom, number_top)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(1)


b = Building(1, 10, 2)
e1 = Elevator(1, 10)
e2 = Elevator(1, 10)
b.run_elevator(1, 5)
print("----------------------------------")
b.run_elevator(2, 7)
print("----------------------------------")
b.fire_alarm()


# Ex 4
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


# car_lists = []
# for i in range(10):
#     max_speed = random.randint(100, 200)
#     car = Car(f"ABC-{i + 1}", max_speed)
#     car_lists.append(car)


class Race:
    def __init__(self, name, distance, number_of_car):
        self.name = name
        self.distance = distance
        self.cars = []
        for i in range(number_of_car):
            max_speed = random.randint(100, 200)
            car = Car(f"ABC-{i + 1}", max_speed)
            self.cars.append(car)

    def hour_passed(self):
        # while True:
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            # print(
            #     f"{car.registration_number} accelerate {car.current_speed} has traveled distance: {car.traveled_distance}"
            # )
            # if car.traveled_distance >= self.distance:
            #     break
        # condition to exit while True. This condition will reference to the nearest car where the traveled_distance >= 10000
        # if car.traveled_distance >= self.distance:
        #     print(f"{car.registration_number} has reached 10,000 km.")
        #     break

    def print_status(self):
        table = []
        for car in self.cars:
            table += [
                [
                    f"{car.registration_number}",
                    f"{car.maximum_speed}",
                    f"{car.current_speed}",
                    f"{car.traveled_distance}",
                ]
            ]
        print(
            tabulate(
                table,
                headers=[
                    "registration_number",
                    "maximum_speed (km/h)",
                    "current_speed (km/h)",
                    "traveled_distance (km)",
                ],
                tablefmt="github",
            )
        )

    def race_finished(self):
        for car in self.cars:
            if car.traveled_distance >= self.distance:
                # print(f"traveled distance: {car.traveled_distance}")
                # break (Why place break here and return outside does not work as expected??????)
                return True
        # return True

race = Race("Grand Demolition Derby", 10000, 10)
hour = 0
while True:
    race.hour_passed()
    hour += 1
    # print(f"hour: {hour}")
    if hour % 10 == 0:
        print(f"hour: {hour}")
        print(
            "------------------------------------------------------------------------------------------------------"
        )
        race.print_status()
        print(
            "------------------------------------------------------------------------------------------------------"
        )
    if race.race_finished():
        break
print(f"Grand Demolition Derby Race completed in {hour}")
print(
    "------------------------------------------------------------------------------------------------------"
)
print("Summary of the race:")
print(
    "------------------------------------------------------------------------------------------------------"
)
race.print_status()
print(
    "------------------------------------------------------------------------------------------------------"
)
