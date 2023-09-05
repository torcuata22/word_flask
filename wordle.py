import random
words = ['apple', 'cherry', 'lemon', 'grape', 'banana']
word_to_guess= ''
attempts = 0
max_attempts = 6
guessed_letters = set()

while attempts < max_attempts:
    word_to_guess= random.choice(words)
    guess = input("Guess a word: ").lower()
    if len(guess) != 5:
        print("Invalid input. Please enter a 5-letter word.")
        continue
    if len(guess) == 5 and word_to_guess == guess:
        print(f"Congratulations! You guessed: {word_to_guess}")
    
    correct_letters = 0
    for i in range(5):
        if guess[i] == word_to_guess[i]:
            correct_letters += 1
            print(f"Correct letters: {correct_letters}/5")

        if correct_letters == 5:
            print(f"Congrtulations! You guessed: {guess}")
        
        attempts += 1

        if attempts >= max_attempts:
            print(f"Sorry, you've reached the maximum number of attempts. The word was: {word_to_guess}")


