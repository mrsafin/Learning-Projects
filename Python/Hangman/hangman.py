import random

print("Welcome to Hangman game!")
print("You have 5 guesses")

word_list = ["defeated", "petite", "range", "valuable", 
             "dolls", "dog", "crabby", "owe", "cross", 
             "dizzy", "wander", "gleaming", "wrathful",
             "careful", "doll", "sisters", "middle", 
             "sprout", "separate", "coil"]

word = random.choice(word_list)

hint_word = []
for letter in word:
    hint_word += '_'
print(hint_word)

guesses = 5
game_over = False
while not game_over:
    guessed_letter = input("Guese a letter: ").lower()
    for i in range(len(word)):
        if word[i] == guessed_letter:
            hint_word[i] = guessed_letter
    print(hint_word)

    if guessed_letter not in word:
            guesses -= 1
            print("Gueses left ", guesses)

    if guesses == 0:
         print("You lose")
         game_over = True

    if '_' not in hint_word:
         print("You win!")
         game_over = True
