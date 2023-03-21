import socket
import psutil
import sys
import time
from wurf_OS import *
import uuid
# from functions import *
# from apps.browser import * 
# from apps.texteditor import * 
# from apps.calculator import * 

from os import system, name



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def open_google():
    pass

def valid_options():
    os_theme()
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
        
    print('''① Open Google\n'''.center(139))
    print('''② Open Vscode\n'''.center(139))
    print('''③ Open File Manager\n'''.center(139))
    print('''➍ Applications\n'''.center(139))
    print('''➎ BioS\n'''.center(139))
    print(f'''➏ LogOut of {user_name}\n'''.center(139))


def valid_applications():
    os_theme()
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
        
    print('''① Simple Calculator\n'''.center(139))
    print('''② Uncle Sam's Calculator\n'''.center(139))
    print('''③ Youtube\n'''.center(139))
    print('''➍ Games\n'''.center(139))
    print('''➎ Back to main menu\n'''.center(139))
    # print(f'''➏ LogOut of {user_name}\n'''.center(139))


def available_games():
    os_theme()
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)

    print('''Available Games.\n'''.center(139))
    print('''① Rock Paper Scissors\n'''.center(139))
    print('''② Tic Tac Toe\n'''.center(139))
    print('''③ Guide\n'''.center(139))
    print('''➍ Back to Applications\n'''.center(139))
    # print('''➎ Back to main menu\n'''.center(139))
    # print(f'''➏ LogOut of {user_name}\n'''.center(139))
def select_games():
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
    prompt = f'~{user_name}-$ :  '
    back = 'N'
    while back == 'N':
        while True:
            try:
                available_games()
                app_selection = int(get_command(prompt))
                break
            except:
                continue
        if app_selection == 1:
            start_rock()
        elif app_selection ==2:
            start_ttt()
        elif app_selection ==3:
            guide()
        elif app_selection ==4:
            select_application()

def select_application():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
    prompt = f'~{user_name}-$ :  '
    back = 'N'
    while back == 'N':
        while True:
            try:
                valid_applications()
                app_selection = int(get_command(prompt))
                break
            except:
                continue
        if app_selection == 1:
            cal()
        elif app_selection ==2:
            tax_cal()
        elif app_selection ==3:
            if connected():
                open_youtube()
            else:
                delay_print('An internet connection is needed to open youtube.')
                print()
        elif app_selection ==4:
            select_games()
        elif app_selection == 5:
            select_options()
        
        



def select_options():
    valid_options()
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
    prompt = f'~{user_name}-$ :  '
    log_out = 'N'
    while log_out == 'N':
        while True:
            try:
                user_selection = int(get_command(prompt))
                break
            except:
                continue
        if user_selection == 1:
            print("""
                                        discontinued""")

        elif user_selection == 2:
            start_vscode()
        elif user_selection == 3:
            start_file_manager()
        elif user_selection == 4:
            select_application()
        elif user_selection == 5:
            openBioS(password,user_name)
        elif user_selection == 6:
            delay_print(f'Logging out of {user_name}...')
            print()
            start_wurf()
        

def openBioS(password,username):
    prompt = 'Enter password admin to enter BioS Mode : '
    user_pass_attempt = get_password(prompt)
    password = password.encode('utf-8')
    user_pass = user_pass_attempt.encode('utf-8')
    if bcrypt.checkpw(user_pass, password):
        delay_print('Logging into [BioS MoDe]')
        while True:
            fd = os.path.dirname(os.path.realpath('__file__'))
            fp = os.path.join(fd, 'users/admin/email.txt')
            user_email = open(fp)
            usermail = user_email.readline()
            time.sleep(5)
            bios_theme()
            host = socket.gethostname()
            ip_address = socket.gethostbyname(host)
            mac_address = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range(0,8*6,8)][::-1]))
            print(f'USERNAME : {username}'.center(140))
            print(f'PASSWORD : {user_pass_attempt}'.center(140))
            print(f'E-Mail : {usermail}'.center(140))
            print(f'HOSTNAME : {host}'.center(140))
            print(f'LOCAL IP ADDRESS : {ip_address}'.center(140))
            print(f'MAC ADDRESS : {mac_address}'.center(140))
            print()
            prompt = 'Make changes to username?(y/N) : '
            decision = get_command(prompt)
            if decision.lower()=='y':
                file_dir = os.path.dirname(os.path.realpath('__file__'))
                file_path = os.path.join(file_dir, 'users/admin/admin.txt')
                new_username = get_name()
                login_details = f'{new_username},{password}'
                with open(file_path, 'w') as vault:
                    vault.write(json.dumps(login_details))
                print('Username changed successfully.')
            prompt = 'Make changes to Email?(y/N) : '
            decision = get_command(prompt)
            if decision.lower()=='y':
                request_email()
                print('Email changed successfully.')
            prompt = 'Done with changes?(y/N) : '
            decision = get_command(prompt)
            if decision.lower()=='y':
                time.sleep(3)
                delay_print('Exiting BioS.....')
                print()
                time.sleep(3)
                return select_options()
            else:
                continue
            
            
                

def bios_theme():
    clear()
    print('''
    
    ''')
    print("""𝙬 𝙪 𝙧 𝙛 - 𝙊 𝙎  [ 𝘽 𝙞 𝙤 𝙎  𝙈 𝙤 𝘿 𝙚 ]\n""".center(140))
    print('''Powered by Ⓛ ⓘ ⓝ ⓤ ⓧ\n'''.center(140))
    print('''© 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022'''.center(140))
def start_admin():
    delay_print('Logging in...')
    time.sleep(3)

    for i in reversed(range(1,6)):
        delay_print(str(i)+'..')
        time.sleep(0.25)
    os_theme()
    # valid_options()
    select_options()

if __name__ == "__main__":
    start_admin()