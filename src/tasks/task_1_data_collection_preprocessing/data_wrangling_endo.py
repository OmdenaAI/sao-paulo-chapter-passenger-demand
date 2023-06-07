import pandas as pd
from datetime import datetime


#Setting up the file
original_dataset='Entrada de Passageiros por Linha - 2022_7.csv'

# Setup the year
year = 2022

# Function to Convert feature type to datetime, with chosen year 
def to_datetime(x, year):
    month_numeric = month_map[x]
    return datetime(year, month_numeric, 1)

#Extraction by station

df_azul = pd.read_csv('Entrada de Passageiros por Linha - 2022_7.csv',
                      encoding='latin_1',
                      sep=';',
                      thousands='.',
                      skiprows=5,
                      skipfooter=44,
                      usecols=[0,1,2,3,4,5],
                      engine='python')
df_azul['estacao'] = 'azul'
df_azul.rename(columns={'Mês':'month', 'Total':'total', 'estacao':'station'}, inplace=True)
df_azul['month'] = df_azul['month'].str.rstrip('*')
df_azul['month'] = df_azul['month'].str.lower()

# Mapping the months to its numeric equivalent
month_map = {
    'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,
    'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8,
    'set': 9, 'out': 10, 'nov': 11, 'dez': 12
}

# Update the feature
df_azul['month'] = df_azul['month'].apply(lambda x: to_datetime(x, year))


#SAME FOR GREEN LINE

df_verde = pd.read_csv(original_dataset,
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=5,
                       skipfooter=44,
                       usecols=[7,8,9,10,11,12],
                       engine='python')
df_verde['station'] = 'verde'
df_verde.rename(columns={'Mês.1':'month', 'Total.1':'total', 'MDU.1':'MDU', 'MSA.1':'MSA', 'MDO.1':'MDO', 'MAX.1':'MAX', 'estacao':'station'}, inplace=True)
df_verde['month'] = df_verde['month'].str.rstrip('*')
df_verde['month'] = df_verde['month'].str.lower()
df_verde['month'] = df_verde['month'].apply(lambda x: to_datetime(x, year))

#SAME FOR SILVER LINE

df_prata = pd.read_csv('Entrada de Passageiros por Linha - 2022_7.csv',
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=24,
                       skipfooter=25,
                       usecols=[7,8,9,10,11,12],
                       engine='python')
df_prata['estacao'] = 'prata'
df_prata.rename(columns={'Mês.1':'month', 'Total.1':'total', 'MDU.1':'MDU', 'MSA.1':'MSA', 'MDO.1':'MDO', 'MAX.1':'MAX', 'estacao':'station'}, inplace=True)
df_prata['month'] = df_prata['month'].str.rstrip('*')
df_prata['month'] = df_prata['month'].str.lower()
df_prata['month'] = df_prata['month'].apply(lambda x: to_datetime(x, year))


#SAME FOR RED LINE

df_vermelha = pd.read_csv('Entrada de Passageiros por Linha - 2022_7.csv',
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=24,
                       skipfooter=25,
                       usecols=[0,1,2,3,4,5],
                       engine='python')
df_vermelha['estacao'] = 'vermelha'
df_vermelha.rename(columns={'Mês':'month', 'Total':'total', 'MDU':'MDU', 'MSA':'MSA', 'MDO':'MDO', 'MAX':'MAX', 'estacao':'station'}, inplace=True)
df_vermelha['month'] = df_vermelha['month'].str.rstrip('*')
df_vermelha['month'] = df_vermelha['month'].str.lower()
df_vermelha['month'] = df_vermelha['month'].apply(lambda x: to_datetime(x, year))

df = pd.concat([df_vermelha,df_azul,df_prata,df_verde],ignore_index=True)

df.to_csv(f'passenger_entrance_{year}.csv')