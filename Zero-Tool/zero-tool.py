import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 ____   ____    ___   _   _   _____ ___   ____
|  _ \ / ___|  / _ \ | \ | | |_   _/ _ \ |  _ \
| |_) | |     | | | ||  \| |   | || | | || |_) |
|  _ <| |___  | |_| || |\  |   | || |_| ||  __/
|_| \_\\____| \ ___ /|_| \_|   |_| \___/ |_|                Developer - Rc
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Rc ! 
""")

def display_menu():
    print(Fore.RED + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. Otp Bypsss                   | 7. TOKENS  
    2. 2fa ig bypass                | 8. MASS BANNING
    3. Qr grab                      | 9. TOKEN GRABBER
    4. Api Down                     | 10. COOKIE GRABBER
    5. Info leaker                  | 11. IG KEY GRABBER
    6. Link grabber                 | 12. Phone Grabber
    
    - Note -: Pvt tool ask key from attaker Developer !
    
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/ip-lookup.py"' if os.name == 'nt' else 'python Zero-Tool/ip-lookup.py')
    elif command == '2':
        os.system('cmd /k "python Zero-Tool/nuke-bot/main.py"' if os.name == 'nt' else 'python Zero-Tool/nuke-bot/main.py')
    elif command == '3':
        os.system('cmd /k "python Zero-Tool/Subdirectory-scanner/main.py"' if os.name == 'nt' else 'python Zero-Tool/Subdirectory-scanner/main.py')
    elif command == '4':
        os.system('cmd /k "python Zero-Tool/email-bomber.py"' if os.name == 'nt' else 'python Zero-Tool/email-bomber.py')
    elif command == '5':
        os.system('cmd /k "python Zero-Tool/phone-locator.py"' if os.name == 'nt' else 'python Zero-Tool/phone-locator.py')
    elif command == '6':
        os.system('cmd /k "python Zero-Tool/port-scanner.py"' if os.name == 'nt' else 'python Zero-Tool/port-scanner.py"')
    elif command == '7':
        os.system('cmd /k "python Zero-Tool/subdomain/main.py"' if os.name == 'nt' else 'python Zero-Tool/subdomain/main.py')
    elif command == '8':
        os.system('cmd /k "python Zero-Tool/ddos.py"' if os.name == 'nt' else 'python Zero-Tool/ddos.py')
    elif command == '9':
        os.system('cmd /k "python Zero-Tool/discord-token-grabber.py"' if os.name == 'nt' else 'python Zero-Tool/discord-token-grabber.py')
    elif command == '10':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Keylogger.py"')
    elif command == '11':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Web-Crawler.py"')
    elif command == '12':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Reverse-Shell.py"')
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
