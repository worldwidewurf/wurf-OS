from os import system, name
import time

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def tax_cal():
    clear()
    theme()
    while True:
        try:
            salary = int(input('''
                                    How much do you earn per annum? : '''))
            break
        except:
            print('''
                                    Salary can only be a number.
    ''')    
            continue
        
    if salary in range(1,226000):
        tax_percentage = 18
    elif salary in range(226001,353100):
        tax_percentage = 26
    elif salary in range(353101,488700):
        tax_percentage = 31
    elif salary in range(488701,641400):
        tax_percentage = 36
    elif salary in range(641401,817600):
        tax_percentage = 39
    elif salary in range(817601,1731600):
        tax_percentage = 41
    elif salary > 1731601:
        tax_percentage = 45
    else:
        time.sleep(1)
        print('''
                                    Not eligible to pay tax.
    ''')
        tax_cal()

    
    
    tax_to_pay =float("{:.2f}".format(salary*(tax_percentage/100))) 
    salary_after_tax = float("{:.2f}".format(salary - tax_to_pay))
    salary_per_month = float("{:.2f}".format(salary_after_tax/12))
    time.sleep(5)
    print(f'''
                                Tax Calculations for a salary of {salary} per annum(p/a):

                                    Tax Amount(p/a)         : {tax_to_pay}
                                    Salary After Tax(p/a)   : {salary_after_tax}
                                    Salary Per Month        : {salary_per_month}

                                    ⁽ᴬᵐᵒᵘⁿᵗˢ ᵐᶦᵍʰᵗ ᵈᶦᶠᶠᵉʳ ᵈᵘᵉ ᵗᵒ ᵈᶦᶠᶠᵉʳᵉⁿᵗ ʷᵒʳᵏᶦⁿᵍ ʰᵒᵘʳˢ⁾

    ''')
    restart = input('''
                                Restart? (y/N) : ''')
    if restart.lower() == 'y':
        tax_cal()
    
def theme():
    print('''


                                ░▒▓ 𝙐 𝙣 𝙘 𝙡 𝙚  𝙎 𝙖 𝙢 ❜ 𝙨  𝘾 𝙖 𝙡 𝙘 𝙪 𝙡 𝙖 𝙩 𝙤 𝙧 ▓▒░
                                © 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022


    ''')
if __name__ == "__main__":
    tax_cal()