import pandas as pd

def load_offers():
    """
    Return a data set which contais the minimium interval between trains (in seconds)
    for each line (blue, green, red and silver) by month from 2021 until 2023.

    Linha 1-Azul: blue
    Linha 2-Verde: green
    Linha 3-Vermelha: red
    Linha15-Prata: silver
    """

    # data from 2021
    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202021.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'blue',
                            'Linha 2-Verde': 'green',
                            'Linha 3-Vermelha': 'red',
                            'Linha 15-Prata ': 'silver'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df1 = data_raw.T

    df1.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    df1 = df1[1:]

    df1 = df1.reset_index()

    df1 = df1.melt('index').query('value!=0')

    df1.rename(columns={'variable': 'month', 'index': 'line', 'value': 'interval'}, inplace=True)

    df1['year'] = 2021

    # data from 2022
    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202022_6.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'blue',
                            'Linha 2-Verde': 'green',
                            'Linha 3-Vermelha': 'red',
                            'Linha 15-Prata ': 'silver'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df2 = data_raw.T

    df2.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    df2 = df2[1:]

    df2 = df2.reset_index()

    df2 = df2.melt('index').query('value!=0')

    df2.rename(columns={'variable': 'month', 'index': 'line', 'value': 'interval'}, inplace=True)

    df2['year'] = 2022

    # data from 2023
    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202023_1.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'blue',
                            'Linha 2-Verde': 'green',
                            'Linha 3-Vermelha': 'red',
                            'Linha 15-Prata ': 'silver'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df3 = data_raw.T

    df3.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    df3 = df3[1:]

    df3 = df3.reset_index()

    df3 = df3.melt('index').query('value!=0')

    df3.rename(columns={'variable': 'month', 'index': 'line', 'value': 'interval'}, inplace=True)

    df3['year'] = 2023
    
    dataset = pd.concat([df1, df2, df3])

    dataset['date'] = pd.to_datetime(dataset[['year', 'month']].assign(DAY=1))

    return (dataset[['line', 'date', 'interval']])