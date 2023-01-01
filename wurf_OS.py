import re
import json
import sys
import getpass
import time 
import os
from datetime import datetime
import psutil
from termcolor import colored, cprint
import bcrypt
from os import system, name
import ssl
import smtplib
from email.message import EmailMessage
import random
from apps.browser import *
from apps.texteditor import *
from apps.file import *
from apps.calculator import * 
from apps.tax_calculator import * 
from apps.youtube import *
import urllib.request
from apps.games.rock_paper import *
from apps.games.guide_robot import *
from apps.games.ticktacktoe import *


def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def get_battery_life():
    battery = psutil.sensors_battery()
    battery_percentage = int(battery.percent)
    is_charging = battery.power_plugged
    wifi_symbol = '✈'
    
    if connected():
        wifi_symbol='''⤽'''

    if battery_percentage < 70 and battery_percentage>30:
        if is_charging:
          battery_sumbol = f'''
                                                                ▣⚡□- {battery_percentage}% {wifi_symbol}                        
    '''
        else:  
            battery_sumbol = f'''
                                                                ▣▣□□- {battery_percentage}% {wifi_symbol}                        
        '''
    elif battery_percentage > 69:
        if is_charging:
            battery_sumbol = f'''
                                                                ▣⚡▣- {battery_percentage}% {wifi_symbol}                       
    '''
        else:

            battery_sumbol = f'''
                                                                ▣▣▣▣- {battery_percentage}% {wifi_symbol}                        
        '''
    elif battery_percentage < 30 and battery_percentage>10:
        if is_charging:
            battery_sumbol = f'''
                                                                ▣⚡□- {battery_percentage}% {wifi_symbol}                       
    '''
        else:
            battery_sumbol = f'''
                                                                ▣□□□- {battery_percentage}% {wifi_symbol}                        
        '''
    else:

        if is_charging:
            battery_sumbol = f'''
                                                                ▣⚡▣- {battery_percentage}% {wifi_symbol}                       
    '''
        else:

            battery_sumbol = f'''
                                                                ▣⚠️▣- {battery_percentage}% {wifi_symbol}                       
        '''
    return battery_sumbol,battery_percentage

def os_theme():
    clear()
    print()
    print()
    print()
    print()
    print('''🅆 🄾 🅁 🄻 🄳 🅆 🄸 🄳 🄴 🅆 🅄 🅁 🄵  🄾 🅂\n'''.center(140))
    print('© 𝘸𝘰𝘳𝘭𝘥𝘸𝘪𝘥𝘦𝘸𝘶𝘳𝘧 2022'.center(140))
    print()
    print('''          𝗛𝗘𝗟𝗟𝗢 𝗨𝗦𝗘𝗥\n'''.center(127))
    print()
    battery_sumbol,battery_percentage =get_battery_life()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print('      ',end=''.center(53))
    cprint(f'{date_time}', "white", attrs=["dark"])
    print()
    print('''        ''',end=' '.center(53))
    if battery_percentage < 10:
        cprint(f'{battery_sumbol}', "red", attrs=["dark"])
    else:
        cprint(f'{battery_sumbol}', "white", attrs=["dark"])
    

def start_options():
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        admin_details = admin_file.readlines()
        if len(admin_details)==0:
            print('''① Setup main user\n'''.center(139))
        elif len(admin_details) > 0:
            print('''① Login to main user\n'''.center(139))
        
        print('''② Setup guest user\n'''.center(139))
        if len(admin_details) > 0:
            print('''③ Reset password\n'''.center(139))
        print('''➍ Turn Off\n'''.center(139))

def get_command(prompt):
    user_input = input(prompt)
   
    return user_input
        
    

def user_name_length(username):
    if len(username)>16 :
        print('Username is too long.')
        return False
    else:
        return True

def valid_passwword(password):
    special_chars      =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_char_list  = [*special_chars]
    password_list      = [*password]
    test_caps          = 0
    test_lower         = 0
    test_num           = 0
    test_chars         = 0
    if password_list != [] and len(password)>7:
        for letter in password_list:
            if letter.isupper():
                test_caps += 1
            if letter.islower():
                test_lower += 1
            elif letter.isdigit():
                test_num  += 1
            elif letter in special_char_list:
                test_chars+= 1
        message_list = []
        if test_caps == 0:
            message = "Password must have atleat 1 caps character."
            message_list.append(message)
        if test_lower == 0:
            message1 = "Password must have atleat 1 lower character."
            message_list.append(message1)
        if test_num == 0:
            message2 = "Password must have atleat 1 number character."
            message_list.append(message2)
        if test_chars == 0:
            message3 = "Password must have atleat 1 special character."
            message_list.append(message3)
        if test_caps == 0 or test_num == 0 or test_chars == 0 or test_lower == 0:
            for warning in message_list:
                print(warning)
                return False
        else:
            return True
    else:
        if len(password)<=10:
            print('Password must be greater than 7.')
        else:
            print('Password cannot be empty.')
        return False


def get_name():
    user_name_prompt     = "Setup username : "
    main_user_name       = get_command(user_name_prompt)
    if user_name_length(main_user_name):
        return main_user_name
    else:
        get_name()

def get_password(password_prompt):
    password = getpass.getpass(password_prompt)
    return password

def set_password():
    password_prompt      = "Setup user password : "
    main_user_password   = get_password(password_prompt)
    if valid_passwword(main_user_password):
        return main_user_password
    else:
        return set_password()


def confirm_password():
    confirm_prompt = "Confirm password : "
    confirm_user_password = get_password(confirm_prompt)
    return confirm_user_password


def delay_print(d_string):
    for letter in d_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.10)


def encrypt_password(password):

    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
    return hashed

def request_email():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/email.txt')
    prompt = 'Register account e-mail : '
    while True:
        email = get_command(prompt)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if(re.fullmatch(regex, email)):
            prompt = 'Verify e-mail : '
            while True:
                verify_email = get_command(prompt)
                if verify_email == email:
                    with open(file_path, 'w') as mail_box:
                        mail_box.write(json.dumps(email))
                break
        break


def get_user_details(info_list):
    username = info_list[0]
    userpassword = info_list[1]
    username_list = [*username]
    userpassword_list = [*userpassword]
    username_list.pop(0)
    userpassword_list.pop(-1)
    userpassword_list.pop(-1)
    userpassword_list.pop(0)
    userpassword_list.pop(0)
    user = "".join(username_list)
    password = "".join(userpassword_list)
    return user,password

def which_user(user_input):
    
    if user_input == 1:
        
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, 'users/admin/admin.txt')
        clear()
        os_theme()
        with open(file_path) as admin_file:
            admin_details = admin_file.readlines()
            if len(admin_details) == 0:
                username = get_name()
                main_user_password =  set_password()
                while True:
                    confirm_user_password = confirm_password()
                    if confirm_user_password == main_user_password:
                        mask_password ='*'*(len([*main_user_password]))
                        print(f'Password set to {mask_password}')
                        delay_print("Creating profile.....")
                        main_user_password = encrypt_password(main_user_password)
                        login_details = f'{username},{main_user_password}'
                        print()
                        request_email()
                        with open(file_path, 'w') as vault:
                            vault.write(json.dumps(login_details))
                        time.sleep(7)
                        delay_print("Profile created, restarting the machine.")
                        print()
                        delay_print("Shutting down.....")
                        print()
                        time.sleep(7)
                        delay_print("......Restarting......")
                        print()
                        time.sleep(5)
                        break
                    else:
                        print("Passwords donnot match.")
                        continue
                    
        user_details = open(file_path)
        get_info = user_details.read().split(',')
        user_name, password = get_user_details(get_info)
        print('Wᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ '+ user_name)
        prompt = 'Enter password for ' + user_name+ ' : '
        while True:
            login_pass = get_password(prompt)
            login_pass = login_pass.encode('utf-8')
            hashed_password = password.encode('utf-8')
            if bcrypt.checkpw(login_pass, hashed_password):
                import users.admin.admin_user as admin
                admin.start_admin()
                
                break
            else:
                print('Wrong password')
                continue
    elif user_input == 2:
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, 'users/guests/guest.txt') 
        userslist = open(file_path).read().strip().split(',')
        print(userslist)
        while True:
            os_theme()
            print('''① Login to existing guest\n'''.center(139))
            print('''② Setup new guest user\n'''.center(139))
            set_or_log = get_command('Select option : ')
            if set_or_log == '1':
                if userslist == []:
                    delay_print('No existing users found.')
                    time.sleep(3)
                else:
                    prompt = 'Enter username : '
                    which_guest = get_command(prompt)
                    alt = [i for i in userslist if which_guest]
                    if alt !=[]:
                        import users.guests.guest as guest
                        guest.start_guest(which_guest)
                    
            elif set_or_log == '2':
                while True:
                    guestusername = get_name()
                    to_list = f'{guestusername},'
                    if guestusername not in userslist and guestusername != '':
                        with open(file_path, 'a') as guest_vault:
                                guest_vault.write(to_list)
                        delay_print('Guest profile created..')
                        print()
                        break
                    else:
                        delay_print('User already exist...')
                        print()
                        time.sleep(3)


    elif user_input == 3 :
        if connected():
            clear()
            os_theme()
            verify_code()
        else:
            os_theme()
            delay_print('An internet connection is needed to reset password.')
            print()
            start_wurf()
    elif user_input == 4:
        delay_print('Turning off....')
        time.sleep(3)
        exit()  
def verify_code():
    random_code = send_mail()
    prompt = "Enter unique code sent to your email : "
    email_code = get_command(prompt)
    if random_code == email_code:
        main_user_password =  set_password()
        while True:
            confirm_user_password = confirm_password()
            if confirm_user_password == main_user_password:
                file_dir = os.path.dirname(os.path.realpath('__file__'))
                file_path = os.path.join(file_dir, 'users/admin/admin.txt')
                user_logd = open(file_path)
                user_logd_l = user_logd.readline()
                user_logd_l = user_logd_l.replace('"','')
                user_logd_l = user_logd_l.split(',')
                username = user_logd_l[0]
                # print(username)
                mask_password ='*'*(len([*main_user_password]))
                print(f'Password set to {mask_password}')
                main_user_password = encrypt_password(main_user_password)
                login_details = f'{username},{main_user_password}'
                print()
                with open(file_path, 'w') as vault:
                    vault.write(json.dumps(login_details))
                delay_print("Password changed successfully restarting machine.")
                print()
                delay_print("Shutting down.....")
                print()
                time.sleep(7)
                delay_print("......Restarting......")
                start_wurf()


def send_mail():
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/email.txt')
    user_email = open(file_path)
    usermail = user_email.readline()

    sender_email = 'rambudavincent0@gmail.com'
    email_password = '' #enter gmail security key 
    owner_email = usermail
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    random_code_list = [str(random.randint(0,9)) for i in range(5)]
    random_code = ''.join(random_code_list)

    subject = "User Recovery Code"
    body = f'''Someone requested a change of password at {current_time}.
ᶦᶠ ʸᵒᵘ ᵈᶦᵈⁿᵗ ʳᵉᵠᵘᵉˢᵗ ᵗʰᶦˢ ᶦᵍⁿᵒʳᵉ.
your secret code is :  [{random_code}]
    '''
    mailsen = EmailMessage()
    mailsen['From'] = sender_email
    mailsen['To'] = owner_email
    mailsen['Subject'] = subject
    mailsen.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender_email,email_password)
        smtp.sendmail(sender_email, owner_email,mailsen.as_string())
    # listp = [*owner_email]
    g = owner_email[-11:]
    s = owner_email[:-11]
    f = len(s)
    r = '*'*(f-1)
    d = owner_email[0]+r+g

    print(f'Code sent to {d}')
    return random_code

def start_wurf():
    first_run = True
    os_theme()
    start_options()
    prompt = 'Select option : '

    while first_run == True:
        try:
            user_input = get_command(prompt)
            user_input = int(user_input)
            first_run  = False 
        except:
            continue
        
    which_user(user_input)

if __name__ == "__main__":
    start_wurf()