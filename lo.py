import random

player_name = input("What is your name? ")

total_score = 0
failed_attempts = 0
plays = 0

print(f"\nWelcome to Python Dice Game, {player_name}!")
print("You have 6 attempts.")
print("Type 'q' to quit the game.\n")

for attempt in range(1, 7):

    choice = input(
        f"Press Enter to throw the dice (attempt {attempt}) "
        "or type q to quit: "
    )

    if choice.lower() == "q":
        print("\nYou quit the game.")
        break

    p_score = random.randint(0, 10)
    plays += 1

    print(f"You scored {p_score} points.")

    total_score += p_score

    if p_score == 0:
        failed_attempts += 1

print("\n--- GAME SUMMARY ---")
print(f"Total score: {total_score}")
print(f"Failed attempts: {failed_attempts}")
print(f"Times played: {plays}")

if total_score >= 18:
    print("Remark: Amazing performance!")
elif total_score >= 10:
    print("Remark: Good effort!")
else:
    print("Remark: Keep practicing!")