# Lab 2: FizzBuzz, Movie Budgets and OOP


print("FizzBuzz")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


movies = [
    ("Inception", 160),
    ("Avatar", 237),
    ("The Dark Knight", 185),
    ("Get Out", 4.5),
    ("Interstellar", 165)
]

total = 0
for title, budget in movies:
    total = total + budget

average = total / len(movies)
print("\nAverage movie budget:", round(average, 2), "million")

count = 0
for title, budget in movies:
    if budget > average:
        difference = budget - average
        print(title, "is above average by", round(difference, 2), "million")
        count = count + 1

print("Number of movies above average:", count)


class Vehicle:
    def start_engine(self):
        print("The vehicle engine has started.")


class Car(Vehicle):
    def start_engine(self):
        print("The car engine has started.")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("The motorcycle engine has started.")


print("\nOOP example")
car = Car()
motorcycle = Motorcycle()
car.start_engine()
motorcycle.start_engine()
