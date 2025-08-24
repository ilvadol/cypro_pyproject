helpgraphic = """
##############################################
#  ____  ____  ________  _____     _______   #
# |_   ||   _||_   __  ||_   _|   |_   __ \  #
#   | |__| |    | |_ \_|  | |       | |__) | #
#   |  __  |    |  _| _   | |   _   |  ___/  #
#  _| |  | |_  _| |__/ | _| |__/ | _| |_     #
# |____||____||________||________||_____|    #
##############################################
"""

helpmessage = """
CyPro Sales Data Analyzer

A CLI-wrapped program for analyzing sales data, providing insights into market trends and patterns. Key features include:

* Data cleaning and preprocessing with options to fix data types, delete missing values, fill missing values, and remove duplicates
* Export of cleaned data for further analysis
* Analysis and visualization of sales data, including KPIs such as:
	+ Top publishers by sales
	+ Genres and games released by top publishers in a given region
	+ Market trends and popular genres among the most successful publishers

To print this help message from anywhere, type 'help'.
To enable verbose mode, type 'verbose' or 'ver'.
To clear the screen, type 'clear' or 'clr'.
To go back to the main menu, type 'menu'.
To show plots on the screen, type 'showplots' or 'shplt'.
To save plots to disc, type 'saveplots' or 'svplt'.
To exit the program, type 'exit' or 'quit'.

Authors: Ilia Oleinikov & Svetlana Saveleva, copyright (c) 2025, licensed under the WTFPL License
"""

goodbyemessage = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠴⠒⠤⣄⡀⠀⠀⠀⠀⢠⣾⠉⠉⠉⠉⠑⠒⠦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠉⠲⡄⠀⢠⠏⡏⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢤⣤⣀⡀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⢸⠀⡇⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⣿⠀⠀⠀⢰⣿⣷⣆⠀⠀⠀⠘⣾⠀⠇⠀⠀⠀⢾⣿⣿⣦⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡤⣄⠀⠀⠀⣼⡇⠀⠀⠀⢀⣀⠀⠀⠀⠈⠳⣴⢿⡄⠀⠀⢸⡿⣿⢹⠀⠀⠀⠀⣿⠀⡆⠀⠀⠀⣼⠻⣇⣸⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠚⠉⠀⠀⠈⠳⡄⠀⣿⡇⠀⠀⠀⣿⣿⡷⡄⠀⠀⠀⢹⣆⢧⠀⠀⠀⠙⠿⠋⠀⠀⠀⠀⣿⠀⡇⠀⠀⠀⠙⠛⠉⠁⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠟⠀⠀⠀⠀⢀⣤⣾⣷⣀⡇⢣⠀⠀⠀⢻⣟⣄⣷⠀⠀⠀⠈⣿⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⢰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡏⠀⠀⠀⣼⡟⣿⣿⡿⠛⠉⢻⣞⣧⠀⠀⠀⠉⠛⠁⠀⠀⠀⠀⡿⣿⣿⣦⣀⠀⠀⠀⠀⣠⣾⡏⢸⣠⣧⣤⣄⣤⣤⣤⣤⣤⣴⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⢸⠋⣿⠛⠁⠀⠀⠀⠀⠻⣯⣷⣄⠀⠀⠀⠀⠀⠀⢀⣼⠁⠘⠿⣿⣿⣻⣿⣿⣿⣿⠏⠀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡟⣇⠀⠀⠈⢿⣏⢧⣴⣶⡆⠀⠀⠀⢿⣿⣿⢳⢦⣤⣤⣤⣶⣿⠟⠀⠀⠀⠀⠉⠉⠛⠋⢩⡤⠖⠒⠛⠛⡿⢁⣾⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣷⠀⠀⠀⠀⢀⣤⠤⠤⣀⡀⠀
⣇⠘⣆⠀⠀⠀⠙⠻⠿⠛⠃⠀⠀⠀⣸⡙⠻⢿⣿⣿⣿⣿⠿⠋⠀⣀⡤⠤⠒⠚⠳⣄⢠⣿⠁⠀⠀⠀⢠⠇⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⢀⡴⢫⡇⠀⠀⠀⠈⠙
⠘⣶⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⣀⣼⣿⠇⠀⠀⠀⣀⣀⣀⠀⢀⣼⣿⣦⡀⠀⠀⠀⠈⢻⡏⠀⠀⠀⠀⡞⠀⡇⢸⠀⠀⠀⠀⢰⣾⣶⣶⣶⣶⣶⡏⠀⠀⡼⠀⡞⠀⠀⠀⠀⠀⢸
⠀⠈⠻⣿⣿⣿⣶⢶⡶⡶⣶⣾⣿⡿⠋⣠⠴⠚⠉⠁⠀⠉⠙⠺⡿⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣸⠃⢰⠀⢸⠀⠀⠀⠀⠘⠛⠛⠿⠿⢿⡏⠀⠀⢰⠃⢠⠇⠀⠀⠀⠀⡜⠌
⠀⠀⠀⠈⠙⠻⠿⠼⠽⠿⠿⠟⠋⢰⡟⠁⠀⠀⢀⣤⣄⡀⠀⠀⠹⡆⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⢰⡇⠀⢸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡞⠀⡜⠀⠀⠀⠀⠀⠀⢰
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢳⡀⠀⠀⠈⢿⡿⠇⠀⠀⣼⠃⠀⠀⠙⢿⣿⣿⣷⠀⠀⠀⠈⡇⠀⢸⠀⡄⠀⠀⠀⠀⢰⣶⣤⣤⣤⣼⠃⠀⢰⠃⢰⠃⠀⠀⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⢣⠀⠀⠀⠀⠀⠀⠀⠈⠋⠉⠲⣄⠀⠀⠙⢿⠸⡄⠀⠀⠀⢳⠀⢸⠀⡇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣃⠀⠀⣞⣠⣾⣤⣀⣀⠀⠀⡄⣀⡞
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠈⣇⠀⠀⠀⠀⣠⣤⣀⠀⠀⠀⠘⣆⠀⠀⠸⡄⢳⠀⠀⠀⠸⡆⢸⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠻⢿⣿⣿⣿⣿⡿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠘⡄⠀⠀⠀⢻⣿⣿⠆⠀⠀⠀⢸⠀⠀⠀⣇⠘⡆⠀⢀⣀⣧⢸⢀⣿⣶⣤⣤⣤⣀⣀⣀⠀⢀⡏⠀⢀⣴⠟⠁⠀⠀⠈⢳⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠹⡄⠀⠀⠈⠉⠁⠀⠀⠀⣠⡾⠀⠀⠀⢹⢀⣿⣿⣿⡿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢰⣯⡏⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠹⡄⠀⠀⠀⢀⣠⣴⣾⣿⠃⠀⠀⠀⠘⠿⠟⠛⠛⠁⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠟⠁⠀⠀⢾⣿⣷⣄⡀⠀⠀⢀⡼⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⢳⣴⣶⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
#########################################################################
#                                                                       #
#                             Have a nice day!                          #
#                                                                       #
#########################################################################
"""

welcomemessage = """
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄

▀█▀ █▀█
░█░ █▄█

█▀█ █▀ █░█   █▀ ▄▀█ █░░ █▀▀ █▀
█▀▀ ▄█ ▀▀█   ▄█ █▀█ █▄▄ ██▄ ▄█

█▀█ █▀▀ █▀█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▀ █▀▀
█▀▀ ██▄ █▀▄ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █░▀█ █▄▄ ██▄

█▄▀ █▀█ █   █▀▄ ▄▀█ █▀ █░█ █▄▄ █▀█ ▄▀█ █▀█ █▀▄
█░█ █▀▀ █   █▄▀ █▀█ ▄█ █▀█ █▄█ █▄█ █▀█ █▀▄ █▄▀
"""

menugraphic = """
========================================================.
     .-.      .-.       .--.                            |
    | OO|    | OO|     / _.-'.-.    .-.    .-.    .''.  |
    |   |    |   |     \  '-.'-'    '-'    '-'    '..'  |
    '^^^'    '^^^'      '--'                            |
.==================.  .-.  .====================.  .-.  |
|                  | |   | |                    |  '-'  |
| █▀▄▀█ ▄▀█ █ █▄░█ | |   | | █▀▄▀█ █▀▀ █▄░█ █░█ |       |
| █░▀░█ █▀█ █ █░▀█ | ':-:' | █░▀░█ ██▄ █░▀█ █▄█ |  .-.  |
|                  |  '-'  |                    |  '-'  |
'=================='       '===================='       |
"""

mainmenu_text = """
Select an option:
1. Load Dataset
2. Analyze Dataset
3. Exit

Type 'help' for more information
"""

analysismenu_graphic = """
▄▀█ █▄░█ ▄▀█ █░░ █▄█ █▀ █ █▀
█▀█ █░▀█ █▀█ █▄▄ ░█░ ▄█ █ ▄█

█▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ ██▄ █░▀█ █▄█
"""

analysismenu_text = """
Select an option:
1. Top Publishers and Genres by Top Publishers in Region
2. Total Sales Over Time in Region
3. Franchise Sales Over Time in Region
4. Average Sales per Genre per Region
5. Go Back
6. Exit

Type 'sample' to see a sample of each metric
"""

genres_by_top_publishers_text = """
Top Publishers and Genres by Top Publishers in Region

The metric is useful because it identifies leading publishers in specific regions, helping to understand regional market trends and preferences.
It also highlights the most successful genres, providing insights into consumer interests and aiding in strategic planning for game development and marketing efforts.
This information can guide publishers in optimizing their portfolios for regional success.
"""

total_sales_over_time_in_region_text = """
Total Sales Over Time in Region

The metric is useful because it provides insights into the dynamics of the video game market in a given region.
It shows the overall sales trend over time, which can be used to identify periods of growth or decline.
This information can be used to make strategic decisions, such as optimizing marketing budgets or adjusting product offerings to align with changing market trends. 
Additionally, comparing sales trends across different regions can help identify regional differences and opportunities.
"""

franchise_sales_over_time_text = """
Franchise Sales Over Time in Region

The metric is useful because it provides insights into the sales performance of a specific franchise in a given region over time. 
This information can help identify trends, peaks, and declines in sales, which are crucial for strategic planning and decision-making. 
Understanding franchise sales trends allows businesses to optimize marketing campaigns, product launches, and inventory management to maximize revenue and market share.
"""

average_sales_per_genre_per_region_text = """
Average Sales per Genre per Region

The metric is useful because it provides insights into the sales performance of specific genres in a given region.
It shows the average number of game sales per genre, which can help identify opportunities for growth and areas where a business should focus its marketing efforts.
This information can be used to optimize product offerings, marketing campaigns, and pricing strategies to maximize revenue and market share.
"""
