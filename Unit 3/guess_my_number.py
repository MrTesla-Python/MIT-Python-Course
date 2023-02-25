import math
print("Please think of a number between 0 and 100!")
high = 100
low = 0
ans = round((low+high)/2)
num_guessed = False
while num_guessed == False:
    print("Is your secret number " + str(ans) + "?")
    answer =  input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == "h":
        high = ans
    elif answer == "l":
        low = ans
    elif answer == "c":
        num_guessed = True
        break
    else:
        print("Sorry, I did no understand your input.")
    ans = math.floor((low+high)/2)
print("Game over. Your secret number was: " + str(ans))
