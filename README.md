# cypro_pyproject
Final Project for Python Module of Data Analytics Course at CyberPro Israel
## Collaborators:
Ilia Oleinikov

Svetlana Saveleva

## Key Features:
- CLI-wrapped programm for analyzing sales data
- Multi-functional nested CLI menu with mutable verbose mode
- Dataset backup 
- Data loading and cleaning
- Cleaned data export
- Data visualization
- Export plots as PNGs
- ASCII art

## Project Goals:
- Create a data-agnostic user-friendly CLI-based programm, that allows sales data analization, providing insights into market trends and patterns

## Project Description
The project contains several Python files that work in tandem to create the programm. Each file can fuction separatly to do its designated task:
### `cli.py`
The `cli.py` file provides CLI-based user-friendly intarface that incapsulates all of the program's functions. 

It also contains a dictionary of commands that can be run from anywhere within the menus. This file is the main file of the programm.
### `loading_cleaning.py`
The `loading_cleaning.py` file contains the functions that load, backup, clean and export cleaned data.

The main function of this file is `import_and_clean_data` that has the following parameters:
- `DATA_filepath`: The file path to the input data file.
- `verboseMode`: A boolean flag to enable or disable verbose mode, which controls the level of output and logging.
- `backup`: A boolean flag to enable or disable data backup, which creates a copy of the original data file.
- `fix_dtypes`: A boolean flag to enable or disable data type fixing, which attempts to correct data type errors in the input data.
- `del_miss_val`: A boolean flag to enable or disable deletion of missing values, which removes rows or columns with missing data.
- `fill_miss_val`: A boolean flag to enable or disable filling of missing values, which replaces missing data with a specified value.
- `rem_dupl`: A boolean flag to enable or disable removal of duplicates, which removes duplicate rows from the input data.
- `export_clean`: A boolean flag to enable or disable export of cleaned data, which saves the cleaned data to a new file.

### `analysis_plotting.py`


### Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib

### Used External Libraries
- Pandas
- NumPy
- Matplotlib

## Dataset Description
[placeholder]

## How to use
[placeholder]
