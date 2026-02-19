#!/usr/bin/env python3

def achievement_tracker_system(player_alice_achievements: set,
                               player_bob_achievements: set,
                               player_charlie_achievements: set) -> None:
    print("=== Achievement Tracker System ===\n")

    print(f"Player alice achievements: {player_alice_achievements}")
    print(f"Player bob achievements: {player_bob_achievements}")
    print(f"Player charlie achievements: {player_charlie_achievements}")


def achievement_analytics(player_alice_achievements: set,
                          player_bob_achievements: set,
                          player_charlie_achievements: set) -> None:
    print("=== Achievement Analytics ===")

    all_unique_achievements = player_alice_achievements.union(
        player_bob_achievements
    ).union(
        player_charlie_achievements
    )

    print(f"All unique achievements: {all_unique_achievements}")
    print(f"Total unique achievements: {len(all_unique_achievements)}")

    common_to_all_players = player_alice_achievements.intersection(
        player_bob_achievements
    ).intersection(
        player_charlie_achievements
    )

    print(f"Common to all players: {common_to_all_players}\n")

    alice_rare = player_alice_achievements.difference(
        player_bob_achievements
    ).difference(
        player_charlie_achievements
    )

    bob_rare = player_bob_achievements.difference(
        player_alice_achievements
    ).difference(
        player_charlie_achievements
    )

    charlie_rare = player_charlie_achievements.difference(
        player_alice_achievements
    ).difference(
        player_bob_achievements
    )

    rare_achievements = alice_rare.union(bob_rare).union(charlie_rare)
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_vs_bob_common = player_alice_achievements.intersection(
        player_bob_achievements
    )
    print(f"Alice vs Bob common: {alice_vs_bob_common}")

    alice_unique = player_alice_achievements.difference(
        player_bob_achievements
    )
    print(f"Alice unique: {alice_unique}")

    bob_unique = player_bob_achievements.difference(
        player_alice_achievements
    )
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    try:
        player_alice_achievements = {
            'first_kill',
            'level_10',
            'treasure_hunter',
            'speed_demon'
        }

        player_bob_achievements = {
            'first_kill',
            'level_10',
            'boss_slayer',
            'collector'
        }

        player_charlie_achievements = {
            'level_10',
            'treasure_hunter',
            'boss_slayer',
            'speed_demon',
            'perfectionist'
        }

        achievement_tracker_system(
            player_alice_achievements,
            player_bob_achievements,
            player_charlie_achievements
        )

        achievement_analytics(
            player_alice_achievements,
            player_bob_achievements,
            player_charlie_achievements
        )

    except Exception as e:
        print(f"Error: {e}")
