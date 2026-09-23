#!/usr/bin/env python3
import random


ALL_ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Speed Runner", "Survivor",
    "Treasure Hunter", "First Steps", "Sharp Mind",
    "Unstoppable", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 9)
    return set(random.sample(ALL_ACHIEVEMENTS, amount))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
        
    print(f"All distinct achievements: {set().union(*players.values())}\n")
    print(f"Common achievements: {set.intersection(*players.values())}\n")
    
    for name, achievements in players.items():
        others = set().union(*(o_achi for o_name, o_achi in players.items() 
                               if o_name != name))
        print(f"Only {name} has: {achievements.difference(others)}")
    
    print("\n")
    all_possible = set(ALL_ACHIEVEMENTS)
    for name, achievements in players.items():
        print(f"{name} is missing: {all_possible.difference(achievements)}")
    
    
if __name__ == "__main__":
    main()
    