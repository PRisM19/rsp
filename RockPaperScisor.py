print("\tWELCOME TO ROCK PAPER SCISSOR GAME🤘📄✂️")
print("==============================================================")
print("Rule Set: 1 for Rock, 2 for scissor and 3 for paper")
def game():
    g = 0
    while g not in [1,2,3]:
        g =  int(input("Throw Your Choice :"))


    p = ['rock', 'paper', 'scissor']

    import random
    import time

    k = random.choice(p)
    print("Computer picks ...")
    time.sleep(3)
    print(k.upper())
    time.sleep(1)


    match g:
        case 1:
            if(k == 'rock'):
                print("\tBoth rocks destroyed💥💥💥")
                print("\tDraw Game")
                cort()
            elif (k == 'paper'):
                print("\tPaper Eats The Rock🍴🍴🍴")
                print("\tGame Lost")
                cort()
            else:
                print("\tRock breaks Scissors🤘🤘🤘")
                print("\t🤘🤘🤘🤘🤘🤘Winner🤘🤘🤘🤘🤘🤘\t")
                cort()
        case 2:
            if(k == 'rock'):
                print("\tScissors are destroyed💥💥💥")
                print("\tGame Lost")
                cort()
            elif (k == 'paper'):
                print("\tScissors cut the paper🙏🙏🙏")
                print("\t✂️✂️✂️✂️✂️Winner✂️✂️✂️✂️✂️\t")
                cort()
            else:
                print("\tScissor cannot cut Scissor😭😭😭😭")
                print("\tGame Draw")
                cort()
        case 3:
            if(k == 'rock'):
                print("\tPaper Wraps The Rock📝📝📝📝📝\t")
                print("\t📄📄📄📄📄Winner📄📄📄📄📄\t")
                cort()
            elif (k == 'paper'):
                print("\tPaper and Paper Friendship🤲🤲🤲")
                print("\tGame Draw")
                cort()
            else:
                print("\tPaper has been Cut💥💥💥")
                print("\tGame Lost")
                cort()

def cort():
    import time
    con = input("Do you want to continue??? y/n:")
    if(con.lower().strip() == 'y'):
        game()
    elif(con.lower().strip() == 'n'):
        time.sleep(2)
        print("❌❌❌❌❌Game Over❌❌❌❌❌")
    else:
        print("Warning only enter y/n")
        time.sleep(5)
        cort()
        
    

                
game()