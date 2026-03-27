import random
easy_words = ["apple", "banana", "cherry", "date", "elderberry"]
medium_words = ["fig", "grape", "honeydew", "kiwi", "lemon"]
hard_words = ["mango", "nectarine", "orange", "papaya", "quince"]

print("Welcome to the Word Guessing Game!")
print("Choose the difficulty level: Easy, Medium, or Hard")

level = input("Enter the difficulty level:").lower()
if level == "easy":
    secret_word = random.choice(easy_words)
elif level == "medium":
    secret_word = random.choice(medium)
elif level == "hard":
    secret_word = random.choice(hard_words)
else:
    print("Invalid difficulty level. Please choose Easy, Medium, or Hard.")
    secret_word = random.choice(easy_words)
attempts = 0
print("Guess the word:")

while True:
    guess = input("Enter your guess:").lower()
    attempts += 1
    if guess == secret:
        print(f"Congratulations! You guessed the word {secret_word} in {attempts} attempts.")
        break
    hint = ""
    for i in range(len(secret_word)):
        if  i < len(guess) and guess[i] == secret_word[i]:
            hint += secret_word[i]
        else:
            hint += "_"
    print("Hint:", hint)
print("Game over!")




              