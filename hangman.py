# 1. create a list of words
# 2. have a welcome screen for the player with the stand (? I forget the word for it) drawn out 
# 3. have the computer randomly pick a word
# 4. count the characters in the word and print the corresponding number of on the screen _ _ _ _
# 5. ask the player to guess a letter
# 6. see if the letter is in the word or not
# 7. if the letter is in the word, reveal the letter and it's location
# 8. else print a part of the man's body
# 9. if the user does not guess the word in the amount of body parts, show's a dead man
# 10. asks the user if they want to play again

 # - categories of words
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
 ~O~  |
 /|\  |
 / \  |
      |
=========''']

# user has 7 tries to guess the word

print(HANGMANPICS[0] + "\nWelcome to Hangwoman!\n") 

with open('word_bank.txt') as word_file:
	hangman_words = word_file.readlines()

	secure_random = random.SystemRandom()
	rando_word = secure_random.choice(hangman_words).strip()
	rando_length = len(rando_word)

	print "_ " * rando_length + '\n'

	rando_word_list = list(rando_word)
	# print _ to represent rando_word_list
	# print rando_word_list

	letter_guess = raw_input("What letter would you like to guess? ").lower()
	if letter_guess in rando_word_list:
		print "Yep! That letter is in there!"
		word_display = [letter_guess if x==letter_guess else '_' for x in rando_word_list]
		print word_display #how to print without the quotations and commas

	else:
		print HANGMANPICS[1] + "\n"
		print "_ " * rando_length + "\n\nSorry, guess again."


