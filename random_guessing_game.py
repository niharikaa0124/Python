import random
games_played = 0
games_won = 0
try:
    with open("highscore.txt", "r") as f:
        highscr = int(f.read())
except FileNotFoundError:
    highscr = None

while True:
    guess=[]
    difficulty=int(input("Enter 1-easy ,2-med ,3-hard "))
    if difficulty==1:
        limit=10
    elif difficulty==2:
        limit=50
    elif difficulty==3:
        limit=100
    else:
        print("Choose 1, 2 or 3")
        continue
    secret_number=random.randint(1,limit)
    games_played += 1
    print(f"Guess a number between 1 and {limit}")
    cnt=0
    while True:
        if cnt==10:
            break
        try:
            num=int(input("Enter a number : "))
        except ValueError:
            print("Enter a valid number")
            continue
        if(num<secret_number):
            print("Number too small")
            guess.append(num)
            cnt=cnt+1
        elif(num>secret_number):
            print("Number too big")
            guess.append(num)
            cnt=cnt+1
        else:
            cnt=cnt+1
            print("Correct!")
            print (f"took {cnt} attempts to guess a number and the guess history is {guess}")
            games_won += 1
            if highscr is None or cnt < highscr:
                highscr=cnt
                with open("highscore.txt", "w") as f:
                    f.write(str(highscr))
                print("NEW HIGH SCORE")
            # if highscr is not None:
            #     print(f"the high score is {highscr}")
            break
    
    if cnt==10:
        print("Attempts finished")
        print(f"The number was {secret_number}")
    # elif highscr>cnt :
    #     highscr=cnt
    
    command=input("Enter command or press enter : ").lower()
    if command in ["no", "n", "exit"]:
        break

    elif command=="reset highscore":
        highscr=None
        with open("highscore.txt", "w") as f:
            f.write("")
        print("High score cleared")

    elif command=="show highscore":
        if highscr is None:
            print("No high score yet")
        else:
            print(f"High score is {highscr}")

    elif command=="stats":
        print(f"the total games player were {games_played}")
        print(f"Games won: {games_won} ")
        print(f"Games lost: {games_played-games_won}")

    elif command == "help":
        print("""
        help            - Show all commands
        show highscore  - Display current high score
        reset highscore - Clear high score
        stats           - Show game statistics
        exit            - Quit the game
    """)

