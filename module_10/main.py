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
