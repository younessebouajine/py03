#!/usr/bin/env python3
import sys


def inventory_dict(inventory_list: list) -> dict:
    inventory = dict()

    for element in inventory_list:
        parts = element.split(":")
        if len(parts) != 2:
            continue

        name, quantity_str = parts
        if name == "" or quantity_str == "":
            continue

        inventory.update({
            name: {
                "name": name,
                "quantity": int(quantity_str),
            }
        })

    return inventory


def inventory_system_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")

    total_items = 0
    for info in inventory.values():
        total_items += info.get("quantity")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")


def current_inventory(inventory: dict) -> None:
    print("\n=== Current Inventory ===")

    total_items = 0
    for info in inventory.values():
        total_items += info.get("quantity", 0)

    for item, info in inventory.items():
        quantity = info.get("quantity")
        if total_items != 0:
            potion_pers = (quantity / total_items) * 100
        else:
            potion_pers = 0
        print(f"{item}: {quantity} units ({potion_pers:.1f}%)")


def inventory_statistics(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")

    most_abundant = 0
    for info in inventory.values():
        quantity = info.get("quantity")
        if most_abundant < quantity:
            most_abundant = quantity

    for item, info in inventory.items():
        if info.get("quantity") == most_abundant:
            print(f"Most abundant: {item} ({most_abundant} units)")
            break

    least_abundant = 0
    for info in inventory.values():
        least_abundant = info.get("quantity")
        break

    for info in inventory.values():
        quantity = info.get("quantity")
        if least_abundant > quantity:
            least_abundant = quantity

    for item, info in inventory.items():
        if info.get("quantity") == least_abundant:
            print(f"Least abundant: {item} ({least_abundant} unit)")
            break


def item_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")

    inventory_categories = {
        "Moderate": dict(),
        "Scarce": dict(),
        "Abundant": dict()
    }

    max_quantity = 0
    for info in inventory.values():
        quantity = info.get("quantity")
        if quantity > max_quantity:
            max_quantity = quantity

    for item, info in inventory.items():
        quantity = info.get("quantity")
        if quantity == max_quantity:
            inventory_categories["Moderate"][item] = quantity
        else:
            inventory_categories["Scarce"][item] = quantity

    print(f"Moderate: {inventory_categories['Moderate']}")
    print(f"Scarce: {inventory_categories['Scarce']}")
    print(f"Abundant: {inventory_categories['Abundant']}")


def management_suggestions(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")

    restock_needed = ""
    first = True

    for item, info in inventory.items():
        quantity = info.get("quantity")
        if quantity <= 1:
            if first:
                restock_needed += item
                first = False
            else:
                restock_needed += ", " + item

    print(f"Restock needed: {restock_needed}")


def dictionary_properties_demo(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")

    dictionary_keys = ""
    first = True
    for key in inventory.keys():
        if first:
            dictionary_keys += key
            first = False
        else:
            dictionary_keys += ", " + key
    print(f"Dictionary keys: {dictionary_keys}")

    dictionary_values = ""
    first = True
    for info in inventory.values():
        value = info.get("quantity")
        if first:
            dictionary_values += str(value)
            first = False
        else:
            dictionary_values += ", " + str(value)
    print(f"Dictionary values: {dictionary_values}")

    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    try:
        inventory_list = sys.argv[1:]
        inventorydict = inventory_dict(inventory_list)

        inventory_system_analysis(inventorydict)
        print("")
        current_inventory(inventorydict)
        inventory_statistics(inventorydict)
        item_categories(inventorydict)
        management_suggestions(inventorydict)
        dictionary_properties_demo(inventorydict)
    except Exception as e:
        print(f"Error: {e}")
