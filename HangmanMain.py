import sys
import os
import random


# Displays number of guesses left, the letter used, and characters correct.
def display_hangman(guesses, letters, correct):
    print("Guesses left: " + str(guesses))
    print('Letters used: ' + ', '.join(letters))
    print(' '.join(correct))


# Finds the nth instance of a string in another string.
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def main():
    guesses_left = 6
    letters_used = []

    # Reads in the word bank of possible choices.
    if not os.path.exists("HangmanWords.txt"):
        print("There is no file with this name, recheck the file and/or its path.")
        sys.exit()
    words_file = open("HangmanWords.txt")
    word_bank = [line.rstrip() for line in words_file]
    words_file.close()

    while True:
        print("Hello, welcome to hangman. Please enter any letter to start or enter 'exit' to leave.")
        if input() == "exit":
            sys.exit()

        # Randomly selects a word from the word bank and removes it from possible selection, in case player replays.
        word_index = random.randint(0, len(word_bank)-1)
        word_to_be_guessed = word_bank[word_index]
        del word_bank[word_index]
        letters_left = [char for char in word_to_be_guessed if char != " "]
        correct_letters = ["_" if char != " " else char for char in word_to_be_guessed]

        while True:
            # First if statement is to test lose condition and the latter is to test win condition
            if guesses_left == 0:
                print("Game over!")
                break
            if not letters_left:
                print("You win! The word/phrase was: " + word_to_be_guessed)
                break
            display_hangman(guesses_left, letters_used, correct_letters)
            print("Guess a letter you think the word/phrase contains")
            letter_guessed = input().lower()
            if letter_guessed in word_to_be_guessed.lower():
                print("Correct, that letter is contained in the word/phrase!")
                # Finds all the indexes of the letters in the word that contain the entered letter and replaces all '_'
                # at the specified indexes with the letter entered.
                nth_letter = 1
                while True:
                    index_of_letter = find_nth(word_to_be_guessed.lower(), letter_guessed, nth_letter)
                    correct_letters[index_of_letter] = letter_guessed
                    letters_left.remove(letter_guessed)
                    if letter_guessed not in letters_left:
                        break
                    nth_letter += 1
            else:
                print("Incorrect, that letter is not contained in the word/phrase!")
                guesses_left -= 1
            letters_used.append(letter_guessed)


if __name__ == '__main__':
    main()
