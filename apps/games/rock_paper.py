import random
from os import system, name

def start_rock():
    while True:
        clear()
        rpstheme()
        
        a = 'rps'
        ai_choices = [*a]
        valid_moves = [*a,'q']
        ai_score = 0
        user_score = 0
        rounds = 3
        while rounds != 0 :
            # clear()
            ai = random.choice(ai_choices)
            ai_symbol = symbols(ai)
            
            while True:
                
                userinput = input('''
                                    [R][P][S]? : ''').lower()
                if userinput not in valid_moves:
                    print('''   
                                    Invalid move.''')
                else:
                    user_symbol = symbols(userinput)
                    rounds -= 1
                    break
            if userinput == 'q':
                break
            print(f''' 
                                    AI : {ai_symbol} 
                                    USER : {user_symbol}''')
            if ai == userinput:
                ai_score +=1
                user_score +=1
            elif userinput == 'r' and ai == 'p':
                ai_score +=1
            elif userinput == 'r' and ai == 's':
                user_score +=1
            elif userinput == 'p' and ai == 'r':
                user_score +=1
            elif userinput == 'p' and ai == 's':
                ai_score +=1
            elif userinput == 's' and ai == 'r':
                ai_score +=1
            elif userinput == 's' and ai == 'p':
                user_score +=1
        if userinput == 'q':
            break
        if user_score > ai_score:
            print('''
                                    You win.''')
        elif user_score < ai_score:
            print('''
                                    Ai wins.''')
        else:
            print('''
                                    Match Drawn.''')
        ask_restart = input('''
                                    Restart? (y/N) :''').lower()
        if ask_restart == 'y':
            start_rock()
        else:
            break

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def symbols(choice):
    
    if choice == 'r':
        return '''
                                    .------.
                                    |R.--. |
                                    | :(): |
                                    | ()() |
                                    | '--'R|
                                    `------'
'''
    elif choice == 'p':
        return '''
                                    .------.
                                    |P.--. |
                                    | :/\: |
                                    | (__) |
                                    | '--'P|
                                    `------'
'''
    elif choice == 's':
        return '''
                                    .------.
                                    |S.--. |
                                    | :/\: |
                                    | :\/: |
                                    | '--'S|
                                    `------'
'''
    




def rpstheme():
    
    print('''


                            ░▒▓ 𝙌 𝙪 𝙖 𝙧 𝙩 𝙯  𝙋 𝙖 𝙧 𝙘 𝙝 𝙢 𝙚 𝙣 𝙩  𝙎 𝙝 𝙚 𝙖 𝙧 𝙨 ▓▒░
                                    © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022

                                    Valid moves:

                                        > Rock     [r]
                                        > Paper    [p]
                                        > Scissors [s]

                                    [press Q to quit]

    ''')

if __name__ == "__main__":
    start_rock()