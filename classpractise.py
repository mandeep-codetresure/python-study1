class Calculator:

    def __init__(self, number):
        self.number = number
    @staticmethod
    def greet():
        print("welcome user")

    def square(self):
        print(f"square of {self.number} is {self.number **2}")
    def cube(self):
        print(f"Cuberoot of {self.number} is {self.number **3}")
    def squareRoot(self):
        print(f"Squareroot of the number {self.number} is {self.number **0.5}")


a = Calculator(5)
a.greet()
a.square()
a.cube()
a.squareRoot()