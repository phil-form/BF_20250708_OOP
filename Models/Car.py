class Car:
    speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"Accelerated to {self.speed} km/h")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Slowed down to {self.speed} km/h")

car = Car()
car2 = Car()
print(car.__dict__)
print(car2.__dict__)

car.accelerate(50)
print(car.__dict__)
print(car2.__dict__)
