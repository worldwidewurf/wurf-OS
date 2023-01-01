from contextlib import redirect_stdout
from io import StringIO
import json
import os
import random
import re
import sys

file_dir = os.path.dirname(os.path.realpath('__file__'))
file_path = os.path.join(file_dir, 'users/guests/guest.txt')
user_logd = open(file_path)
userslist = user_logd.read().strip().split(',')

guestusername = input('ent ')
to_list = f'{guestusername}, '
with open(file_path, 'a') as guest_vault:
        guest_vault.write(to_list)
# import uuid
# i = input('in ').lower()
# print(i)
# s = 'aab'
# ls = [*s]
# if ls[0] is ls[1] is ls[2]:
#     print('you won')
# else:
#     print('match drawn')
# joins elements of getnode() after each 2 digits.
# import os
# print(os.system('ipconfig'))  

# print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range(0,8*6,8)][::-1]))
# print(sys.platform)
# f = StringIO()

# with redirect_stdout(f):
#     k = 'this is fresh'
#     print(k)
# centerd = f.getvalue()
# print(centerd.center(110))
# prompt = 'Select : '
# while True:
#     try:
#         user_selection = int(input(prompt))
#         break 
#     except:
#         continue
# random_code = [str(random.randint(0,9)) for i in range(5)]
# j = ''.join(random_code)
# print(j)
# k = 'abcdef@gmail.com'
# # listp = [*k]
# g = k[-11:]
# s = k[:-11]
# f = len(s)
# r = '*'*(f-1)
# d = k[0]+r+g
# print(d)
# k.replace()
# def request_email():
#     file_dir = os.path.dirname(os.path.realpath('__file__'))
#     file_path = os.path.join(file_dir, 'users/admin/email.txt')
#     prompt = 'Register account e-mail : '
#     while True:
#         email = input(prompt)
#         regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#         if(re.fullmatch(regex, email)):
#             prompt = 'Verify e-mail : '
#             while True:
#                 verify_email = input(prompt)
#                 if verify_email == email:
#                     with open(file_path, 'w') as mail_box:
#                             mail_box.write(json.dumps(email))
#                 break
#         break


# request_email()
# import os
# def get_user_details(info_list):
#     username = info_list[0]
#     userpassword = info_list[1]
#     username_list = [*username]
#     userpassword_list = [*userpassword]
#     username_list.pop(0)
#     userpassword_list.pop(-1)
#     user = "".join(username_list)
#     password = "".join(userpassword_list)
#     return user,password
# file_dir = os.path.dirname(os.path.realpath('__file__'))
# file_path = os.path.join(file_dir, 'users/admin/admin.txt')
# user_details = open(file_path)
# get_info = user_details.read().split(',')
# print(get_user_details(get_info))


# # print(get_info)




# import bcrypt


# hashed = b'$2b$10$mLYCy2nHdzBCX4vaaRt2vOobqmBfBnr8jnsZzmeIZCXebOWxHVaEG'
# print(hashed)
# # <strong># Create an authenticating password input field to check if a user enters the correct password</strong> 
# check = str(input("check password: ")) 

# # <strong># Encode the authenticating password as well</strong> 
# check = check.encode('utf-8') 
# print(check)
# # <strong># Use conditions to compare the authenticating password with the stored one</strong>:
# if bcrypt.checkpw(check, hashed):
#     print("login success")
# else:
#     print("incorrect password")



# name = input('name')
# password_prompt      = "Setup user password : "
# password = getpass.getpass(password_prompt)
# details = {'Username': name,
# 		'Password' : password}

# with open('convert.txt', 'w') as convert_file:
# 	convert_file.write(json.dumps(details))



# import random

# stru = 'thisworld'

# print('*'*len([*stru]))


# password = "Ra360"
# print(len(password))
# special_chars      =  " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
# special_char_list  = [*special_chars]
# password_list      = [*password]
# test_caps          = 0
# test_lower         = 0
# test_num           = 0
# test_chars         = 0
# if password_list != []:
#     for letter in password_list:
#         if letter.isupper():
#             test_caps += 1
#         if letter.islower():
#             test_lower += 1
#         elif letter.isdigit():
#             test_num  += 1
#         elif letter in special_char_list:
#             test_chars+= 1
#     message_list = []
#     if test_caps == 0:
#         message = "Password must have atleat 1 caps character."
#         message_list.append(message)
#     if test_lower == 0:
#         message1 = "Password must have atleat 1 lower character."
#         message_list.append(message1)
#     if test_num == 0:
#         message2 = "Password must have atleat 1 number character."
#         message_list.append(message2)
#     if test_chars == 0:
#         message3 = "Password must have atleat 1 special character."
#         message_list.append(message3)
#     if test_caps == 0 or test_num == 0 or test_chars == 0 or test_lower == 0:
#         for warning in message_list:
#             print(warning)
#         # return False
#     else:
#         print('password set')
# else:
#     print('Password cannot be empty.')
#     # return False
