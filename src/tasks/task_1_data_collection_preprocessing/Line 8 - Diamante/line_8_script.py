import pandas as pd
import tabula

# Dictionary of month and corresponding PDF URLs
dict_path_files = {
      '2023-Apr': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20230512141555847-Demanda%20de%20Passageiros%20L8%20-%20esta%C3%A7%C3%B5es%20-%20Abril%202023.pdf',
      '2023-Mar': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20230512141355316-Demanda%20de%20Passageiros%20L8%20-%20esta%C3%A7%C3%B5es%20-%20%20Mar%C3%A7o%202023.pdf',
      '2023-Feb': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20230323092307897-Demanda%20de%20Passageiros%20-%20Linha%208%20-%20Janeiro%202023_esta%C3%A7%C3%B5es.pdf',
      '2023-Jan': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20230323092450356-Demanda%20de%20Passageiros%20-%20Linha%208%20-%20Fevereiro%202023_esta%C3%A7%C3%B5es.pdf',
      '2022-Dec': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20230116095111837-Demanda%20de%20Passageiros%20-%20L8%20-%20Esta%C3%A7%C3%B5es%20-%20Dezembro%202022.pdf',
      '2022-Nov': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20221213155906943-Passageiros%20transportados%20VM8_esta%C3%A7%C3%B5es.pdf',
      '2022-Oct': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20221110174951505-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Sep': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20221014111009916-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Aug': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220922174230998-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Jul': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220818104522479-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Jun': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220708165344223-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-May': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220624102431046-Demanda%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Apr': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220511105750767-Entrada%20de%20passageiros%20por%20esta%C3%A7%C3%A3o.pdf',
      '2022-Mar': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220404182602960-2%20-%20Demanda%20de%20Passageiros%20-%20L8%20esta%C3%A7%C3%B5es.pdf',
      '2022-Feb': 'https://www.viamobilidade.com.br/assets/viamobilidade/ccr-viamobilidade/public/media/page/passengers/files/20220404182202270-2%20-%20Demanda%20de%20Passageiros%20-%20L8%20esta%C3%A7%C3%B5es.pdf'
}

# Create an initial DataFrame with column headers
df = pd.DataFrame.from_dict({'Estação': [None, 'Amador Bueno', 'Ambuitá', 'Santa Rita', 'Itapevi',
                                        'Engenheiro Cardoso', 'Sagrado Coração', 'Jandira',
                                        'Jardim Silveira', 'Jardim Belval', 'Barueri', 'Antonio João',
                                        'Santa Terezinha', 'Carapicuíba', 'General Miguel Costa',
                                        'Quitaúna', 'Comandante Sampaio', 'Osasco', 'Presidente Altino',
                                        'Imperatriz Leopoldina', 'Domingos de Morais', 'Lapa',
                                        'Barra Funda', 'Julio Prestes', 'TOTAL']})


# Iterate through the dictionary of URLs and extract data from each PDF
for month, path_file in dict_path_files.items():
    # Read the PDF file and extract data from the first page
    df_temp = tabula.read_pdf(path_file, pages=1)

    # Merge the extracted data with the existing DataFrame based on the 'Estação' column
    df = pd.merge(df, df_temp[0], how='right', on='Estação')

    # Rename the column corresponding to the month value
    df.rename(columns={'Linha 8 - Diamante': month}, inplace=True)

# Rename the 'Estação' column to 'Station'
df.rename(columns={'Estação':'Station'}, inplace=True)

# Remove the first row (contains None values) and reset the index
df = df.drop([0]).reset_index(drop=True)

# Save the final DataFrame as a CSV file
df.to_csv('line_8_diamante.csv', encoding='utf-8')
