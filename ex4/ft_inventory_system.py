#!/usr/bin/env python3
import sys

def inventory_dict(inventory_list: list) -> dict:
    inventory = dict()

    for element in inventory_list:
        name = ""
        quantity_str = ""
        parsing_quantity = False

        for n in element:
            if not parsing_quantity:
                if n == ":":
                    parsing_quantity = True
                else:
                    name += n
            else:
                quantity_str += n

        if name != "" and quantity_str != "":
            inventory.update({name: int(quantity_str)})
    return inventory


def inventory_system_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")

    total_items = 0
    for n in inventory.values():
        total_items += n
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")


def current_inventory(inventory: dict) -> None:
    print("\n=== Current Inventory ===")

    total_items = 0
    for n in inventory.values():
        total_items += n

    for element in inventory.keys():
        quantity = inventory.get(element)
        try:
            potion_pers = (quantity / total_items) * 100
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        print(f"{element}: {quantity} units ({potion_pers:.1f}%)")


def inventory_statistics(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    most_abundant = 0
    for n in inventory.values():
        if most_abundant < n:
            most_abundant = n

    for element in inventory.keys():
        if inventory.get(element) == most_abundant:
            print(f"Most abundant: {element} ({most_abundant} units)")

    least_abundant = 0
    for key in inventory:
        least_abundant = inventory.get(key)
        break

    for n in inventory.values():
        if least_abundant > n:
            least_abundant = n

    for element in inventory.keys():
        if inventory.get(element) == least_abundant:
            print(f"Least abundant: {element} ({least_abundant} units)")


def item_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")

    moderate = dict()
    scarce = dict()

    for item in inventory.keys():
        quantity = inventory.get(item)
        if quantity >= 5:
            moderate.update({item: quantity})
        else:
            scarce.update({item: quantity})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

def management_suggestions(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")
    restock_needed = []

    for item in inventory.keys():
        quantity = inventory.get(item)
        if quantity <= 1:
            restock_needed.append(item)

    print(f"Restock needed: {restock_needed}")

def dictionary_properties_demo(inventory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    dictionary_keys = ""
    for key in inventory.keys():
        dictionary_keys += key + ", "
    dictionary_keys = dictionary_keys[:-2]
    print(f"Dictionary keys: {dictionary_keys}")

    dictionary_values = ""
    for value in inventory.values():
        dictionary_values += str(value) + ", "
    dictionary_values = dictionary_values[:-2]
    print(f"Dictionary values: {dictionary_values}")

    is_in_inventory = False
    for key in inventory.keys():
        if key == "sword":
            is_in_inventory = True
    print(f"Sample lookup - 'sword' in inventory: {is_in_inventory}")

if __name__ == "__main__":
    try:
        inventory_list=sys.argv[1:]
        inventorydict = inventory_dict(inventory_list)
        inventory_system_analysis(inventorydict)
        current_inventory(inventorydict)
        inventory_statistics(inventorydict)
        item_categories(inventorydict)
        management_suggestions(inventorydict)
        dictionary_properties_demo(inventorydict)
    except Exception as e:
        print(f"Error: {e}")
