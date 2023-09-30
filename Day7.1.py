import random
from word_list import list_of_words
from ascii import stages
from logo import hangman
import os

print(hangman)

choosen_word = random.choice(list_of_words)
display=[]

for letter in choosen_word:
    display+="_"
    
# print(choosen_word)
print(display)

end_of_game = False
lives=6

while not end_of_game:
    guess= input(("Guess a letter: ")).lower()
    os.system('cls')

    for position in range(len(choosen_word)):
        letter = choosen_word[position]

        if guess == letter:
            display[position]=guess

    if guess in display:
       print(f"You have already choosen letter {guess}")    

    if guess not in choosen_word:
       print(f"{guess} is not in the word")
       lives-=1    
       print(f"you have {lives} attempts left")

    print(stages[lives])

    if lives==0:
       end_of_game=True
       print("You lost")
       print(f"The word was {choosen_word}")

    print(display)
    
    if "_" not in display:
     end_of_game = True
     print("You won") 
    
   

