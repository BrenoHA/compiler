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


def error_translation(df, estado, classe):
    n_error = int(df[classe][estado].replace('e', ''))
    row_error = df.iloc[n_error]
    available = (value for value in row_error if value != df[classe][estado])
    available_list = list(available)
    print("==> ERRO SINTATICO Linha: {} Coluna: {} => recebeu: {}, disponiveis no estado {}: {}".format(
        estado, classe, classe, available_list[0], available_list[1:]))

def holub(pstack,tokens):
    while len(tokens) > 0:
        npstack = pstack.copy()
        while len(npstack) > 0:
            if (action(npstack[-1],tokens[0]) != error):
                return(npstack,tokens)
            npstack.pop()
        del tokens[0]
    return None

