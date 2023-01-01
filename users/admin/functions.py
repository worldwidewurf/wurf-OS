import json
import sys
import getpass
import time 
import os
from datetime import datetime
import psutil
from termcolor import colored, cprint
import bcrypt
# from apps.browser import * 
# from apps.texteditor import * 

def get_battery_life():
    battery = psutil.sensors_battery()
    battery_percentage = int(battery.percent)
    is_charging = battery.power_plugged
    
    if battery_percentage < 70:
        if is_charging:
          battery_sumbol = f'''
        ▣⚡□- {battery_percentage}%                         
    '''
        else:  
            battery_sumbol = f'''
            ▣▣□□- {battery_percentage}%                         
        '''
    elif battery_percentage > 70:
        if is_charging:
            battery_sumbol = f'''
        ▣⚡▣- {battery_percentage}%                         
    '''
        else:

            battery_sumbol = f'''
            ▣▣▣▣- {battery_percentage}%                         
        '''
    elif battery_percentage < 30:
        if is_charging:
            battery_sumbol = f'''
        ▣⚡□- {battery_percentage}%                         
    '''
        else:
            battery_sumbol = f'''
            ▣□□□- {battery_percentage}%                         
        '''
    else:

        if is_charging:
            battery_sumbol = f'''
        ▣⚠️⚡▣- {battery_percentage}%                        
    '''
        else:

            battery_sumbol = f'''
            ▣⚠️⚠️▣- {battery_percentage}%                        
        '''
    return battery_sumbol

def os_theme():

    delay_print('''🅆 🄾 🅁 🄻 🄳 🅆 🄸 🄳 🄴 🅆 🅄 🅁 🄵  🄾 🅂\n
      𝗛 𝗘 𝗟 𝗟 𝗢  𝗨 𝗦 𝗘 𝗥\n''')
    battery_sumbol =get_battery_life()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print('      ',end='')
    cprint(f'{date_time}', "white", attrs=["dark"])
    cprint(f'{battery_sumbol}', "white", attrs=["dark"])
    

def start_options():
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        admin_details = admin_file.readlines()
        if len(admin_details)==0:
            print('''      ① Setup main user\n''')
        elif len(admin_details) > 0:
            print('''      
      ① Login to main user\n''')
        
        print('''      ② Setup guest user\n''')


def get_command(prompt):
    user_input = input(prompt)
   
    return user_input
        
    

def user_name_length(username):
    if len(username)>14 :
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

def decrypt_verify(original_password,user_attempt):
    
    user_attempt = user_attempt.encode('utf-8') 

    if bcrypt.checkpw(user_attempt, original_password):
        return True
    else:
        print("incorrect password")
        return False


def get_user_details(info_list):
    username = info_list[0]
    userpassword = info_list[1]
    username_list = [*username]
    userpassword_list = [*userpassword]
    username_list.pop(0)
    userpassword_list.pop(-1)
    user = "".join(username_list)
    password = "".join(userpassword_list)
    return user,password

def which_user(user_input):
    
    if user_input == 1:
        
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, 'users/admin/admin.txt')

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
                        login_details = f'{username}, {main_user_password}'
                        with open(file_path, 'w') as vault:
                            vault.write(json.dumps(login_details))
                        print()
                        time.sleep(7)
                        delay_print("Profile created, restarting the machine.")
                        print()
                        delay_print("Shutting down.....")
                        print()
                        break
                    else:
                        print("Passwords donnot match.")
                        continue
        user_details = open(file_path)
        get_info = user_details.read().split(',')
        user_name, password = get_user_details(get_info)
        print('Wᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ '+ user_name)
        prompt = 'Enter password for ' + user_name
        while True:
            login_pass = get_password(prompt)
            if decrypt_verify(password,login_pass):
                homefile_dir = os.path.dirname(os.path.realpath('__file__'))
                homefile_path = os.path.join(homefile_dir, 'users/admin/admin_user.py')
                os.startfile(homefile_path)
            else:
                continue
       




                
                
            
                
            
                       

                    




def start_wurf():
    first_run = True
    os_theme()
    # start_options()
    # prompt = 'Select option : '

    # while first_run == True:
    #     try:
    #         user_input = get_command(prompt)
    #         user_input = int(user_input)
    #         first_run  = False 
    #     except:
    #         continue
        
    # which_user(user_input)

if __name__ == "__main__":
    start_wurf()