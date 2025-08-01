#импортировали нужные библиотеки
import numpy as np
import pandas as pd


def setup_pandas():
    #настроили пандас для полного отображения таблиц
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)


def import_csv():
    #сделали датафрейм, прочитав csv
    df = pd.read_csv('cypro_pyproject/dataset/PS4_GamesSales.csv')
    print(df.head())
    return df


def print_summary(df):
    #отобразили сводную инфу датафрейма
    df.info()
    print(df.isna().sum())
    print(df.describe())

#хз какие функции пока что понадобятся, пока не обозначили отдельные задачи по анализу

def import_and_clean_data():
    setup_pandas()
    df = import_csv()
    print_summary(df)
    #смотрим сколько нан значений в колонках, где мы поняли что они есть
    print(df[df['Year'].isna() & df['Publisher'].isna()])
    return df


if __name__ == "__main__":
    import_and_clean_data()
