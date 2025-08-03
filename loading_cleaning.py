# Imported necessary libraries
import numpy as np
import pandas as pd
import shutil
import os

def setup_pandas():
    # Configured pandas for full display of tables
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

def backup_csv(filepath, verboseMode=False):
    # Backup the file
    if verboseMode:
        print("Backing up file...")
    filepathBackup = filepath.replace('.csv', '_backup.csv')
    if os.path.exists(filepathBackup):
        if verboseMode:
            print("Backup already exists:", filepathBackup)
        return
    shutil.copy(filepath, filepathBackup)
    if verboseMode and os.path.exists(filepathBackup):
        print("Backup created:", filepathBackup)

def import_csv(filepath, verboseMode=False):
    # Created dataFrame by reading CSV
    dataFrame = pd.read_csv(filepath)
    if verboseMode:
        print("Imported data:")
        print(dataFrame.head())
    return dataFrame

def print_summary(dataFrame):
    # Displayed summary information of the dataFrame
    print("Summary information:")
    print(dataFrame.head())
    print(dataFrame.tail())
    print(dataFrame.info())
    print(dataFrame.describe())

def delete_missing_values(dataFrame, verboseMode=False):
    nan_count = dataFrame.isna().sum().sum()
    if verboseMode:
        # Checked the number of NaN values in columns
        print("Missing values:")
        print(dataFrame.isna().sum())
        # Checked the total number of NaN values
        print("Total missing values:")
        print(nan_count)
    if nan_count > 0:
        if verboseMode:
            print("There are missing values! Deleting...")
        # Removed NaN
        dataFrame = dataFrame.dropna()
    else:
        if verboseMode:
            print("No missing values")
    return dataFrame

def fill_missing_values(dataFrame, verboseMode=False):
    nan_count = dataFrame.isna().sum().sum()
    if verboseMode:
        # Checked the number of NaN values in columns
        print("Missing values:")
        print(dataFrame.isna().sum())
        # Checked the total number of NaN values
        print("Total missing values:")
        print(nan_count)
    if nan_count > 0:
        if verboseMode:
            print("There are missing values! Filling...")
        # Removed NaN
        dataFrame = dataFrame.fillna('')
    else:
        if verboseMode:
            print("No missing values")
    return dataFrame 

def fix_datatypes(dataFrame, verboseMode=False):
    if verboseMode:
        print("Datatypes:")
        # Check datatypes
        print(dataFrame.dtypes)
        # Show column names
        print(dataFrame.columns)
        # Columns: 'Game', 'Year', 'Genre', 'Publisher', 'North America', 'Europe', 'Japan', 'Rest of World', 'Global'
        print(dataFrame.head())
    # Fix datatypes
    dataFrame['Game'] = dataFrame['Game'].astype('string')
    dataFrame['Year'] = dataFrame['Year'].astype(int)
    dataFrame['Genre'] = dataFrame['Genre'].astype('string')
    dataFrame['Publisher'] = dataFrame['Publisher'].astype('string')
    dataFrame['North America'] = dataFrame['North America'].astype(float)
    dataFrame['Europe'] = dataFrame['Europe'].astype(float)
    dataFrame['Japan'] = dataFrame['Japan'].astype(float)
    dataFrame['Rest of World'] = dataFrame['Rest of World'].astype(float)
    dataFrame['Global'] = dataFrame['Global'].astype(float)
    if verboseMode:
        print("Datatypes after fix:")
        print(dataFrame.dtypes)
        print(dataFrame.head())
    return dataFrame

def remove_duplicates(dataFrame, verboseMode=False):
    number_of_duplicates = dataFrame.duplicated().sum()
    if verboseMode:
        print("Duplicates:")
        print(dataFrame.duplicated().sum())
    if number_of_duplicates > 0:
        if verboseMode:
            print("There are duplicates! Removing...")
        dataFrame = dataFrame.drop_duplicates()
        if verboseMode:
            print("Duplicates after removal:")
            print(dataFrame.duplicated().sum())
    else:
        if verboseMode:
            print("No duplicates")
    return dataFrame

def ask_to_export_csv(dataFrame, filepath, verboseMode=False):
    # Ask user if they want to export
    filepathClean = filepath.replace('.csv', '_cleaned.csv')
    if os.path.exists(filepathClean):
        if verboseMode:
            print("Cleaned data already exists:", filepathClean)
        return
    userInput = input("Export cleaned data to csv for further use? (y/n): ")   
    if userInput == 'y' or userInput == 'Y' or userInput == 'yes' or userInput == 'Yes' or userInput == 'YES':
        print("Exporting...")
        dataFrame.to_csv(filepathClean, index=False)
        if verboseMode:
            print("Exported to", filepathClean)    
    else:
        print("OK. Not exporting")

def import_and_clean_data(DATA_filepath, verboseMode=False, backup=True, fix_dtypes=False, del_miss_val=False, fill_miss_val=False, rem_dupl=True, export_clean=False):
    setup_pandas()
    if backup:
        backup_csv(DATA_filepath, verboseMode)
    dataFrame = import_csv(DATA_filepath)
    if verboseMode:
        print("Imported data to clean:")
        print_summary(dataFrame)
    if fix_dtypes:
        dataFrame = fix_datatypes(dataFrame, verboseMode)
    if del_miss_val:
        dataFrame = delete_missing_values(dataFrame, verboseMode)
    if fill_miss_val:
        dataFrame = fill_missing_values(dataFrame, verboseMode)
    if rem_dupl:
        dataFrame = remove_duplicates(dataFrame, verboseMode)
    if export_clean:
        ask_to_export_csv(dataFrame, DATA_filepath, verboseMode)
    if verboseMode:
        print("Cleaned data:")
        print_summary(dataFrame)
    return dataFrame

if __name__ == "__main__":
    verbose = True
    DATA = "cypro_pyproject/dataset/PS4_GamesSales.csv"
    import_and_clean_data(DATA, verbose)