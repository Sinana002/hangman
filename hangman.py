import random
#from hangman_words import word_list
#from hangman_art import stages, logo
logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

stages = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    """
]

word_list = [
    "elephant", "giraffe", "python", "hangman", "bicycle",
    "umbrella", "computer", "keyboard", "monitor", "chocolate",
    "sandwich", "notebook", "backpack", "mountain", "airplane",
    "calendar", "kangaroo", "volcano", "microwave", "penguin",
    "sunflower", "pineapple", "whistle", "triangle", "glasses",
    "flashlight", "balloon", "library", "pyramid", "rainbow"
]

print(logo)
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Uncomment this for debugging
# print(f"Psst, the word is: {chosen_word}")

display = ["_"] * word_length
guessed_letters = []

game_over = False

while not game_over:
    print(f"\n{' '.join(display)}")
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        if "_" not in display:
            game_over = True
            print("\nYou won! 🎉")
    else:
        lives -= 1
        print(f"You guessed '{guess}', which is not in the word.")
        if lives == 0:
            game_over = True
            print("\nYou lost. 💀")
            print(f"The word was: {chosen_word}")

    print(stages[lives])
