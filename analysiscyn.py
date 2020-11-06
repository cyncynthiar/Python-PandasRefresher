"""
Cynthia Rothschild
oct 29 2020
pandas project to study from
Read and Display data
"""
# all functions inspired from Keith Galli youtube video and github
#Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby)
#https://github.com/KeithGalli/pandas
#Data original source of data from Kaggle: https://www.kaggle.com/abcsds/pokemon

import time
import pandas as pd
import numpy  as np
import analysiscynRead as readF
import analysiscynAdv  as advF

def setCSV():
    df = pd.read_csv('pokemon_data.csv')
    return df

def set_xlsx():
    df_x = pd.read_excel('pokemon_data.xlsx')
    return df_x

def set_txt():
    df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
    return df_txt

def new_sum_col_1(df,print_):
    if print_:
        print("creates a new column 'total pt', which will be the sum of columns: HP, Attack...")
        print("the new column's objective is help rank pokemnon by strength")
    df["total pt"] = df["HP"] + df["Attack"] + df["Defense"] +df["Sp. Atk"] + df['Sp. Def'] + df['Speed']
    if print_:
        print(df.head(4))
        print(df.iloc[0]) #did summation on different program from data show (aka from first row to double check total
    #could also build a for loop and check these column sum against last column and throw error or flag

def new_sum_col_2(df, print_):
    if print_:
        print("creates a new column 'total', which will be the sum of columns: HP, Attack...")
        print("the new column's objective is help rank pokemnon by strength, uses iloc")
    df['Total'] = df.iloc[:,4:10].sum(axis=1)
    #       [all rows 0:n, columns [4:10) ]     axis=0 means vertically VS axis=1 sums column of row/item
    if print_:
        print(df.head(3))

def drop_col(df, print_):
    if print_:
        print("will remove column 'total pt'")
    df = df.drop(columns=["total pt"])
    if print_:
        print(df.tail(2)) 
    return df

def reorder_by_rating(df):
    return df[["Name", "HP", "total"]]

def reorder(df):
    #move total column to 4th position 
    col = list(df.columns.values)
    df = df[col[0:4] + [col[-1]] + col[4:-1]]
    return df

def write_csv(df):
    df.to_csv('modified_pokemon.csv', index = False, sep="\t")
    #df.to_excel("modified_pokemon.csv", index = false, sep="\t")
    #        will not keep the first column called index in file created when created df

def main():
    
    df_csv = setCSV()
    
    #df_xlsx = set_xlsx()
    #df_txt = set_txt()
    
    """
    readF.testing(df_csv)
    
    #readF.show_col(df_csv)
    #print()
    #readF.show_table(df_csv) #head() tail()
    
    print("iloc method:")
    readF.index_locate(df_csv) #iloc[] index
    
    #print("iterrow in for loop, itterates over df by row allows access by column name")
    #readF.show_all_row_info(df_csv) #for loop, iterrow()

    #print(" locate all rows with desired values in selected columns")
    #readF.locate_by_value(df_csv) #loc[bool]

    readF.describe_stat_and_sort(df_csv) #describe(), sort_values() "col name" or ["col1", col2", ..]
    """
    """
    new_sum_col_1(df_csv, 0) #create new column total pt
    print()
    new_sum_col_2(df_csv, 0)
    print()
    df_csv = drop_col(df_csv, 0) #takes away column total pt, via drop(... = []) and makes copy

    df_rate = reorder_by_rating(df_csv)
    print("reordered dataframe and shows limited columns")
    print(df_rate)

    df_reorder = reorder(df_csv)
    print("reordered dataframe and moved total col forward")
    print(df_reorder)
    #write_csv(df_reorder) #writes new df to file "modified_pokemon.csv"

    readF.locate_by_value2(df_csv)
    """

    """
    #print(advF.filtering_txt3(df_csv))

    #print(advF.filtering_test_flagEqual(df_csv))
    #advF.explain_regex(df_csv)

    new_sum_col_2(df_csv, 0) #creates 'Total' column
    advF.condition_change_df(df_csv)
    print(df_csv)
    #df_csv changed in place from function and in this domain has kept change
    #now for each 'Total' column > 500,
    #then its 'Generation' and 'Legnedary' columns changed to "ultimun" and "YAY" respectively
    
    """
    #stats

    #print("the mean stats of each column based off of groups formed(grouped by) by Type 1 column")
    #print(advF.aggregate_stat_groupby(df_csv))
    #print(df_csv)


    #print(advF.count_groupby1(df_csv)['count'])
    print()
    #print(advF.count_groupby2(df_csv)['count'])

    advF.read_by_size('modified_pokemon.csv',5)
    
    print("\n+here v5; ------ ", time.ctime())
    

    
if __name__ == '__main__':
    main()
