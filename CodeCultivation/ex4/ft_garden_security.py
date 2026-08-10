class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name.capitalize()

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value: float):
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, value: int):
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")


def main():
    rose = Plant("rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-5.0)
    rose.set_age(-10)

    print("Current State: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
