class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, ", end="")
        print(f"{self._age} days old")

    def grow(self, amount: float):
        self._height += amount

    def age_up(self, days: int):
        self._age += days

def main():
    print("=== Garden Plant Types ===")
    
    # 測試 Flower
    print("=== Flower")


if __name__ == "__main__":
    main()