# Importing modules
import sys
import os
import time
import random
import graphics_and_messages as gm

#==================#
# Global variables #
#==================#

verbose = False

#===============#
# CLI functions #
#===============#

# Defining wait_for_key function

if os.name == 'nt':  # Windows
    import msvcrt

    def wait_for_key():
        print('Press any key to continue. Press ESC to exit.')
        while True:
            key = msvcrt.getch()
            if key == b'\x1b':  # ESC key
                print('Exiting...')
                sys.exit(0)
            else:
                break

else:  # Unix (Linux/macOS)
    import termios
    import tty

    def wait_for_key():
        print('Press any key to continue. Press ESC to exit.')
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # ESC key
                print('Exiting...')
                sys.exit(0)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# Defining a function to center text
def print_centered(text):
    # Get the terminal width
    terminal_width = os.get_terminal_size().columns

    # Center each line
    centered_text = "\n".join(line.center(terminal_width) for line in text.splitlines())

    # Print the centered text
    print(centered_text)

#==================#
# Global functions #
#==================#

# Defining the function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Defining the function to print verbose information
def switch_verbose():
    global verbose 
    verbose = not verbose
    print ("Verbose mode: " + ("ON\nYou will see the steps of advanced calculations plus additional information" if verbose else "OFF"))

# Defining the function to exit the program
def exit_program():
    clear_screen()
    print_centered(gm.goodbyemessage)
    exit()

# Defining the function to print the help message
def print_help():
    clear_screen()
    print_centered(gm.helpmessage)
    wait_for_key()
    clear_screen()

# Defining the function to print the welcome message
def print_welcome():
    clear_screen()
    print_centered(gm.welcomemessage)
    wait_for_key()
    clear_screen()

# Defining the command list
command_list = {
    "clear": clear_screen,
    "clr": clear_screen,
    "help": print_help,
    "exit": exit_program,
    "verbose": switch_verbose,
    "ver": switch_verbose
}

# Defining the function that checks the input against the command list
def check_input(entered_input):
    entered_input = str(entered_input).lower()
    func = command_list.get(entered_input)
    if func is exit_program:
        func()
    if func is not None:
        print (f"Executing command: " + entered_input)
        time.sleep(random.uniform(0.1, 0.5))
        func()
        return None
    else:
        return entered_input

#===============#
# Menu function #
#===============#

def print_menu():
    clear_screen()
    print_centered(gm.menugraphic)
    print(gm.menutext)

def main():
    print_welcome()
    while True:
        print_menu()
        INPUT = input(">>> ")
        check_input(INPUT)

if __name__ == "__main__":
    main()
