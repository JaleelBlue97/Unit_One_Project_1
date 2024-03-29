"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    random_number = random.randint(0, 10)
    
    
    win_message = "You win it took you {} guesses"
    
    
    header = """---------------------------
Number Guessing Game !!
---------------------------"""
    
    number_of_guesses = 1
    guess = input("Enter your {} guess: ".format(number_of_guesses))
        
    while guess != random_number:      
      
      try:
        guess = int(guess)
      except ValueError:
        print("That input was invalid please try again")
      
      else:
        if guess == random_number:
          print(win_message.format(number_of_guesses))
        else:
          if guess > random_number:
              print("Your guess {} is too high".format(guess))
          elif guess < random_number:
              print("Your guess {} is too low".format(guess))
          
          number_of_guesses += 1
          guess = input("Enter your {} guess: ".format(number_of_guesses)) 
      
      

    print("Game Over. Come Again !")
              
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
