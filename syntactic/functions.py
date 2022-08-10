import csv
import pandas as pd
df_action = pd.read_csv('./public/action.csv') 
df_goto = pd.read_csv('./public/goto.csv')  

def fill_errors(df):
    for index, state in enumerate(df['State']):
        df[df['State']==index] = df[df['State']==index].fillna('e'+str(state))

def goto(estado,lexema):
    fill_errors(df_goto)
    return df_goto[lexema][estado]

def action(lexema,estado):
    fill_errors(df_action)
    return df_action[lexema][estado]

