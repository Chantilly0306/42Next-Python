class Plant:
    def __init__(self, name: str, height: float, age: int, rate: float = 0.0):
        self.name = name
        self.height = height
        self.age = age
        self.rate = rate

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self):
        self.height += self.rate

    def aging(self):
        self.age += 1


def main():
    rose = Plant("Rose", 25.0, 30, 0.8)
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for i in range(1, 8):
        rose.grow()
        rose.aging()
        print(f"=== Day {i} ===")
        rose.show()

    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
