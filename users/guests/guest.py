from wurf_OS import *


def welcome(user):
    os_theme()
    print(f'welcome back {user}:'.center(139))
    print('''Available Games.\n'''.center(139))
    print('''① Rock Paper Scissors\n'''.center(139))
    print('''② Tic Tac Toe\n'''.center(139))
    print('''③ Guide\n'''.center(139))
    print(f'''➍ log out of {user} \n'''.center(139))

def start_guest(user=''):
    select_guest_games(user)

def select_guest_games(user):
    
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, 'users/admin/admin.txt')

    with open(file_path) as admin_file:
        get_info = admin_file.read().split(',')
        user_name, password = get_user_details(get_info)
    prompt = f'{user}@{user_name}-$ :  '
    back = 'N'
    while back == 'N':
        while True:
            try:
                welcome(user)
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
            delay_print(f'Logging out of {user}...')
            start_wurf()

if __name__ == "__main__":
    start_guest()