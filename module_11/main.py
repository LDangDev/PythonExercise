# Ex 1
class Publication:
    def __init__(self, name) -> None:
        self.name = name


class Book(Publication):
    def __init__(self, name, author_name, page_count) -> None:
        self.author_name = author_name
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} (author {self.author_name}, {self.page_count} pages)")


class Magazine(Publication):
    def __init__(self, name, chief_editor) -> None:
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor})")


book = Book("Compartment No. 6", "Rosa Liksom", 192)
megazine = Magazine("Donald Duck", "Aki Hyyppä")
book.print_information()
megazine.print_information()

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
            self.current_speed += change_of_speed
        return

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours
        return


class ElectricCar(Car):
    def __init__(
        self,
        registration_number,
        maximum_speed,
        current_speed=0,
        traveled_distance=0,
        battery_capacity=0,
    ):
        super().__init__(
            registration_number, maximum_speed, current_speed, traveled_distance
        )
        self.battery_capacity = battery_capacity

    def accelerate(self, change_of_speed):
        super().accelerate(change_of_speed)

    def drive(self, hours):
        super().drive(hours)


class Gasoline(Car):
    def __init__(
        self,
        registration_number,
        maximum_speed,
        current_speed=0,
        traveled_distance=0,
        volume_tank=0,
    ):
        super().__init__(
            registration_number, maximum_speed, current_speed, traveled_distance
        )
        self.volume_tank = volume_tank

    def accelerate(self, change_of_speed):
        super().accelerate(change_of_speed)

    def drive(self, hours):
        super().drive(hours)


tesla = ElectricCar("ABC-15", 180, 80, 0, 52.5)
toyota = Gasoline("ACD-123", 165, 90, 0, 32.3)
tesla.drive(3)
toyota.drive(3)
print(f"tesla has driven: {tesla.traveled_distance}")
print(f"toyota has driven: {toyota.traveled_distance}")
