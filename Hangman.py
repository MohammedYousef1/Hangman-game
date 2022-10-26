import random
import Hangman_ASCII_Art
import Hangman_Wordlist
import pyfiglet

HANGMAN = pyfiglet.figlet_format("HANGMAN")
print(HANGMAN)

random_word = random.choice(Hangman_Wordlist.word_list) # Random word from the wordlist

guess_word = [] # We make annonymous word in the list
for _ in random_word:
    guess_word.append('_') # Add underscore until the same length of the random word

num_of_lives = 0 # Counter of number of lives
end_of_game = False # Condition for the while loop


while(not end_of_game):
    guess_letter = input("Enter your guess --> ").lower() # We let the user make a guess
    
    
    if(guess_letter in guess_word): # Check if he put the same letter twice
        print(f"You already used letter {guess_letter}")
    
    for position in range(len(random_word)): # We need to get the position of the letter to replace it with the guess_word list at the same position of the random word
        if(guess_letter == random_word[position]):
            guess_word[position] = guess_letter # Replace the underscore with the letter
    if(guess_letter not in random_word): # if its not true we show the hangman picture and increase the num of lives
        print(Hangman_ASCII_Art.Hangman[num_of_lives])
        num_of_lives += 1

    print("".join(guess_word)) # print the guess word

    if('_' not in guess_word): # Check if there is no underscore 
        end_of_game = True # Change the condition to True
        Won = pyfiglet.figlet_format("YOU WON") # ASCII ART
        print(Won) # He won
    if(num_of_lives == 7): # Check if its reach maximum number of lives
        end_of_game = True # Change the condition to True
        Lost = pyfiglet.figlet_format("YOU LOST") # ASCII ART
        print(Lost)
        print(f"The choosen word is {random_word}") # He lost