#!/usr/bin/env python3

artifacts = [
    {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
    {'name': 'Fire Staff', 'power': 92, 'type': 'armor'},
    {'name': 'Ice Wand', 'power': 78, 'type': 'weapon'},
]

mages = [
    {'name': 'Casey', 'power': 51, 'element': 'ice'},
    {'name': 'Jordan', 'power': 50, 'element': 'fire'},
    {'name': 'Zara', 'power': 60, 'element': 'lightning'},
    {'name': 'Luna', 'power': 94, 'element': 'fire'},
    {'name': 'Riley', 'power': 53, 'element': 'earth'}
]

spells = ['fireball', 'heal', 'shield']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    power_data = list(map(lambda mage: mage["power"], mages))
    return {
        'max_power': max(mages, key=lambda mage: mage["power"])["power"],
        'min_power': min(mages, key=lambda mage: mage["power"])["power"],
        'avg_power': round(sum(power_data) / len(mages), 2)
    }


def main():
    print("\nTesting artifact sorter...")
    ranking = artifact_sorter(artifacts)
    for i in range(0, len(ranking) - 1):
        print(
            f'{ranking[i]["name"]} ({ranking[i]["power"]} power) comes before'
            f' {ranking[i + 1]["name"]} ({ranking[i + 1]["power"]} power)'
        )

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    print("\nTesting power filter...")
    powerful = power_filter(mages, 60)
    print("The mage who has at least 60 power:")
    for p in powerful:
        print(f'{p["name"]} ({p["power"]} power)')

    print("\nTesting mage stats...")
    for key, value in mage_stats(mages).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
