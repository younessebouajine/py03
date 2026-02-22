#!/usr/bin/env python3

def players_dict() -> dict:
    return {
        "alice_player": {
            "name": "alice",
            "score": 2300,
            "active": True,
            "active_region": "north",
            "achievements": 5,
            "achiev": "boss_slayer",
            "active_regions": "north"
        },
        "bob_player": {
            "name": "bob",
            "score": 1800,
            "active": True,
            "active_region": "east",
            "achievements": 3,
            "achiev": "level_10",
            "active_regions": "east"
        },
        "charlie_player": {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "active_region": "central",
            "achievements": 7,
            "achiev": "first_kill",
            "active_regions": "central"
        },
        "diana_player": {
            "name": "diana",
            "score": 2050,
            "active": False,
            "active_region": "",
            "achievements": 0,
            "achiev": "first_kill",
            "active_regions": "north"
        }
    }


def list_comprehension_examples(players: dict) -> None:
    print("\n=== List Comprehension Examples ===")

    high_scorers = [
        players[key]["name"]
        for key in players
        if players[key]["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [
        players[key]["score"] * 2
        for key in players
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        players[key]["name"]
        for key in players
        if players[key]["active"]
    ]
    print(f"Active players: {active_players}")


def dict_comprehension_examples(players: dict) -> None:
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        p["name"]: p["score"]
        for p in players.values()
        if p["active"]
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([p for p in players.values() if p["score"] >= 2000]),
        "medium": len([p for p in players.values()
                       if 1800 <= p["score"] < 2100]),
        "low": len([p for p in players.values() if p["score"] <= 1800]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        p["name"]: p["achievements"]
        for p in players.values()
        if p["active"]
    }
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_examples(players: dict) -> None:
    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players.values()}
    print(f"Unique players: {unique_players}")

    unique_achievements = {p["achiev"] for p in players.values()}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["active_regions"] for p in players.values()}
    print(f"Active regions: {active_regions}")


def combined_analysis(players: dict) -> None:
    print("\n=== Combined Analysis ===")

    print(f"Total players: {len(players)}")

    total = sum([p["achievements"] for p in players.values()])
    total_unique_achievements = total
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = sum([p["score"] for p in players.values()]) / len(players)
    print(f"Average score: {average_score}")

    top_player = max(
        [(p["name"], p["score"], p["achievements"]) for p in players.values()],
        key=lambda x: x[1]
    )
    message = (
        f"Top performer: {top_player[0]} "
        f"({top_player[1]} points, {top_player[2]} achievements)"
    )
    print(message)


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===")
        players = players_dict()

        list_comprehension_examples(players)
        dict_comprehension_examples(players)
        set_comprehension_examples(players)
        combined_analysis(players)
    except Exception as e:
        print(f"Error: {e}")
