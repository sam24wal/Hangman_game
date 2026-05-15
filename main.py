# Program will choose a secret word and indicate how many letters
# Players will choose a letter and will be told if the letters is in the word
# The player will get 6 lives and lose a life each time they guess incorrectly
# They need to guess the word correctly before they run out of lives

from random import choice

words = ["wealthy", "material", "abandoned", "poke", "great", "plug", "continue", "spiffy",
            "omniscient", "afraid", "range", "likeable", "whisper", "plate", "silly", "fresh",
            "zoo", "elite", "hellish", "wave", "distance", "pickle", "deafening", "kind"]

correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters

def ask_letter():
    chosen_letter = ""
    is_valid = False
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while not is_valid:
        chosen_letter = input("Please choose a letter: ")

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            chosen_letter = input("You haven't chosen a correct letter")

    return chosen_letter

def show_new_board(chosen_word):
    hidden_list = []
    for l in chosen_word:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append("-")

    print(" ".join(hidden_list))

def check_letter(chosen_letter, hidden_word, tries, matches):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        matches += 1
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1

    if tries == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return tries, end, matches

def lose():
    print("You lose!")
    print("The correct word was " + word)

    return True

def win(revealed_word):
    show_new_board(revealed_word)
    print("You win!")

    return True

word, unique_letters = choose_word(words)

# While the game is active, we want to call the above functions
while not game_over:
    show_new_board(word)
    print("\n")
    print("Incorrect letters: " + "-".join(incorrect_letters))
    print(f"Tries: {tries}")
    letter = ask_letter()
    tries, over, right_answers = check_letter(letter, word, tries, right_answers)
    game_over = over