import sys


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

    print("Hello, welcome to hangman. Please enter a word/phrase for a player to try and guess.")
    word_to_be_guessed = input()
    letters_left = [char for char in word_to_be_guessed if char != " "]
    correct_letters = ["_" if char != " " else char for char in word_to_be_guessed]

    while True:
        if guesses_left == 0:
            print("Game over!")
            sys.exit()
        if not letters_left:
            print("You win! The word/phrase was: " + word_to_be_guessed)
            sys.exit()
        display_hangman(guesses_left, letters_used, correct_letters)
        print("Guess a letter you think the word/phrase contains")
        letter_guessed = input()
        if letter_guessed in word_to_be_guessed:
            print("Correct, that letter is contained in the word/phrase!")
            nth_letter = 1
            while True:
                index_of_letter = find_nth(word_to_be_guessed, letter_guessed, nth_letter)
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
