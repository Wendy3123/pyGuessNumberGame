from art import logo
print(logo)
import sys
import random 

def setDifficulty():
  if difficultyLevel == 'easy':
    return 10
  else:
    return 5


randNum = random.randint(1,100+1)
print("Welcome to the Number guessing game")
print(f"random number is {randNum}")
# Allow the player to submit a guess for a number between 1 and 100.
print("I'm thinking of a number between 1 and 100.")
difficultyLevel = input("Choose a difficulty level: type 'easy' or 'hard': ").lower()


lives = setDifficulty()
while lives !=0:
  userGuess = int(input('Guess a number between 1 and 100: '))
  if userGuess > 100 or userGuess < 1 :
    print('Invalid input, bye👋🏼')
    sys.exit() 
  else:
    if userGuess > randNum:
      lives -= 1
      print('Too high! Guess again')
      print(f"You have {lives} more lives")
    elif userGuess < randNum:
      lives -= 1
      print('Too Low! Guess again')
      print(f"You have {lives} more lives")
    else:
      print(f'You won! The correct number is {randNum}.')
      sys.exit() 
print('You lost bye!')

