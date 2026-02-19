#!/usr/bin/env python3

import sys
import math

def ft_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

def game_coordinate_system() -> None:
    position_created = (10, 20, 5)
    first_position = (0, 0, 0)
    print(f"Position created: {position_created}")
    distance = ft_distance(first_position, position_created)
    print(f"Distance between {first_position} and {position_created}: {distance:.2f}\n")

    parse_position = "3,4,0"
    print(f"Parsing coordinates: \"{parse_position}\"")
    list_position = [int(x) for x in parse_position.split(',')]
    tuple_position = tuple(list_position)
    print(f"Parsed position: {tuple_position}")
    distance2 = ft_distance(first_position, tuple_position)
    print(f"Distance between {first_position} and {tuple_position}: {distance2:.1f}\n")
    
    invalid_pars = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_pars}\"")
    try:
        list2_position = [int(x) for x in invalid_pars.split(',')]
        tuple2_position = tuple(list2_position)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    
    print("\nUnpacking demonstration:")
    print(f"Player at x={tuple_position[0]}, y={tuple_position[1]}, z={tuple_position[2]}")
    print(f"Coordinates: X={tuple_position[0]}, Y={tuple_position[1]}, Z={tuple_position[2]}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    try:
        game_coordinate_system()
    except Exception as e:
        print(f"Error: {e}")