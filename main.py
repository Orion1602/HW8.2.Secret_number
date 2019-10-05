import random
secret = random.randint(1, 20)


for x in range (6):
   guess = int(input("What's the secret number between 0 and 20??"))

   if guess == secret:
        print("You got it!!!! Hooray!!")
        break
   elif guess > secret:
       print("Your guess is not correct.... try something smaller!!")
   elif guess < secret:
       print("Your guess is not correct.... try something bigger!!")
   else:
        print("That was a fail. Try again!!")