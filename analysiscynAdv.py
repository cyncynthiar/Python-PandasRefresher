"""
Cynthia Rothschild
oct 29 2020
pandas project to study from
filtering text, conditional, and stats
"""
#variable df in main inspired from https://realpython.com/pandas-dataframe/ under create panda dataframes
# all functions inspired from Keith Galli youtube video and github
#Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby)
#https://github.com/KeithGalli/pandas
import pandas as pd
import numpy as np
import re

def filtering_txt1(df):
    """
    get all rows containing "Mega" in name column
    uses str.contains
    uses df.loc
    var is df to be filtered through
    return new df
    """

    return df.loc[  df['Name'].str.contains('Mega')  ]


def filtering_txt2(df):
    """
    get all rows NOT containing "Mega" in name column
    uses str.contains
    uses df.loc
    uses ~ as not
    var is df to be filtered through
    return new df
    """
    return df.loc[ ~ df['Name'].str.contains('Mega')  ]

def filtering_txt3(df):
    """
    get all rows type 1 is fire or grass
    uses str.contains
    uses regex true in str.contains
    uses df.loc
    var is df to be filtered through
    return new df
    """
    return df.loc[  df['Type 1'].str.contains('Fire|Grass', regex=True)  ]


def filtering_test_flagEqual(df):
    """
    panda equals and str.contains(..flags=re.I)
    pandas equals, (pd.DataFrame).equals(other_df)
    the == has trouble with NaN 
    pandas data frame, checking that the df's are equal when sifted/sorted
    by type 1 = grass or fire. but seeing how the 
    """
    df1 = df.loc[  df['Type 1'].str.contains('Fire|Grass', regex=True)  ]
    df2 = df.loc[  df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
    print("df1.equals(df2)")
    print(df1.equals(df2))
    print("df1 == df2")
    print(df1 == df2)
    #return df1 == df2


def explain_regex(df):
    """
    """
    #[A-Z] range of string special characters
    # ^ start of line
    # * wild cards
    print("df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]")
    print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
    return


def condition_change_df(df):
    """
    if condition met than assign existing columns
    condition "total" > 500 then generation column => ''
    and lengandary column => "YAY"
    
    """
    
    print("df.loc[df['Total'] > 500, ['Generation', 'Legendary']]   = ['Ultimum','YAY']")
    df.loc[df['Total'] > 500, ['Generation', 'Legendary']]   = ['Ultimum','YAY']

    return


"""
Stats
"""

def aggregate_stat_groupby(df):
    """
    shows which type 1 group has on average/mean the highest defense
    also shows the groups averages/mean for every other column
    """
    df_stat = df.groupby(['Type 1']).mean().sort_values("Defense", ascending=False)
    #       = df.groupby(['Type 1']).sum()
    
    #grouped by 'Type 1', this finds the mean of each column for the items grouped by type 1 col
    #sorted for display by highest defense 
    return df_stat


def count_groupby1(df):
    """
    """
    #create a count column that way we value each pokemon as 1 and can count how many
    #pokemon per catigory or how many pokemon have the same value for the type 1 columnn
    df['count'] = 1

    df_count = df.groupby(['Type 1']).count()
    return df_count

def count_groupby2(df):
    """
    """
    #create a count column that way we value each pokemon as 1 and can count how many
    #pokemon per catigory or how many pokemon have the same value for the type 1 columnn
    df['count'] = 1

    #shows count of type 1 and subsets of type 2 columns
    return df.groupby(['Type 1', 'Type 2']).count()


"""
large data
"""

def read_by_size(df_str,num_col):
    """
    reads and can do stats or other work on small amount of data at a time
    incase entire data frame is larger than memory/space aloted
    """
    #? results instaciate or declare before loop?
    new_df = pd.DataFrame(columns=df.columns)

    for df in pd.read_csv(df_str, chunksize=num_col):
        results = df.groupby(['Type 1']).count()
        new_df = pd.concat([new_df, results]) #appends items to new_df



def main():
    pass
if __name__ == '__main__':
    main()


