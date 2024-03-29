import pandas as pd
import re
df_action = pd.read_csv('./public/action.csv')
df_goto = pd.read_csv('./public/goto.csv')


def fill_errors(df):
    for index, state in enumerate(df['State']):
        df[df['State'] == index] = df[df['State']
                                      == index].fillna('e'+str(state))
        df.to_csv(r'./public/goto_1.csv', index=False)


def goto(estado, classe):
    return int(df_goto[classe][estado])


def action(estado, classe):
    available_classes = list(df_action.columns)
    available_states = list(df_action['State'])
    if (estado in available_states and classe in available_classes):
        return df_action[classe][estado]
        # value = df_action[classe][estado]
        # evaluate = re.sub(r'[0-9]+', '', value)
        # if(evaluate != 'e'):
        #     return df_action[classe][estado]
        # else:
        #     error_translation(df_action, estado, classe)
        #     return df_action[classe][estado]
    else:
        print("Posição [{},{}] inexistente na tabela Action".format(
            estado, classe))
