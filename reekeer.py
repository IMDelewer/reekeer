import getpass
import os
import sys

version = 1.1

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
LIGHT_BLUE = "\033[1;34m"
END = "\033[0m"

def print_centered_text(text):
    lines = text.splitlines()  # Используем метод splitlines() для разделения строк
    terminal_width = os.get_terminal_size().columns

    for line in lines:
        centered_line = line.center(terminal_width)
        print(centered_line)

class Menu():
    def main():
        os.system("cls")
        menu= '''     
        █▀▀█ █▀▀ █▀▀ █░█ █▀▀ █▀▀ █▀▀█
        █▄▄▀ █▀▀ █▀▀ █▀▄ █▀▀ █▀▀ █▄▄▀
        ▀░▀▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀▀▀ ▀░▀▀
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                             ┃
        ┃             Welcome to main menu            ┃
        ┃         Type 'help' to show commands        ┃
        ┃                                             ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(BLUE)
        print_centered_text(menu)
        print(END)
    def help():
        os.system("cls")
        menu= '''     
        █▀▀█ █▀▀ █▀▀ █░█ █▀▀ █▀▀ █▀▀█
        █▄▄▀ █▀▀ █▀▀ █▀▄ █▀▀ █▀▀ █▄▄▀
        ▀░▀▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀▀▀ ▀░▀▀
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                             ┃
        ┃   main      help      extensions      info  ┃
        ┃             Created by reekeer              ┃
        ┃                                             ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(BLUE)
        print_centered_text(menu)
        print(END)
    def extensions(extensions):
        os.system("cls")
        menu= f'''     
        █▀▀█ █▀▀ █▀▀ █░█ █▀▀ █▀▀ █▀▀█
        █▄▄▀ █▀▀ █▀▀ █▀▄ █▀▀ █▀▀ █▄▄▀
        ▀░▀▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀▀▀ ▀░▀▀
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                             ┃
        ┃            Here all extensions:             ┃
        ┃{extensions}┃
        ┃                                             ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(BLUE)
        print_centered_text(menu)
        print(END)
    def info():
        os.system("cls")
        menu= f'''     
        █▀▀█ █▀▀ █▀▀ █░█ █▀▀ █▀▀ █▀▀█
        █▄▄▀ █▀▀ █▀▀ █▀▄ █▀▀ █▀▀ █▄▄▀
        ▀░▀▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀▀▀ ▀░▀▀
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                             ┃
        ┃     Version: {version}   Created by imdelewer     ┃
        ┃    discord: delewer     github: IMDelewer   ┃
        ┃                                             ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        print(BLUE)
        print_centered_text(menu)
        print(END)  
class Console():
    def terminal():
        command = input("[reekeer@"+getpass.getuser()+"] : ")
        
        if command == "main":
            Menu.main()
            Console.terminal()
        elif command == "help" or command == "h":
            Menu.help()
            Console.terminal()
        elif command ==  "quit" or command == "q":
            sys.exit()
        elif command == "info" or command == "i":
            Menu.info()
            Console.terminal()
        else:
            print("Unknown command. See commands in 'help' ")
Menu.main()
Console.terminal()

