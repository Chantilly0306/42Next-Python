#!/usr/bin/env python3

class Plant():
    class _Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def log_grow(self):
            self._grow_count += 1

        def log_age(self):
            self._age_count += 1

        def log_show(self):
            self._show_count += 1

        def display(self):
            print(f"Stats: {self._grow_count} grow, {self._age_count}", end="")
            print(f" age, {self._show_count} show")

    def __init__(self, name: str, height: float, age: int):
        self._name = name.capitalize()
        if height < 0:
            print("Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print("Error, age can't be negative")
        else:
            self._age = age
        self._stats: Plant._Stats = self._Stats()

    def get_stats(self):
        self._stats.display()

    def show(self):
        self._stats.log_show()
        print(f"{self._name}: {round(self._height, 1)}cm, ", end="")
        print(f"{self._age} days old")

    def grow(self, growth_rate: float):
        self._stats.log_grow()
        self._height += growth_rate

    def aging(self, days: int):
        self._stats.log_age()
        self._age += days

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._is_bloomed: bool = False

    def bloom(self):
        self._is_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self._seeds_count: int = 0

    def bloom_and_set_seeds(self, seeds: int):
        self.bloom()
        self._seeds_count = seeds

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds_count}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        if trunk_diameter < 0:
            print("Trunk diameter can't be negative")
        else:
            self._trunk_diameter = trunk_diameter
        self._shade_count: int = 0

    def produce_shade(self):
        self._shade_count += 1
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{round(self._height, 1)}cm long and ", end="")
        print(f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def get_stats(self) -> None:
        super().get_stats()
        print(f"{self._shade_count} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int = 0):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow_and_age(self, growth_rate: float, days: int):
        self.grow(growth_rate)
        self.aging(days)
        self._nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def display_stats(plant: Plant):
    plant.get_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("\n=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.aging(20)
    sunflower.bloom_and_set_seeds(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_stats(anon)


if __name__ == "__main__":
    main()
