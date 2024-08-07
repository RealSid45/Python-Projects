import random
import string
from words import words

def get_valid(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 8
    
    while len(word_letters)>0 and lives>0 :
        
        print("You have", lives, "lives left and used these letters: ", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", " ".join(word_list))
              
        user_letter= input("Guess A Letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives-1
                print("Letter Not Present")
    
        elif user_letter in used_letters:
          print("Already Used Character ")
      
        else:
            print("Invalid Character")
    if lives == 0:
        print("You Died, The Word Was", word)
    else:
        print("You Guessed The Word ",word)
        
hangman()