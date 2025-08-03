# Importing modules
import sys
import os
import time
import random
sys.path.append('cypro_pyproject')
import graphics_messages as gm
import analysis_plotting as ap
import loading_cleaning as lc

#==================#
# Global variables #
#==================#

DATAPATH = "cypro_pyproject/dataset/PS4_GamesSales.csv"
verboseMode = False
ShowPlots = True

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
    global verboseMode
    verboseMode = not verboseMode
    print ("Verbose mode: " + ("ON\nYou will see a TON of additional information" if verboseMode else "OFF"))
    wait_for_key()

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
def check_commandCall(entered_input):
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

#================#
# Menu functions #
#================#

def print_mainmenu():
    clear_screen()
    print_centered(gm.menugraphic)
    print(gm.mainmenu_text)

def loadData():
    global DATAPATH
    global DataFrame
    DataFrame = lc.import_and_clean_data(DATAPATH, verboseMode)
    print("Data imported.")
    wait_for_key()

def analyseData():
    global DataFrame
    global ShowPlots
    Year = input("Choose a year:\n>>> ")
    check_commandCall(Year)
    Year = int(Year)
    Top = input("Choose a number of top publishers:\n>>> ")
    check_commandCall(Top)
    Top = int(Top)
    ap.genres_by_top_publishers(df=DataFrame, year=Year, num=Top, show_plot=ShowPlots)
    Region = input("Choose a region:\n>>> ")
    check_commandCall(Region)
    ap.total_sales_over_time_in_region(df=DataFrame, region=Region, show_plot=ShowPlots)
    Franshise = input("Choose a franchise:\n>>> ")
    check_commandCall(Franshise)
    Region = input("Choose a region:\n>>> ")
    check_commandCall(Region)
    ap.franchise_sales_over_time(df=DataFrame, franchise_name=Franshise, region=Region, show_plot=ShowPlots)
    Region = input("Choose a region:\n>>> ")
    check_commandCall(Region)
    ap.average_sales_per_genre_per_region(df=DataFrame, region=Region, show_plot=ShowPlots)

def main():
    print_welcome()
    while True:
        print_mainmenu()
        userInput = input(">>> ")
        check_commandCall(userInput)
        match userInput:
            case '1':
                global DATAPATH
                loadData()
            case '2':
                if DataFrame is None:
                    print ("No data loaded. Please load data first.")
                    wait_for_key()
                else:
                    analyseData()
            case '3':
                exit_program()
            case _:
                print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    DataFrame = None
    main()