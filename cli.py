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
SavePlots = True

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

def switch_showPlots():
    global ShowPlots
    ShowPlots = not ShowPlots
    print ("Showing plots: " + ("ON\nYou will see the plots" if ShowPlots else "OFF\nThe plots will not be shown"))
    wait_for_key()

def switch_savePlots():
    global SavePlots
    SavePlots = not SavePlots
    print ("Saving plots: " + ("ON\nThe plots will be saved to a file" if SavePlots else "OFF\nThe plots will not be saved to a file"))
    wait_for_key()

def switch_mainMenuFlag():
    global mainMenuFlag
    mainMenuFlag = not mainMenuFlag
    print ("Main menu flag: " + ("TRUE" if mainMenuFlag else "FALSE"))
    wait_for_key()

# Defining the function to exit the program
def exit_program():
    clear_screen()
    print_centered(gm.goodbyemessage)
    exit()

# Defining the function to print the help message
def print_help():
    clear_screen()
    print_centered(gm.helpgraphic)
    print(gm.helpmessage)
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
    "quit": exit_program,
    "verbose": switch_verbose,
    "ver": switch_verbose,
    "showplots": switch_showPlots,
    "shplt": switch_showPlots,
    "saveplots": switch_savePlots,
    "svplt": switch_savePlots,
    "menu": switch_mainMenuFlag
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
    global verboseMode
    global DataFrame
    DataFrame = lc.import_and_clean_data(DATAPATH, verboseMode)
    print("Data imported.")
    wait_for_key()

def analyseData():
    global DataFrame
    global ShowPlots
    global SavePlots
    global mainMenuFlag
    if DataFrame is None:
        print ("No data loaded. Please load data first.")
        wait_for_key()
        return
    while mainMenuFlag == False:
        clear_screen()
        print_centered(gm.analysismenu_graphic)
        print(gm.analysismenu_text)
        userChoice = input("Choose an option:\n>>> ")
        check_commandCall(userChoice)
        match userChoice:
            case "1":
                print(gm.genres_by_top_publishers_text)
                print('DataFrame Columns:')
                print(DataFrame.columns.tolist())
                print('\nYear range in DataFrame: ' + str(int(DataFrame['Year'].max())) + '-' + str(int(DataFrame['Year'].min())))
                userYear = input("Choose a single year:\n>>> ")
                if userYear == '' or userYear.isalpha():
                    print("Error: year is not a digit or is empty. Going back...")
                    wait_for_key()
                    continue
                if int(userYear) < int(DataFrame['Year'].min()) or int(userYear) > int(DataFrame['Year'].max()):
                    print("Error: year is not in the range of the DataFrame. Going back...")
                    wait_for_key()
                    continue
                userYear = int(userYear)
                userTop = input("Choose a number of top publishers:\n>>> ")
                if userTop == '' or userTop.isalpha():
                    print("Error: number of top publishers is not a digit or is empty. Going back...")
                    wait_for_key()
                    continue
                if int(userTop) > int(DataFrame['Publisher'].nunique()):
                    print("Error: number of top publishers is higher than the number of unique publishers in the DataFrame. Going back...")
                    wait_for_key()
                    continue
                userTop = int(userTop)
                userRegion = input("Choose a region:\n>>> ")
                if userRegion == '' or userRegion.isnumeric():
                    print("Error: region is not a string or is empty. Going back...")
                    wait_for_key()
                    continue
                if userRegion not in DataFrame.columns.tolist():
                    print("Error: region is not a column in the DataFrame. Going back...")
                    wait_for_key()
                    continue
                ap.genres_by_top_publishers(df=DataFrame, year=userYear, num=userTop, region=userRegion, save_plot=SavePlots, show_plot=ShowPlots)
            case "2":
                print(gm.total_sales_over_time_in_region_text)
                print('DataFrame Columns:')
                print(DataFrame.columns.tolist())
                userRegion = input("Choose a region:\n>>> ")
                if userRegion == '' or userRegion.isnumeric():
                    print("Error: region is not a string or is empty. Going back...")
                    wait_for_key()
                    continue
                if userRegion not in DataFrame.columns.tolist():
                    print("Error: region is not a column in the DataFrame. Going back...")
                    wait_for_key()
                    continue
                ap.total_sales_over_time_in_region(df=DataFrame, region=userRegion, save_plot=SavePlots, show_plot=ShowPlots)
            case "3":
                print(gm.franchise_sales_over_time_text)
                print('DataFrame Columns:')
                print(DataFrame.columns.tolist())
                userFranshise = input("Choose a franchise:\n>>> ")
                if userFranshise == '' or userFranshise.isnumeric():
                    print("Error: franchise is not a string or is empty. Going back...")
                    wait_for_key()
                    continue
                userRegion = input("Choose a region:\n>>> ")
                if userRegion == '' or userRegion.isnumeric():
                    print("Error: region is not a string or is empty. Going back...")
                    wait_for_key()
                    continue
                if userRegion not in DataFrame.columns.tolist():
                    print("Error: region is not a column in the DataFrame. Going back...")
                    wait_for_key()
                    continue
                ap.franchise_sales_over_time(df=DataFrame, franchise_name=userFranshise, region=userRegion, save_plot=SavePlots, show_plot=ShowPlots)
            case "4":
                print(gm.average_sales_per_genre_per_region_text)
                print('DataFrame Columns:')
                print(DataFrame.columns.tolist())
                userRegion = input("Choose a region:\n>>> ")
                if userRegion == '' or userRegion.isnumeric():
                    print("Error: region is not a string or is empty. Going back...")
                    wait_for_key()
                    continue
                ap.average_sales_per_genre_per_region(df=DataFrame, region=userRegion, save_plot=SavePlots, show_plot=ShowPlots)
            case "5":
                mainMenuFlag = True
            case "6":
                exit_program()
            case "sample":
                print("Sample data are being generated...")
                print("Showing Top Genres of 2016 by Top Publishers in Japan...")
                ap.genres_by_top_publishers(DataFrame, 2016, 5, 'Japan', save_plot=False, show_plot=True)
                wait_for_key()
                print("Showing total sales over time in Europe...")
                ap.total_sales_over_time_in_region(DataFrame, 'Europe', save_plot=False, show_plot=True)
                wait_for_key()
                print("Showing Call of Duty franchise sales over time in Global...")
                ap.franchise_sales_over_time(DataFrame, 'Call of Duty', 'Global', save_plot=False, show_plot=True)
                wait_for_key()
                print("Showing average sales per genre in North America...")
                ap.average_sales_per_genre_per_region(DataFrame, 'North America', save_plot=False, show_plot=True)
                wait_for_key()
            case None:
                continue
            case _:
                print("Invalid choice. Please try again.")
                wait_for_key()

def main():
    print_welcome()
    global mainMenuFlag
    while True:
        mainMenuFlag = True
        print_mainmenu()
        userInput = input(">>> ")
        userInput = check_commandCall(userInput)
        match userInput:
            case '1':
                global DATAPATH
                loadData()
            case '2':
                if DataFrame is None:
                    print ("No data loaded. Please load data first.")
                    wait_for_key()
                else:
                    mainMenuFlag = False
                    analyseData()
            case '3':
                exit_program()
            case None:
                continue
            case _:
                print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    DataFrame = None
    mainMenuFlag = False
    main()