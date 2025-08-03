import pandas as pd
import matplotlib.pyplot as plt
from loading_cleaning import import_and_clean_data

FIGURE_FOLDER = 'cypro_pyproject/figures/'

def genres_by_top_publishers(df, year, num = 5, plot = True, show_plot = False):
    # найти топ n издательств по продажам за определенный год
    # показать число игр, опубликованных топовыми издательствами, по жанрам за тот же год
    # эта функция показывыет на основе данных за определенный год жанры которые выпускают самые успешные по продажам компании
    # какие жанры выпускают более продаваемые издатели/ как мыслят самые успешные компании и какие игры они выпускают
    df_publishers = df[df['Year'] == year][['Publisher', 'Global']].groupby('Publisher')
    ds_top_publishers = df_publishers['Global'].sum().sort_values(ascending=False).head(num)
    print("\n", ds_top_publishers)
    ds_top_genres = df[(df['Year'] == year) & (df['Publisher'].isin(ds_top_publishers.index))][['Genre']]
    ds_top_genres = ds_top_genres.sort_values('Genre', ascending=False)
    print("\n", ds_top_genres.value_counts())
    # print(ds_publishers.value_counts()) если хотим посмотреть топ издательств относительно кол-ва игр
    if plot:
        ds_top_genres.value_counts().plot(kind='bar', color='green')
        plt.title('Top Genres of ' + str(year) + ' by Top Publishers')
        plt.xlabel(None)
        plt.ylabel('Number of Games Released')
        plt.xticks(rotation=45)
        plt.tight_layout()
        FIGURE_PATH = FIGURE_FOLDER + str(year) + '_top_genres.png'
        plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()
        ds_top_publishers.plot(kind='bar', color='red')
        plt.title('Top Publishers of ' + str(year))
        plt.xlabel(None)
        plt.ylabel(str(year) + ' Sales (in millions)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        FIGURE_PATH = FIGURE_FOLDER + str(year) + '_top_publishers.png'
        plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


def total_sales_over_time_in_region(df, region, plot = True, show_plot = False):
    # Total Global Sales Over Time (Общие мировые продажи по времени)
    # → Что показывает: Общий объём продаж всех игр в мире в разбивке по месяцам или годам.
    # → Зачем: Позволяет понять общие тренды на рынке (спады, пики интереса к играм).
    # Группировка по году и суммирование продаж
    ds_global_sales_over_time = df.groupby('Year')[region].sum()
    ds_global_sales_over_time = ds_global_sales_over_time.reset_index()
    ds_global_sales_over_time['Year'] = ds_global_sales_over_time['Year'].astype(int)
    print("\n", ds_global_sales_over_time.to_string(index = False))
    if plot:
        ds_global_sales_over_time.plot(x='Year', y=region)
        FIGURE_PATH = FIGURE_FOLDER + region + '_total_sales_over_time.png'
        plt.title('Total Sales of All Games Over Time in ' + region)
        plt.xlabel(None)
        plt.ylabel('Total Sales (in millions)')
        plt.tight_layout()
        plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


def franchise_sales_over_time(df, franchise_name, region, plot = True, show_plot = False):
    # Franchise Sales Over Time (Продажи по франшизам)
    # → Что показывает: Объём продаж одной франшизы в разбивке по месяцам или годам.
    df_franchise = df[df['Game'].str.contains(franchise_name, case=False)]
    ds_franchise_sales_over_time = df_franchise.groupby('Game')[region].sum()
    ds_franchise_sales_over_time = ds_franchise_sales_over_time.reset_index().sort_values(region, ascending=False)
    print("\n", ds_franchise_sales_over_time.to_string(index = False))
    if plot:
        ds_franchise_sales_over_time.plot(x='Game', y=region, kind='bar', color='green')
        FIGURE_PATH = FIGURE_FOLDER + franchise_name + '_franchise_sales_over_time.png'
        plt.title(franchise_name + ' Franchise Sales Over Time')
        plt.xlabel(None)
        plt.ylabel(region + ' Sales (in millions)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


def average_sales_per_genre_per_region(df, region, plot = True, show_plot = False):
    # Average Sales per Genre per Region (Средние продажи игр по жанрам по регионам)
    # → Что показывает: Средний объём продаж одной игры в каждом регионе (NA, EU, JP, Other).
    # → Зачем: Помогает выявить регионы с наибольшей вовлечённостью в покупку игр.
    # Группировка по жанру и региону, вычисление среднего значения продаж
    ds_avg_sales = df.groupby('Genre')[region].mean().reset_index()
    ds_avg_sales = ds_avg_sales.sort_values(region, ascending=False)
    print("\n", ds_avg_sales.to_string(index=False))
    if plot:
        # Построение графика
        ds_avg_sales.plot(x='Genre', y=region, kind='bar', color='blue')
        plt.title('Average Sales per Genre in ' + region)
        plt.xlabel('Genre')
        plt.ylabel('Average Sales (in millions)')
        plt.tight_layout()
        FIGURE_PATH = FIGURE_FOLDER + region + '_avg_sales_per_genre.png'
        plt.savefig(FIGURE_PATH)
        if show_plot:
            plt.show()


if __name__ == '__main__':
    DATAPATH = "cypro_pyproject/dataset/PS4_GamesSales.csv"
    verbose = False
    df = import_and_clean_data(DATAPATH, verbose)
    genres_by_top_publishers(df, 2016)
    total_sales_over_time_in_region(df, 'Europe')
    franchise_sales_over_time(df, 'Call of Duty', 'Global')