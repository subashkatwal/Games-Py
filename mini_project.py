import random
from collections import Counter

someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word: ")
    for _ in word:
        print('_', end='')
    print()
    
    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = str(input("Enter a letter to guess: "))
            except KeyboardInterrupt:
                print()
                print("Bye! Try again next time ")
                exit()
            except:
                print("Enter only a letter! ")
                continue
            
            if not guess.isalpha():
                print("Enter only a letter ")
                continue
            elif len(guess) > 1:
                print("Enter only a single letter ")
                continue
            
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed:
                    print(char, end='')
                    correct += 1
                else:
                    print('_', end='')
            
            if correct == len(word):
                print("\nThe word is:", word)
                print("Congratulations! You won!")
                break
            
        if chances <= 0 and correct != len(word):
            print("\nYou lost! The word was:", word)
            
    except KeyboardInterrupt:
        print()
        print("Bye! Try again next time ")
