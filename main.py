import random
from art import logo
print(logo)
print("\nWelcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
number = random.choice(range(1,101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5
guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
while guess != number:
  attempts -= 1
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    break
  
  if guess > number:
    print("Too high.")
    guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
  elif guess < number:
    print("Too low.")
    guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    
print(f"You got it! The answer was {number}.") 
    