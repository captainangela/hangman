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

#things to add: 
  # user has 7 guesses
  # categories of words
  # guess the word in the middle of letter guesses
  # ask the user if they want to play again
  # prevent them from typing multiple letters at a time

import sys
import constants

def update_display (random_word, display, letter):
  for idx, val in enumerate(constants.random_word):
    if letter == val:
      display[idx] = letter
  return display

def check_if_won(word_display):
  if '_' not in word_display:
    print "Wowza! You've got it!"
    new_game()

def opening_display():
  print constants.HANGMANPICS[0] + "\n\033[5;32;40m %s \033[m\n" % "Welcome to Hangwoman!"
  print "_ " * constants.random_length + '\n'

def check_input_errors(guess, guesses):
  if guess in guesses:
    return "You've already guessed that."
  elif guess == 'exit':
    sys.exit()
  elif len(guess) > 1:
    return "You can only guess 1 letter at a time."
  elif not guess.isalpha():
    return "You can only put in letters."
  else:
    return False

def play_hangman():
  num_wrong_guesses = 0
  guesses = {}
  random_word_list = list(constants.random_word)
  word_display = list("_"*constants.random_length)
  while num_wrong_guesses < constants.GUESS_MAX:
    guess = raw_input("What letter would you like to guess? ").lower()
    error = check_input_errors(guess, guesses)
    guesses[guess] = True
    if error:
      print error
      continue
    if guess in random_word_list:
      print constants.HANGMANPICS[num_wrong_guesses] + '\n'
      word_display = update_display(constants.random_word, word_display, guess)
      print word_display #how to print without the quotations and commas
      print "\nYep! That letter is in there!\n"
      check_if_won(word_display)
    elif guess == 'exit':
      sys.exit()  
    else:
      num_wrong_guesses += 1
      print constants.HANGMANPICS[num_wrong_guesses] + "\n"
      print word_display  
      print "\n\nSorry, guess again."
  print "Oh shucks, you've died!"

opening_display()
play_hangman()


