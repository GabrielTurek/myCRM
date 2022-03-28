import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("")
print("")
print("")
print("  A wizard is never late, nor is he early. He arrives precisely when he means to.\n")
print(f"{bcolors.OKCYAN}██      ███████ ███████ ████████     ███████ ██  █████  ██████  ███████ ███    ███")
print(f"██      ██      ██         ██        ██      ██ ██   ██ ██   ██ ██      ████  ████") 
print(f"██      █████   █████      ██        ███████ ██ ███████ ██████  █████   ██ ████ ██") 
print(f"██      ██      ██         ██             ██ ██ ██   ██ ██   ██ ██      ██  ██  ██") 
print(f"███████ ███████ ███████    ██        ███████ ██ ██   ██ ██   ██ ███████ ██      ██{bcolors.ENDC}\n\n")

#input("Press any key for menu")

    # Sprawdzamy czy baza odpowiada
addr = "8.8.8.8"
print('----Halo baza?----')

response = os.popen(f"ping {addr}").read()
if "Received = 4" in response:
    print(f"{bcolors.OKGREEN}Database UP!{bcolors.ENDC}{bcolors.OKBLUE} {addr}{bcolors.ENDC}\n\n ")
else:
    print(f"Database DOWN {addr} Ping Unsuccessful")

menu_options = {
    0: 'Show notifications',
    1: 'Add customer',
    2: 'Add note',
    3: 'Serch',
    4: 'Run Python Command',
    3: 'Test DB Connection',
    5: 'Exit',

}


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option0():
     print('Handle option \'Option 0\'')

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

def option4():
     print('Handle option \'Option 5\'')

def option5():
     print('Handle option \'Option 5\'')

while(True):
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
         print('Wrong input. Please enter a number ...')

#Check what choice was entered and act accordingly

    if option == 0:
        option0()
    elif option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option3()
    elif option == 5:
        print('Do roboty!')
        exit()
    else:
        print('Invalid option. Please enter a number between 0 and 5.')