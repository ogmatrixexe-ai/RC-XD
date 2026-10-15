import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                
____   ____    ___   _   _   _____ ___   ____
|  _ \ / ___|  / _ \ | \ | | |_   _/ _ \ |  _ \
| |_) | |     | | | ||  \| |   | || | | || |_) |
|  _ <| |___  | |_| || |\  |   | || |_| ||  __/                Attaker ! 
|_| \_\\____|  \___/ |_| \_|   |_| \___/ |_|                   Developer - Rc !!
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Rc ( For Hacking & Bypass )
""")

def display_menu():
    print(Fore.GREEN + """
    1: Rc Attaker (Hacking Tools)      | 2: Rc Op
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/zero-tool.py"' if os.name == 'nt' else 'python Zero-Tool/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
