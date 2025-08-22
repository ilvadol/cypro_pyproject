import pandas as pd
import matplotlib.pyplot as plt
from loading_cleaning import import_and_clean_data

FIGURE_FOLDER = 'cypro_pyproject/figures/'

def genres_by_top_publishers(df, year, num = 5, region = 'Global', plot = True, save_plot = True, show_plot = False):
    # Genres by Top Publishers in Region
    # → What it shows: The genres and games released by the top publishers in a given region.
    # → Why: Helps identify market trends and popular genres among the most successful publishers.
    # Find top n publishers by sales for a given year and show the number of games published by top publishers by genre for the same year
    df_publishers = df[df['Year'] == year][['Publisher', region]].groupby('Publisher')
    ds_top_publishers = df_publishers[region].sum().sort_values(ascending=False).head(num)
    print("\n", ds_top_publishers)
    ds_top_genres = df[(df['Year'] == year) & (df['Publisher'].isin(ds_top_publishers.index))][['Genre']]
    ds_top_genres = ds_top_genres.sort_values('Genre', ascending=False)
    print("\n", ds_top_genres.value_counts())
    if plot:
        ds_top_genres.value_counts().plot(kind='bar', color='green')
        plt.title('Top Genres of ' + str(year) + ' by Top Publishers in ' + region)
        plt.xlabel(None)
        plt.ylabel('Number of Games Released')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_plot:
            FIGURE_PATH = FIGURE_FOLDER + str(year) + '_top' + str(num) + '_genres_in_' + region.replace(' ', '_') + '.png'
            plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()
        ds_top_publishers.plot(kind='bar', color='red')
        plt.title('Top Publishers of ' + str(year) + ' in ' + region)
        plt.xlabel(None)
        plt.ylabel(str(year) + ' Sales (in millions)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_plot:
            FIGURE_PATH = FIGURE_FOLDER + str(year) + '_top' + str(num) + '_publishers in ' + region.replace(' ', '_') + '.png'
            plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()

def total_sales_over_time_in_region(df, region, plot = True, save_plot = True, show_plot = False):
    # Total Sales Over Time in the Region
    # → What it shows: The total volume of sales of all games in the region by months or years.
    # → Why: It allows to understand the overall trends in the market (downturns, peaks of interest in games).
    # Grouping by year and summing up sales
    ds_global_sales_over_time = df.groupby('Year')[region].sum()
    ds_global_sales_over_time = ds_global_sales_over_time.reset_index()
    ds_global_sales_over_time['Year'] = ds_global_sales_over_time['Year'].astype(int)
    print("\n", ds_global_sales_over_time.to_string(index = False))
    if plot:
        ds_global_sales_over_time.plot(x='Year', y=region)
        plt.title('Total Sales of All Games Over Time in ' + region)
        plt.xlabel(None)
        plt.ylabel('Total Sales (in millions)')
        plt.tight_layout()
        if save_plot:
            FIGURE_PATH = FIGURE_FOLDER + 'total_sales_over_time_in_' + region.replace(' ', '_') + '.png'
            plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()

def franchise_sales_over_time(df, franchise_name, region, plot = True, save_plot = True, show_plot = False):
    # Franchise Sales Over Time
    # → What it shows: The volume of sales of one franchise broken down by months or years.
    # → Why: Helps identify the performance of the given franchise in the market.
    # Grouping by game and summing up sales
    df_franchise = df[df['Game'].str.contains(franchise_name, case=False)]
    ds_franchise_sales_over_time = df_franchise.groupby('Game')[region].sum()
    ds_franchise_sales_over_time = ds_franchise_sales_over_time.reset_index().sort_values(region, ascending=False)
    print("\n", ds_franchise_sales_over_time.to_string(index = False))
    if plot:
        ds_franchise_sales_over_time.plot(x='Game', y=region, kind='bar', color='green')
        plt.title(franchise_name + ' Franchise Sales Over Time')
        plt.xlabel(None)
        plt.ylabel(region + ' Sales (in millions)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_plot:
            FIGURE_PATH = FIGURE_FOLDER + franchise_name.replace(' ', '_') + '_franchise_sales_over_time_in_' + region.replace(' ', '_') + '.png'
            plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


def average_sales_per_genre_per_region(df, region, plot = True, save_plot = True, show_plot = False):
    # Average Sales per Genre per Region
    # → What it shows: The average volume of sales of one game in each region (NA, EU, JP, Other).
    # → Why: Helps identify regions with the highest engagement in buying games.
    # Grouping by genre and region, calculating the average sales
    ds_avg_sales = df.groupby('Genre')[region].mean().reset_index()
    ds_avg_sales = ds_avg_sales.sort_values(region, ascending=False)
    print("\n", ds_avg_sales.to_string(index=False))
    if plot:
        ds_avg_sales.plot(x='Genre', y=region, kind='bar', color='blue')
        plt.title('Average Sales per Genre in ' + region)
        plt.xlabel('Genre')
        plt.ylabel('Average Sales (in millions)')
        plt.tight_layout()
        if save_plot:
            FIGURE_PATH = FIGURE_FOLDER + region.replace(' ', '_') + '_avg_sales_per_genre.png'
            plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


if __name__ == '__main__':
    DATAPATH = "cypro_pyproject/dataset/PS4_GamesSales.csv"
    verbose = False
    df = import_and_clean_data(DATAPATH, verbose)
    genres_by_top_publishers(df, 2016, 5, 'Japan')
    total_sales_over_time_in_region(df, 'Europe')
    franchise_sales_over_time(df, 'Call of Duty', 'Global')
    average_sales_per_genre_per_region(df, 'North America')