"""Tip Splitter - split a bill (with tip) evenly among friends."""


def split_bill(total, tip_percent, people):
    """Return how much each person pays, rounded to 2 decimals."""
    if total < 0:
        raise ValueError("Total can't be negative.")
    if tip_percent < 0:
        raise ValueError("Tip can't be negative.")
    if people < 1:
        raise ValueError("You need at least 1 person.")
    tip = total * tip_percent / 100
    return round((total + tip) / people, 2)


def ask_number(prompt, cast=float):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== Tip Splitter ===")
    total = ask_number("Bill total: ")
    tip = ask_number("Tip % (e.g. 10): ")
    people = ask_number("Number of people: ", int)
    try:
        share = split_bill(total, tip, people)
    except ValueError as e:
        print(f"Error: {e}")
        return
    print(f"Each person pays: {share:.2f}")


if __name__ == "__main__":
    main()
