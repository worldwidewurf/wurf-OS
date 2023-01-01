import time
from os import system, name
import random
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def start_single_player():
    symbol = 'O'
    a = ['a1','a2','a3' ]
    b = ['b1','b2','b3' ]
    c = ['c1','c2','c3' ]
    a1,a2,a3,b1,b2,b3,c1,c2,c3= ' ',' ',' ',' ',' ',' ',' ',' ',' '
    # print(a)
    # print(b)
    # print(c)
    first_run = 'y'
    psbl_moves = 0
    invalid_move = 'n'
    mode = 'single'
    while True:
        clear()
        tttheme(mode)
        print(f'''
                                              1    2    3
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         A  | {a1} || {a2} || {a3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         B  | {b1} || {b2} || {b3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         C  | {c1} || {c2} || {c3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
        ''')
        if invalid_move == 'n':
            psbl_moves += 1
        invalid_move = 'n'
        if first_run == 'y':
            symbol = 'O'
            first_run = 'n'
        elif first_run == 'n':
            symbol = 'X'
            first_run = 'y'
            
        if a[0] == a[1] == a[2] : 
            if a[0] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print(f'''
                                        You beat the AI''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        elif a[0] == b[0] == c[0] : 
            if a[0] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')

            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        elif a[0] == b[1] == c[2] : 
            if a[0 ] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        elif b[0] == b[1] == b[2] : 
            if b[0 ] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        elif a[2] == b[2] == c[2] : 
            if b[2] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break

        elif c[0] == b[1] == a[2] : 
            if b[1] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        elif c[0] == c[1] == c[2]: 
            if c[0 ] == 'X':
                print(f'''
                                        AI Won. ''')
            else:
                print('''
                                        You beat the AI''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                break
        
        elif psbl_moves == 10:
            print('Match Drawn')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                start_single_player()
            else:
                start_ttt()
        # print(psbl_moves)
        if first_run == 'n':
            w = input('''
                                        Players Turn : ''').lower()
        else:
            # first row
            if a[0] == a[1] == 'X' and a[2]!='O':
                w = 'a3'
            elif a[0] == a[2] == 'X' and a[1]!='O' :
                w = 'a2'
            elif a[2] == a[1] == 'X' and a[0]!='O' :
                w= 'a1'
            
            # second row
            elif b[0] == b[1] == 'X' and b[2]!='O':
                w = 'b3'
            
            elif b[0] == b[2] == 'X' and b[1]!='O':
                w = 'b2'
            elif b[2] == b[1] == 'X' and b[0]!='O':
                w= 'b1'

            # third row
            elif c[0] == c[1] == 'X' and c[2]!='O':
                w = 'c3'
        
            elif c[0] == c[2] == 'X' and c[1]!='O':
                w = 'c2'
            elif c[2] == c[1] == 'X' and c[0]!='O':
                w= 'c1'
            # first column
            elif a[0] == b[0] == 'X' and c[0]!='O':
                w = 'c1'
            elif a[0] == c[0] == 'X' and b[0]!='O':
                w = 'b1'
            elif b[0] == c[0] == 'X' and a[0]!='O':
                w= 'a1'
    
            # second column
            elif a[1] == b[1] == 'X' and c[1]!='O':
                w = 'c2'
            elif a[1] == c[1] == 'X' and b[1]!='O':
                w = 'b2'
            elif b[1] == c[1] == 'X' and a[1]!='O':
                w= 'a2'

            # third
            elif a[2] == b[2] == 'X' and c[2]!='O':
                w = 'c3'
            elif a[2] == c[2] == 'X' and b[2]!='O':
                w = 'b3'
            elif b[2] == c[2] == 'X' and a[2]!='O':
                w= 'a3'

            # cross 1
            elif a[0] == b[1] == 'X' and c[2]!='O':
                w = 'c3'
            elif a[0] == c[2] == 'X' and b[1]!='O':
                w = 'b2'
            elif b[1] == c[2] == 'X' and a[0]!='O':
                w= 'a1'
            # cross 2
            elif a[2] == b[1] == 'X' and c[0]!='O':
                w = 'c1'
            elif a[2] == c[0] == 'X' and b[1]!='O':
                w = 'b2'
            elif b[1] == c[0] == 'X' and a[2]!='O':
                w= 'a3'

            else:
                while True:
                    # first row
                    if a[0] == a[1] == 'O' and a[2]!='O' and a[2]!='X':
                        w = 'a3'
                        break
                    elif a[0] == a[2] == 'O' and a[1]!='O' and a[1]!='X':
                        w = 'a2'
                        break
                    elif a[2] == a[1] == 'O' and a[0]!='O' and a[0]!='X':
                        w= 'a1'
                        break
                    # second row
                    elif b[0] == b[1] == 'O' and b[2]!='O'and b[2]!='X':
                        w = 'b3'
                        break
                    elif b[0] == b[2] == 'O' and b[1]!='O' and b[1]!='X':
                        w = 'b2'
                        break
                    elif b[2] == b[1] == 'O' and b[0]!='O' and b[0]!='X':
                        w= 'b1'
                        break
                    # third row
                    elif c[0] == c[1] == 'O' and c[2]!='O' and c[2]!='X':
                        w = 'c3'
                        break
                    elif c[0] == c[2] == 'O' and c[1]!='O' and c[1]!='X':
                        w = 'c2'
                        break
                    elif c[2] == c[1] == 'O' and c[0]!='O' and c[0]!='X':
                        w= 'c1'
                        break
                    # first column
                    elif a[0] == b[0] == 'O' and c[0]!='O'and c[0]!='X':
                        w = 'c1'
                        break
                    elif a[0] == c[0] == 'O' and b[0]!='O'and b[0]!='X':
                        w = 'b1'
                        break
                    elif b[0] == c[0] == 'O' and a[0]!='O'and a[0]!='X':
                        w= 'a1'
                        break
                    # second column
                    elif a[1] == b[1] == 'O' and c[1]!='O' and c[1]!='X':
                        w = 'c2'
                        break
                    elif a[1] == c[1] == 'O' and b[1]!='O' and b[1]!='X':
                        w = 'b2'
                        break
                    elif b[1] == c[1] == 'O' and a[1]!='O' and a[1]!='X':
                        w= 'a2'
                        break

                    # third
                    elif a[2] == b[2] == 'O' and c[2]!='O' and c[2]!='X':
                        w = 'c3'
                        break
                    elif a[2] == c[2] == 'O' and b[2]!='O' and b[2]!='X':
                        w = 'b3'
                        break
                    elif b[2] == c[2] == 'O' and a[2]!='O' and a[2]!='X':
                        w= 'a3'
                        break

                    # cross 1
                    elif a[0] == b[1] == 'O' and c[2]!='O'and c[2]!='X':
                        w = 'c3'
                        break
                    elif a[0] == c[2] == 'O' and b[1]!='O'and b[1]!='X':
                        w = 'b2'
                        break
                    elif b[1] == c[2] == 'O' and a[0]!='O' and a[0]!='X':
                        w= 'a1'
                        break
                    # cross 2
                    elif a[2] == b[1] == 'O' and c[0]!='O' and c[0]!='X':
                        w = 'c1'
                        break
                    elif a[2] == c[0] == 'O' and b[1]!='O' and b[1]!='X':
                        w = 'b2'
                        break
                    elif b[1] == c[0] == 'O' and a[2]!='O' and a[2]!='X':
                        w= 'a3'
                        break
                    else:
                        while True:
                            l = 'a','b','c'
                            u =random.choice(l)
                            n= random.randint(1,3)
                            w = f"{u}{str(n)}"
                            if w in a or w in b or w in c:
                                # print(f'AI Turn : {w}')
                                
                                break
                            else:
                                # print('incalid move')
                                # print(w)
                                continue
                        print(f'''
                                        AI Turn : {w}''')
                        time.sleep(2)
                    break
        m = symbol
        if w in a or w in b or w in c:
            if w in a:
                
                a = list(map(lambda x: x.replace(w, m), a))
                if w == 'a1':
                    a1 = m
                elif w == 'a2':
                    a2 = m
                elif w == 'a3':
                    a3 = m
            elif w in b:
                b = list(map(lambda x: x.replace(w, m), b))
                if w == 'b1':
                    b1 = m
                elif w == 'b2':
                    b2 = m
                elif w == 'b3':
                    b3 = m
            elif w in c:
                c = list(map(lambda x: x.replace(w, m), c))
                if w == 'c1':
                    c1 = m
                elif w == 'c2':
                    c2 = m
                elif w == 'c3':
                    c3 = m
        else:
            if w == 'q':
                break

            first_run = 'y'
            print('''
                                        Invalid box''')
            invalid_move = 'y'
            time.sleep(3)

def tttheme(mode):
    clear()
    if mode == 'multiplayer':
        print('''
                                        ░▒▓ 𝙏 𝙞 𝙘  𝙏 𝙖 𝙘  𝙏 𝙤 𝙚 ▓▒░
                                        © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022
                                        - 𝘓𝘖𝘊𝘈𝘓 𝘔𝘜𝘓𝘛𝘐𝘗𝘓𝘈𝘠𝘌𝘙''')
    elif mode == 'single':
        print('''
                                        ░▒▓ 𝙏 𝙞 𝙘  𝙏 𝙖 𝙘  𝙏 𝙤 𝙚 ▓▒░
                                        © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022
                                        - 𝘚𝘐𝘕𝘎𝘓𝘌 𝘗𝘓𝘈𝘠𝘌𝘙''')
    elif mode == 'home':
        print('''
                                        ░▒▓ 𝙏 𝙞 𝙘  𝙏 𝙖 𝙘  𝙏 𝙤 𝙚 ▓▒░
                                        © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022
    
                                        ① Single player (play against AI)
                                        ② Local Multiplayer(Play with a friend)
                                        ③ Quit 
    ''')

def local_multiplayer():
    symbol = 'O'
    game_mode = 'multiplayer'
    a = ['a1','a2','a3' ]
    b = ['b1','b2','b3' ]
    c = ['c1','c2','c3' ]
    a1,a2,a3,b1,b2,b3,c1,c2,c3= ' ',' ',' ',' ',' ',' ',' ',' ',' '
    # print(a)
    # print(b)
    # print(c)
    first_run = 'y'
    psbl_moves = 0
    invalid_move = 'n'
    while True:
        tttheme(game_mode)
        
        print(f'''
                                              1    2    3
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         A  | {a1} || {a2} || {a3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         B  | {b1} || {b2} || {b3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
                                            ┌ ─ ┐┌ ─ ┐┌ ─ ┐
                                         C  | {c1} || {c2} || {c3} |
                                            └ ─ ┘└ ─ ┘└ ─ ┘
        ''')
        if invalid_move == 'n':
            psbl_moves += 1
        invalid_move = 'n'
        if first_run == 'y':
            symbol = 'O'
            first_run = 'n'
        elif first_run == 'n':
            symbol = 'X'
            first_run = 'y'
            
        if a[0] == a[1] == a[2] : 
            print(f'''
                                        {a[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        elif a[0] == b[0] == c[0] : 
            print(f'''
                                        {a[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        elif a[0] == b[1] == c[2] : 
            print(f'''
                                        {a[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        elif b[0] == b[1] == b[2] : 
            print(f'''
                                        {b[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        elif a[2] == b[2] == c[2] : 
            print(f'''
                                        {a[2]} Won. ''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break

        elif c[0] == b[1] == a[2] : 
            print(f'''
                                        {c[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        elif c[0] == c[1] == c[2]: 
            print(f'''
                                        {c[0]} Won. ''')
            
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                break
        
        elif psbl_moves == 10:
            print('''
                                        Match Drawn''')
            ask_restart = input('''
                                        Restart? (y/N) : ''').lower()
            if ask_restart == 'y':
                local_multiplayer()
            else:
                start_ttt()
        # print(psbl_moves)
        # if first_run == 'n':
        w = input('''                   
                                        Grid Coordinates : ''')
        
        m = symbol
        if w in a or w in b or w in c:
            if w in a:
                
                a = list(map(lambda x: x.replace(w, m), a))
                if w == 'a1':
                    a1 = m
                elif w == 'a2':
                    a2 = m
                elif w == 'a3':
                    a3 = m
            elif w in b:
                b = list(map(lambda x: x.replace(w, m), b))
                if w == 'b1':
                    b1 = m
                elif w == 'b2':
                    b2 = m
                elif w == 'b3':
                    b3 = m
            elif w in c:
                c = list(map(lambda x: x.replace(w, m), c))
                if w == 'c1':
                    c1 = m
                elif w == 'c2':
                    c2 = m
                elif w == 'c3':
                    c3 = m
        else:
            if w == 'q':
                break
            else:
                print('''               
                                        Invalid box''')
                if symbol == 'X':
                    first_run = 'n'
                else:
                    first_run = 'y'
                invalid_move = 'y'
                time.sleep(3)

def start_ttt():
    while True:
        tttheme('home')
        mode_choice = input('''
                                        [1] or [2] : ''').lower()
        if mode_choice == "1":
            start_single_player()
        elif mode_choice == "2":
            local_multiplayer()
        elif mode_choice == '3' or mode_choice == 'q':
            break
        else:
            
            print('''
                                        Invalid option. ''')
            time.sleep(3)

if __name__ == "__main__":
    start_ttt()