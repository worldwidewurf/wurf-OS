from os import system, name
from time import sleep


first_run = 'Y'
num = 0
guide = 1
empty =[]
sign = ''
def cal():
 clear()
 print('''
 
                                ░▒▓ 𝙎 𝙞 𝙢 𝙥 𝙡 𝙚  𝘾 𝙖 𝙡 𝙘 𝙪 𝙡 𝙖 𝙩 𝙤 𝙧 ▓▒░
                                © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022
                                Math Signs:
        
                                   > + [Addition]
                                   > - [Subtraction]
                                   > x [multiplication]
                                   > / [Division]
                                   > * [Power of]
                                   > = get solution
        
                                last number before = should be 0
''')

 global num,guide,first_run,empty,sign
 signs = '+-x/*='
 valid = [*signs]
 end = ''
 while end == '':
    print(f"""
                                 {''.join(empty)}""")
    print(f'''
                                 [      {num}      ]''')
    if first_run == 'N':
        while True:
            print(' ',end='')
            sign = input('''
                                Action : ''')
            if validate_sign(sign):
                break
            else:
                print('''
                                Invalid mathematical sign''')
                continue
    if sign == '=':
        print(f"{''.join(empty)} = {num}")
        
        ask_usr = input("""
                                Restart?(y/N) : """)
        if ask_usr.lower() == 'y':
            first_run = 'Y'
            num = 0
            guide = 1
            empty =[]
            sign = ''
            cal()
        else:
            end='y'
            break
    ordinal_list = get_ordinal()
    num_list = [i for i in range(1,len(ordinal_list)+1)]
    for number in num_list:
        if guide == number:
            ordinal_index = num_list.index(number)
    ordinal = ordinal_list[ordinal_index]
    # print(num_list)
    # print(ordinal_list)
    while True:
        try:
            print(' ',end='')
            number = int(input(f'''
                                Enter {ordinal} number : '''))
            break
        except:
            print('''
                                Simple calculator only calculates numbers.''')
            continue
    if first_run == 'Y':
        num += number
        first_run = 'N'
        guide += 1
        empty.append(str(number))
        cal()
    guide += 1
    if sign == '+':
        num += number
        empty.append('+'+(str(number)))
        cal()
    elif sign == '-':
        num -= number 
        empty.append('-'+(str(number)))
        cal()
    elif sign == 'x':
        num *= number
        empty.append('x'+(str(number)))
        cal()
    elif sign == '/':
        num /= number
        empty.append('/'+(str(number)))
        cal()
    elif sign == '*':
        num **= number
        empty.append('*'+(str(number)))
        cal()
    break
  
def validate_sign(sign):
    signs = '+-x/*='
    valid = [*signs]
    if sign in valid:
        return True
    else:
        return False
    
def clear():
   if name == 'nt':
    _ = system('cls')
   else:
    _ = system('clear')
def get_ordinal():
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    ordinal_list = [ordinal(n) for n in range(1,100)] #ADJUST IF EQUATION IS LONG 
    return ordinal_list

if __name__ == "__main__":
    cal()