# find the even square:

from pickle import FALSE


squares = [num*num for num in range(6) if num % 2 == 0 and num != 0]
squarestr = ", ".join([str(square) for square in squares])

print(squarestr)

# conversion types
numstr = "1, 44, 676, 22"
nlist = numstr.split(",")
numlist = [int(n) for n in nlist]
maxim = max(numlist)
print(maxim)


# zip function
players = ["Joe", "Jeb", "Jim"]
scores = [1, 4, 6]
print(dict(list(zip(players, scores))))

# OOP


# class Car:
#     runs = True
#     wheels = 4

#     def __init__(self, name):
#         self.name = name
#         print(f"You've got a new {self.name}!")

#     def __str__(self):
#         return f"This is a {self.name}"

#     def __repr__(self):
#         return f"Car({self.name})"

#     def start(self):
#         if self.runs:
#             print(f"{self.name} is running!")
#         else:
#             print(f"{self.name} is broken!")


@classmethod
def get_wheels(cls):
    return cls.wheels

# inheritance


class Vehicle:
    runs = True

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def start(self):
        if self.runs:
            print(f"{self.make} is running!")
        else:
            print(f"{self.make} is broken!")


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", wheels=4):
        super().__init__(make, model, fuel)
        self.wheels = wheels


subaru = Car("subaru", "x1")

subaru.start()

print(subaru.wheels)


class Motorcycle(Vehicle):

    def __init__(self, make, model, fuel="gas", wheels=2):
        super().__init__(make, model, fuel)
        self.wheels = wheels


honda = Motorcycle("honda", "650")

print(honda.wheels)
honda.runs = False
honda.start()

# Exceptions:

user_input = "a"

try:
    print(int(user_input))
except Exception as e:
    print("There was an error:", e)

# custom exception


class CustomException(Exception):
    def __init__(self, value):
        message = f"Wrong value: {value}"
        super().__init__(message)


raise CustomException(3)

# library and modules
