import pandas as pd

#Setting up the file
original_dataset='src/tasks/task_1_data_collection_preprocessing/Entrada de Passageiros por Linha - 2022_7.csv'

#Extraction by station

df_azul = pd.read_csv(original_dataset,
                      encoding='latin_1',
                      sep=';',
                      thousands='.',
                      skiprows=5,
                      skipfooter=44,
                      usecols=[0,1,2,3,4,5],
                      engine='python')
df_azul['station'] = 'azul'
df_azul.rename(columns={'Mês':'month', 'Total':'total'}, inplace=True)


df_verde = pd.read_csv(original_dataset,
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=5,
                       skipfooter=44,
                       usecols=[7,8,9,10,11,12],
                       engine='python')
df_verde['station'] = 'verde'
df_verde.rename(columns={'Mês.1':'month', 'Total.1':'total', 'MDU.1':'MDU', 'MSA.1':'MSA', 'MDO.1':'MDO', 'MAX.1':'MAX'}, inplace=True)

df_prata = pd.read_csv(original_dataset,
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=24,
                       skipfooter=25,
                       usecols=[7,8,9,10,11,12],
                       engine='python')
df_prata['station'] = 'prata'
df_prata.rename(columns={'Mês.1':'month', 'Total.1':'total', 'MDU.1':'MDU', 'MSA.1':'MSA', 'MDO.1':'MDO', 'MAX.1':'MAX'}, inplace=True)

df_vermelha = pd.read_csv(original_dataset,
                       encoding='latin_1',
                       sep=';',
                       thousands='.',
                       skiprows=24,
                       skipfooter=25,
                       usecols=[0,1,2,3,4,5],
                       engine='python')
df_vermelha['station'] = 'vermelha'
df_vermelha.rename(columns={'Mês':'month', 'Total':'total'}, inplace=True)

df = pd.concat([df_vermelha,df_azul,df_prata,df_verde],ignore_index=True)

print(df)