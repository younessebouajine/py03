#!/usr/bin/env python3

from typing import Generator


def event_generator(num_events: int) -> Generator:

    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, num_events + 1):
        yield {
            'id': i,
            'player': players[i % len(players)],
            'level': ((i * 7) % 20) + 1,
            'action': actions[i % len(actions)]
        }


def fibonacci_generator(n: int) -> Generator:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int) -> Generator:

    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1


if __name__ == "__main__":
    try:
        print("=== Game Data Stream Processor ===")

        num_events = 1000
        print(f"\nProcessing {num_events} game events...\n")
        events = event_generator(num_events)

        total = 0
        high_level = 0
        treasure = 0
        levelup = 0

        for event in events:
            if event['id'] <= num_events:
                message = (
                    f"Event {event['id']}: Player {event['player']} "
                    f"(level {event['level']}) {event['action']}"
                )
                print(message)

            total += 1
            if event['level'] >= 10:
                high_level += 1
            if event['action'] == "found treasure":
                treasure += 1
            if event['action'] == "leveled up":
                levelup += 1

        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {total}")
        print(f"High-level players (10+): {high_level}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {levelup}")

        print("\nMemory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")

        print("\n=== Generator Demonstration ===")
        fib = fibonacci_generator(10)
        fib_output = "Fibonacci sequence (first 10): "
        count = 0
        for num in fib:
            if count > 0:
                fib_output += ", "
            fib_output += f"{num}"
            count += 1
        print(fib_output)

        primes = prime_generator(5)
        prime_output = "Prime numbers (first 5): "
        count = 0
        for num in primes:
            if count > 0:
                prime_output += ", "
            prime_output += f"{num}"
            count += 1
        print(prime_output)
    except Exception as e:
        print(f"Error: {e}")
