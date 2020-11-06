"""
Cynthia Rothschild
oct 29 2020
pandas project to study from
this covers reading and locating from panda daraframe and some helpful functions for
for accessing dataframe variables like culumn values and reseting index for value 
"""
#variable df in main inspired from https://realpython.com/pandas-dataframe/ under create panda dataframes
# all functions inspired from Keith Galli youtube video and github
#Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby)
#https://github.com/KeithGalli/pandas
#Data original source of data from Kaggle: https://www.kaggle.com/abcsds/pokemon
import pandas as pd
import numpy as np

def testing(df):
    print("in read program hello")

def show_col(df):
    print("name of columns")
    print(df.columns) #column is attribute
    #print specific column by column name
    print("\nSpecific column: (and show column number)")
    print("\nName:\n", df['Name'])
    print("\nName [2-5) :\n",  df['Name'][2:5]) #specific range inorder
    print("\nLegendary:\n", df['Legendary'])

    print("\n\nshow 'Name', 'HP', 'Legendary' for items at index [9-13)")
    col_items = ['Name', 'HP', 'Legendary']
    print(df[col_items][9:13])

def show_table(df):
    print("will show first 4 rows/show rows [0 - 3] rows")
    print(df.head(4))
    print("\nwill show last 3 rows/show last [n-2, n] rows")
    print(df.tail(3))

def index_locate(df):
    print("will show item/row at an index")
    row_at_index = df.iloc[0]
    print("row at index 0\n", row_at_index)
    row_at_index = df.iloc[2:5]
    print("\nrow at index's [2-5)\n", row_at_index)

    print("\niloc, row at index 797\n", df.iloc[797])
    print("\nelement at 3rd column \""+df.columns[3]+"\", at index 797 is: \""+df.iloc[797,3]+"\"")
    print("df.iloc[797,3]")

def show_all_row_info(df):
    """
    itterate each row in dataframe
    For each row can access its element at row/column for entire df
    access (values in cells) by the name of the columns.
    """
    print("all elements for each row, limits show only 3 rows\n")
    quit_count = 0
    for index, row in df.iterrows():
        if quit_count > 2:
            break
        print(index, row)
        print("<3"*15)
        quit_count +=1
        
    quit_c = 0
    print("\nfor each row shows specific element\n")
    for index, row in df.iterrows():
        if quit_c > 4:
            break

        #choose column: "Defense", "Attack", "Type 1"
        col_name = "Type 1"
        print("Index :",col_name+",\tfor Name")
        print(index,"    :", row[col_name]+",\t",row["Name"])
        
        quit_c +=1

def locate_by_value(df):
    col_type1 = df["Type 1"]
    print("show all rows where column Type 1 is Fire")
    print(df.loc[col_type1 == "Fire"])

    print("\nshow all rows where column Defense is greater than 120")
    print(df.loc[df["Defense"] > 120])

def locate_by_value2(df):
    print("show all poison bugs")
    print(df.loc[(df['Type 1']=="Bug") & (df['Type 2'] == "Poison")])
    # OR |              ... | (df["HP"] > 90)

          
def describe_stat_and_sort(df):
    print("data describe shows a quick statical informational overview")
    print(df.describe())
    print("\nshows items/rows sorted by their names ascending order")
    print(df.sort_values("Name"))
    print("\nshows items/rows sorted by their names in descending order [Z-A]")
    print(df.sort_values("Name", ascending=False))
    print("\nshows items/rows sorted by their HP then Defense")
    print("\tMost strong and denfensive Pokemon, with largest HP and Defense")
    print(df.sort_values(['HP', 'Defense'], ascending = False))

    print("\nshows items/rows sorted by their Type 1 then most HP")
    print("\tPokemon, show for each of 'type 1' starting with most HP")
    print(df.sort_values(['Type 1', 'HP'], ascending = [True, False]))
    #                                               OR [1,0]

"""
Helpful functions
"""

def get_col_list(df):
    return list(df.columns.values)

def reset_index_(df):
    print("reset index, updates index to remove old index and set with new index starting first row at 0")
    new_df = df.reset_index()#(drop=True, ..) will drop column holding old index
    #can do save new df in place (inplace=True, ..) rather than copy over or reassign
    return new_df
 

def main():
    data = {'Name': ["sally",'john', 'marty', 'baker', 'cam'], 'HP': ['yellow', 'blue','yellow','green','yellow']}
    row_lables = [101, 102, 103, 104, 105]
    df = pd.DataFrame(data=data, index=row_lables)
    #from https://realpython.com/pandas-dataframe/ under create panda dataframes
    show_table(df)
    print("here")
    testing(df)

if __name__ == '__main__':
    main()

