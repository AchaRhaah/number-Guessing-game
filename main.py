import random
print("Welcome to the number guessing game!!!")
difficulty=input("type 'easy' or'medium' or 'hard':")
if difficulty=='easy':
    print("I'm thinking of a number between 1 and 50")
    answer=random.randint(1,50)
    attempts=10
else:
    print("I'm thinking of a number between 1 and 100")
    if difficulty=='medium':
        answer=random.randint(1,100)
        attempts = 10
    else:
        answer=random.randint(1,100)
        attempts=5
    

def compare(answer,user_guess):
    if user_guess>answer:
        print("Your guess is high")
    elif user_guess<answer:
        print("Your guess is low")
    else:
        print("YOU WIN")

go_on=False
while not go_on:
    print(f"You have {attempts} attempts\nGuess again")
    user_guess=int(input("guess a number:"))
    compare(answer=answer,user_guess=user_guess)
    if user_guess!=answer:
        attempts-=1
    if attempts==0 or answer==user_guess:
        go_on=True
       
print(f"the number is {answer}")
    
