#!/usr/bin/env python3
import sys


class RedundantError(Exception):
    def __init__(self, message = "Reundant item"):
        super().__init__(message)


def check_argument(args: list[str]) -> dict[str, int]:
    inventory = {}
    for arg in args:
        try:
            colon = arg.index(':', 1, -1)
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        
        if arg[:colon] in inventory:
            try:
                raise RedundantError
            except RedundantError as e:
                print(f"{e} '{arg[:colon]}' - discarding")
                continue
        
        try:
            inventory[arg[:colon]] = int(arg[colon + 1:])
        except ValueError as e:
            print(f"Quantity error for '{arg[:colon]}': {e}")
    
    return inventory
    

def main():
    print("=== Inventory System Analysis ===\n")
    inventory = check_argument(sys.argv[1:])
    
    print(f"\nGot inventory: {inventory}\n")
    items = list(inventory.keys())
    print(f"Item list: {items}\n")
    
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    if total == 0:
        return
    
    for item, qty in inventory.items():
        percentage = round(qty / total * 100, 1)
        print(f"Item {item} represents {percentage}%")
    
    most = max(inventory, key=inventory.get)
    least = min(inventory, key=inventory.get)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    
    inventory.update({'magic_item': 1})
    print(f"\nUpdated inventory: {inventory}")


if __name__ == "__main__":
    main()
    