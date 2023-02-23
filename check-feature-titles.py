#Import libraries
import pandas as pd


def check_title(dir_df):
    
    df = pd.read_csv(dir_df)
    titles = df ['Feature Title'].value_counts()
    title_list = []

    #Append formatted titles to empty title list
    for i in range(len(titles)):
        title_list.append(str(titles.index[i]) + ' -> ' +str(titles[i]) + '/n')

    title_list.sort()

    return title_list