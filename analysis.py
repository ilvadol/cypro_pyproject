import pandas as pd
from loading_cleaning import import_and_clean_data, fix_datatypes


def print_genres_by_top_publishers(df, year, n):
    # найти топ n издательств по продажам за определенный год
    # показать число игр, опубликованных топовыми издательствами, по жанрам за тот же год
    # эта функция показывыет на основе данных за определенный год жанры которые выпускают самые успешные по продажам компании
    # какие жанры выпускают более продаваемые издатели/ как мыслят самые успешные компании и какие игры они выпускают
    df_publishers = df[df['Year'] == year][['Publisher', 'Global']].groupby('Publisher')
    ds_top_n = df_publishers['Global'].sum().sort_values(ascending=False).head(n)
    print(ds_top_n)
    df_games = df[(df['Year'] == year) & (df['Publisher'].isin(ds_top_n.index))][['Genre']]
    print(df_games)
    print(df_games.value_counts())
    # print(ds_publishers.value_counts()) если хотим посмотреть топ издательств относительно кол-ва игр

# Total Global Sales Over Time (Общие мировые продажи по времени)
# → Что показывает: Общий объём продаж всех игр в мире в разбивке по месяцам или годам.
# → Зачем: Позволяет понять общие тренды на рынке (спады, пики интереса к играм).

# def print_top_sales_by_year(df):
#     df_years = pd.to_numeric(df['Year'], errors='coerce').dropna()
#     print(df_years)
#     # Группировка по году и суммирование продаж
#     global_sales_by_year = df.groupby('Year')['Global'].sum().sort_index()
#     print(global_sales_by_year)

if __name__ == '__main__':
    DATAPATH = "cypro_pyproject/dataset/PS4_GamesSales.csv"
    verbose = True
    df = import_and_clean_data(DATAPATH, verbose)
    print_genres_by_top_publishers(df, 2016, 5)