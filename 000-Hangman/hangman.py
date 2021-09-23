import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ['horse','elephant','camel']
chosen_word = list(random.choice(word_list))
word_length = len(chosen_word)

lives = 6
#cheating
print(f'the chosen word is {chosen_word}')

#creating blanks
display = []
for _ in range(word_length):
    display += '_'
print(display)

while not end_of_game:
    #getting user input
    user_guess = input("Guess a Letter: ")

    #check if guess is correct 
    for i in range(word_length):
        if chosen_word[i] == user_guess:
            display[i] = user_guess
    print(display)
    #deduct a life if guess is not correct
    if user_guess not in chosen_word:
        lives -= 1
        #End of game if life finished
        if lives == 0:
            print("You Lose, GAME OVER")
            end_of_game = True
    #if there is no more blank, then the user wins
    if "_" not in display:
        print("CONGRATS, You Win!")
        end_of_game = True
    print(stages[lives])