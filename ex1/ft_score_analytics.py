#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        message1 = (
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        print(message1)
    else:
        try:
            organize_scores = [int(x) for x in sys.argv[1:]]
            sumscores = sum(organize_scores)
            length = len(organize_scores)
            maximum = max(organize_scores)
            minimum = min(organize_scores)
            average_score = sumscores / length

            print(f"Scores processed: {organize_scores}")
            print(f"Total players: {length}")
            print(f"Total score: {sumscores}")
            print(f"Average score: {average_score}")
            print(f"High score: {maximum}")
            print(f"Low score: {minimum}")
            print(f"Score range: {maximum - minimum}")

        except ValueError:
            message2 = (
                "Error: Invalid input detected!"
                "All scores must be valid numbers."
            )
            print(message2)
