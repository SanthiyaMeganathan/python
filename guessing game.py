actual_word="python"
guess=""
guess_count=0
guess_limit=3
outof_guess= False
while guess != actual_word and not(outof_guess):
    if guess_count < guess_limit:
        guess=input("Enter your guess: ")
        guess_count += 1
    else:
        outof_guess=True    

if outof_guess:
    print("You are out of guesses. The word was " + actual_word)
else:
    print("Congratulations! You guessed the word " + actual_word)