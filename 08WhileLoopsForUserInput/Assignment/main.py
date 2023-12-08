import random

def number_guesser():
    random = random.randint(1, 10)
    correct = False

    while correct == False:
        guess = int(input("Input your guess."))
        if guess == random:
            correct = True
            print("Correct!")
        elif guess > random:
            print("too high")
        elif guess < random:
            print("too low")


def number_guesser_with_lives():
    import random
    random = random.randint(1, 10)
    correct = False
    lives = 3

    while correct == False:
        guess = int(input("Input your guess."))
        if guess == random:
            correct = True
            lives = 3
            print("Correct!")
        elif guess > random:
            print("too high")
            lives = lives - 1
            print("lives Left:",lives)
        elif guess < random:
            print("too low")        
            lives = lives - 1
            print("lives Left:",lives)
        else:
            print("invalid Input")
        if lives == 0:
            correct = True
def vending_machine():
    amount_due = 50
    paid = False
    coin = 0
    change = 0
    while paid == False:
        print("Ammount Due:",amount_due)
        coin = int(input("please enter a coin: "))
        if coin == 5:
            amount_due = amount_due - 5
        elif coin == 10:
            amount_due = amount_due - 10
        elif coin == 25:
            amount_due = amount_due - 25
        else:
            print ("invalid coin")
        if amount_due == 0:
            paid = True
            print("Thank You!")
        if amount_due < 0:
            paid = True
            change = abs(amount_due)
            print("Thank You! Your change will be:", change)

        
print(vending_machine())


