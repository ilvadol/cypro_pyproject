import pandas as pd
from cleaning import import_and_clean_data


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

#

if __name__ == '__main__':
    df = import_and_clean_data()
    print_genres_by_top_publishers(df, 2016, 5)
