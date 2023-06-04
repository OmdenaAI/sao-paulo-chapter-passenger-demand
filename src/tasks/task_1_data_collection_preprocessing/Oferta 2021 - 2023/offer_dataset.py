import pandas as pd

def load_offers():
    """
    Return a data set which contais the minimium interval between trains (in seconds)
    for each line (blue, green, red and silver) by month from 2021 until 2023.
    """
    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202021.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'azul',
                            'Linha 2-Verde': 'verde',
                            'Linha 3-Vermelha': 'vermelha',
                            'Linha 15-Prata ': 'prata'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df1 = data_raw.set_index('month').T.rename_axis('station').reset_index().rename_axis(None, axis=1)

    df1['year'] = 2021

    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202022_6.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'azul',
                            'Linha 2-Verde': 'verde',
                            'Linha 3-Vermelha': 'vermelha',
                            'Linha 15-Prata ': 'prata'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df2 = data_raw.set_index('month').T.rename_axis('station').reset_index().rename_axis(None, axis=1)

    df2['year'] = 2022

    path = 'https://transparencia.metrosp.com.br/sites/default/files/Oferta%20-%202023_1.csv'

    data_raw = pd.read_csv(path,
                        encoding='latin_1',
                        sep=';',
                        #thousands='.',
                        skiprows=4,
                        nrows=12
                        )

    data_raw.rename(columns = {'Mês': 'month',
                            'Linha 1-Azul ': 'azul',
                            'Linha 2-Verde': 'verde',
                            'Linha 3-Vermelha': 'vermelha',
                            'Linha 15-Prata ': 'prata'}, inplace=True)

    data_raw['month'] = data_raw['month'].str.replace('*', '')

    df3 = data_raw.set_index('month').T.rename_axis('station').reset_index().rename_axis(None, axis=1)

    df3['year'] = 2023

    return (pd.concat([df1, df2, df3]))