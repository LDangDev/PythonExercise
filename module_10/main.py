# 10. Association
# Ex 1


class Elevator:
    total_move = 0

    def __init__(self, number_bottom, number_top, current_floor=1):
        self.number_bottom = number_bottom
        self.number_top = number_top
        self.current_floor = current_floor

    def go_to_floor(self, target_floor):
        print(f"You are at: {self.current_floor }")
        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
                print(f"You are at: {self.current_floor }")
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()
                print(f"You are at: {self.current_floor }")
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


h = Elevator(1, 6)

h.go_to_floor(6)
h.go_to_floor(3)
