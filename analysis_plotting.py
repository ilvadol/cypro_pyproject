import pandas as pd
from loading_cleaning import import_and_clean_data


def print_genres_by_top_publishers(df, year, num = 5):
    # найти топ n издательств по продажам за определенный год
    # показать число игр, опубликованных топовыми издательствами, по жанрам за тот же год
    # эта функция показывыет на основе данных за определенный год жанры которые выпускают самые успешные по продажам компании
    # какие жанры выпускают более продаваемые издатели/ как мыслят самые успешные компании и какие игры они выпускают
    df_publishers = df[df['Year'] == year][['Publisher', 'Global']].groupby('Publisher')
    ds_top_publishers = df_publishers['Global'].sum().sort_values(ascending=False).head(num)
    print("\n", ds_top_publishers)
    ds_top_genres = df[(df['Year'] == year) & (df['Publisher'].isin(ds_top_publishers.index))][['Genre']]
    print("\n", ds_top_genres.value_counts())
    # print(ds_publishers.value_counts()) если хотим посмотреть топ издательств относительно кол-ва игр


def print_total_sales_over_time_in_region(df, region):
    # Total Global Sales Over Time (Общие мировые продажи по времени)
    # → Что показывает: Общий объём продаж всех игр в мире в разбивке по месяцам или годам.
    # → Зачем: Позволяет понять общие тренды на рынке (спады, пики интереса к играм).
    # Группировка по году и суммирование продаж
    ds_global_sales_over_time = df.groupby('Year')[region].sum()
    ds_global_sales_over_time = ds_global_sales_over_time.reset_index()
    ds_global_sales_over_time['Year'] = ds_global_sales_over_time['Year'].astype(int)
    print("\n", ds_global_sales_over_time.to_string(index = False))


# Average Sales per Genre per Region (Средние продажи игр по жанрам по регионам)
# → Что показывает: Средний объём продаж одной игры в каждом регионе (NA, EU, JP, Other).
# → Зачем: Помогает выявить регионы с наибольшей вовлечённостью в покупку игр.



if __name__ == '__main__':
    DATAPATH = "cypro_pyproject/dataset/PS4_GamesSales.csv"
    verbose = False
    df = import_and_clean_data(DATAPATH, verbose)
    # print_genres_by_top_publishers(df, 2016)
    print_total_sales_over_time_in_region(df, 'Europe')