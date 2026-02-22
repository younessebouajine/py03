#!/usr/bin/env python3

import math


def ft_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def convert_position_to_int(pos: tuple) -> tuple | None:
    x, y, z = pos
    try:
        return (int(x), int(y), int(z))
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error: {e}")


def game_coordinate_system() -> None:
    position_created = ("10", 20, 5)
    try:
        position_created = convert_position_to_int(position_created)
    except ValueError as e:
        print(f"Caught error: {e}")
        position_created = (0, 0, 0)

    first_position = (0, 0, 0)
    print(f"Position created: {position_created}")
    distance = ft_distance(first_position, position_created)
    message = (
        f"Distance between {first_position} "
        f"and {position_created}: {distance:.2f}\n"
    )
    print(message)

    parse_position = "3,4,0"
    print(f"Parsing coordinates: \"{parse_position}\"")
    list_position = [int(x) for x in parse_position.split(',')]
    tuple_position = tuple(list_position)
    print(f"Parsed position: {tuple_position}")
    distance2 = ft_distance(first_position, tuple_position)
    message2 = (
        f"Distance between {first_position} and "
        f"{tuple_position}: {distance2:.1f}\n"
    )
    print(message2)
    invalid_pars = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_pars}\"")
    try:
        list2_position = [int(x) for x in invalid_pars.split(',')]
        tuple2_position = tuple(list2_position)
        print(f"Parsed position: {tuple2_position}")
        distance3 = ft_distance(first_position, tuple2_position)
        message3 = (
            f"Distance between {first_position} "
            f"and {tuple2_position}: {distance3:.1f}\n"
        )
        print(message3)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    players = (3, 4, 0)
    print(f"Player at x={players[0]}, y={players[1]}, z={players[2]}")
    print(f"Coordinates: X={players[0]}, Y={players[1]}, Z={players[2]}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    try:
        game_coordinate_system()
    except Exception as e:
        print(f"Error: {e}")
