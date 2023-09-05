import random

words = ['apple', 'lemon', 'grape', 'knife', 'kitty']
word_to_guess = random.choice(words)
attempts = 0
max_attempts = 6
guessed_letters = []
guessed_words=set()

while attempts < max_attempts:
    guess = input("Guess a word: ").lower()

    if guess in guessed_words:
        print("You already guessed that word. Try a different one.")
        continue
    
    if len(guess) != 5:
        print("Invalid input. Please enter a 5-letter word.")
        continue
    
    guessed_words.add(guess)

    
    correct_letters = 0
    correct_letter_positions = []  # Store the positions of correctly guessed letters
    
    for i in range(5):
        if guess[i] == word_to_guess[i]:
            guessed_letters.append(guess[i])
            correct_letter_positions.append(i)
            correct_letters += 1
    
    # Provide feedback on correct and incorrect letters
    feedback = ['_' if i not in correct_letter_positions else guess[i] for i in range(5)]
    print(f"Feedback: {' '.join(feedback)}")
    print(f"Correct letters: {correct_letters}/5")

    if correct_letters == 5:
        print(f"Congratulations! You guessed: {guess}")
        break
    
    attempts += 1

if attempts >= max_attempts:
    print(f"Sorry, you've reached the maximum number of attempts. The word was: {word_to_guess}")
