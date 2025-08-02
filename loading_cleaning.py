#импортировали нужные библиотеки
import numpy as np
import pandas as pd
import shutil
import os

def setup_pandas():
    #настроили пандас для полного отображения таблиц
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

def backup_csv(PATH, verb=False):
    # backup the file
    if verb:
        print("Backing up file...")
    PATHBakup = PATH.replace('.csv', '_backup.csv')
    shutil.copy(PATH, PATHBakup)
    if verb and os.path.exists(PATHBakup):
        print("Backup created:", PATHBakup)

def import_csv(PATH):
    #сделали датафрейм, прочитав csv
    df = pd.read_csv(PATH)
    print(df.head())
    return df

def print_summary(df):
    #отобразили сводную инфу датафрейма
    df.info()
    df.describe()

def delete_missing_values(df, verb=False):
    nan_count = df.isna().sum().sum()
    if verb:
        #смотрим сколько NaN значений в колонках
        print("Missing values:")
        print(nan_count)
    if nan_count >> 0:
        if verb:
            print("There are missing values! Deleting...")
        #удаляем NaN
        df = df.dropna()
    else:
        if verb:
            print("No missing values")
    return df

def fix_datatypes(df, verb=False):
    if verb:
        print("Datatypes:")
        # Check datatypes
        print(df.dtypes)
        # Show column names
        print(df.columns)
        #Columns: 'Game', 'Year', 'Genre', 'Publisher', 'North America', 'Europe', 'Japan', 'Rest of World', 'Global'
        print(df.head())
    # Fix datatypes
    df['Game'] = df['Game'].astype('string')
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df['Genre'] = df['Genre'].astype('string')
    df['Publisher'] = df['Publisher'].astype('string')
    df['North America'] = df['North America'].astype(float)
    df['Europe'] = df['Europe'].astype(float)
    df['Japan'] = df['Japan'].astype(float)
    df['Rest of World'] = df['Rest of World'].astype(float)
    df['Global'] = df['Global'].astype(float)
    if verb:
        print("Datatypes after fix:")
        print(df.dtypes)
        print(df.head())
    return df

def remove_duplicates(df, verb=False):
    number_of_duplicates = df.duplicated().sum()
    if verb:
        print("Duplicates:")
        print(df.duplicated().sum())
    if number_of_duplicates > 0:
        if verb:
            print("There are duplicates! Removing...")
        df = df.drop_duplicates()
        if verb:
            print("Duplicates after removal:")
            print(df.duplicated().sum())

    else:
        if verb:
            print("No duplicates")
    return df

def ask_to_export_csv(dataframe, PATH, verb=False):
    #ask user if he wants to export
    PATH = PATH.replace('.csv', '_cleaned.csv')
    userInput = input("Export cleaned data to csv for further use? (y/n): ")   
    if userInput == 'y' or userInput == 'Y' or userInput == 'yes' or userInput == 'Yes' or userInput == 'YES':
        print("Exporting...")
        dataframe.to_csv(PATH, index=False)
        if verb:
            print("Exported to", PATH)    
    else:
        print("OK. Not exporting")

#хз какие функции пока что понадобятся, пока не обозначили отдельные задачи по анализу

def import_and_clean_data(DATA_PATH, verb=False):
    setup_pandas()
    backup_csv(DATA_PATH, verb)
    df = import_csv(DATA_PATH)
    if verb:
        print_summary(df)
    df = delete_missing_values(df, verb)
    df = fix_datatypes(df, verb)
    df = remove_duplicates(df, verb)
    ask_to_export_csv(df, DATA_PATH, verb)
    return df

if __name__ == "__main__":
    verbose = True
    import_and_clean_data("cypro_pyproject/dataset/PS4_GamesSales.csv", verbose)
