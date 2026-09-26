"""Lab 2: FizzBuzz, movie budgets, and inheritance/overriding."""


def fizzbuzz(limit: int = 100) -> list[str]:
    """Return FizzBuzz results from 1 through limit."""
    results = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))
    return results


def analyze_movie_budgets(movies: list[tuple[str, float]]) -> tuple[float, list[tuple[str, float]], int]:
    """Return average budget, above-average movies with excess, and count."""
    if not movies:
        raise ValueError("The movie list cannot be empty.")
    average = sum(budget for _, budget in movies) / len(movies)
    above_average = [(title, budget - average) for title, budget in movies if budget > average]
    return average, above_average, len(above_average)


class Vehicle:
    def start_engine(self) -> str:
        return "The vehicle engine starts."


class Car(Vehicle):
    def start_engine(self) -> str:
        return "The car engine starts with a key or button."


class Motorcycle(Vehicle):
    def start_engine(self) -> str:
        return "The motorcycle engine starts with a kick or electric starter."


def main() -> None:
    print("FizzBuzz:")
    print(" ".join(fizzbuzz()))

    movies = [
        ("Inception", 160),
        ("Avatar", 237),
        ("The Dark Knight", 185),
        ("Get Out", 4.5),
        ("Interstellar", 165),
    ]
    average, above_average, count = analyze_movie_budgets(movies)
    print(f"\nAverage movie budget: ${average:.2f} million")
    for title, excess in above_average:
        print(f"{title} exceeds average by ${excess:.2f} million")
    print(f"Movies above average: {count}")

    print("\nVehicle inheritance test:")
    for vehicle in (Car(), Motorcycle()):
        print(vehicle.start_engine())


if __name__ == "__main__":
    main()
