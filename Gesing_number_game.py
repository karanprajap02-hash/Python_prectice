import random
    
def Guessing_game(user):
    win= False
    bot= random.randint(1,100)
    if user.lower() == "play" or user.lower() == "try":
        print("\nRULES:__There are only five attempts__")
        print("     __Guessing is between 1 to 100__\n")

        print("\nEnter the your guesses")
        
        attemps=0
        while attemps<6:
            user_guess=int(input("You:"))
            attemps+=1
            if user_guess == bot:
                print("""\n\n               --------------- BINGO --------------
                                 "YOU WIN"           """)
                win=True
                break
            elif user_guess< bot:
                print("\n               Gussing is less\n")
                print("             Try greater no.")
            else:
                print(""""\n            Guessing is too high
            Try some loo""")
    elif user.lower()=='exit':
        print("Thank You For Playing")
        return
    
    if not win:
        print(f"""\n              -----   THE GAME IS OVER   ------   
                        Try again 
                        BOT Gessing---{bot}""")
    trys=input("     _____Want to play again enter 'Try'_____\n")
    if trys.lower()=='try':
        print("\n               -------------- GESSING THE NUMBER -------------\n")
        Guessing_game(user)



print("\n                ------------- GESSING THE NUMBER -------------\n")
user =input("""    Type 'PLAY' to star game:-
    Type 'EXIT' to stop game:-
               """)
Guessing_game(user)