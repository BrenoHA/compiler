import csv
import pandas as pd
df_action = pd.read_csv('./public/action.csv')  
df_goto = pd.read_csv('./public/goto.csv')  

def fill_errors(df):
    for index, state in enumerate(df['State']):
        df[df['State']==index] = df[df['State']==index].fillna('e'+str(state))
    print(df)

fill_errors(df_action)
