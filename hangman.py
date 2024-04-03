import random

# List of words to choose from
someWords = [
    'apple', 'banana', 'mango', 'strawberry',
    'orange', 'grape', 'pineapple', 'apricot',
    'lemon', 'coconut', 'watermelon', 'cherry',
    'papaya', 'berry', 'peach', 'lychee', 'muskmelon'
]

# Select a random word
word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word: ")
    guessed_word = ['_' if char.isalpha() else char for char in word]
    print(' '.join(guessed_word))
    
    playing = True
    letterGuessed = set()
    chances = len(word) + 2
    
    while chances > 0 and '_' in guessed_word:
        print()
        chances -= 1
        
        try:
            guess = input("Enter a letter to guess: ").lower()
        except KeyboardInterrupt:
            print()
            print("Bye! Try again next time")
            exit()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in letterGuessed:
            print("You've already guessed that letter.")
            continue
        
        letterGuessed.add(guess)
        
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word[i] = char
            print(' '.join(guessed_word))
        else:
            print("Incorrect guess!")
    
    if '_' not in guessed_word:
        print("Congratulations! You won! The word is:", word)
    else:
        print("Sorry, you lost. The word was:", word)
