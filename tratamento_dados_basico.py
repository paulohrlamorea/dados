import pandas as pd

# Carregar o arquivo de e-commerce da base
df = pd.read_csv('/data/ecommerce.csv')

# 1 - Verifique a quantidade de linhas e colunas e armazene na variável 'linhas_colunas'
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# 2 - Verifique os tipos de dados de todo o dataframe e armazene na variável 'tipos'
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# 3 - Verifique a quantidade de valores nulos e armazene na variável 'nulos'
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

# 4 - Substitua, no mesmo dataframe, os valores nulos das colunas 'Temporada' e 'Marca' por 'Não Definido'
df['Temporada'] = df['Temporada'].fillna('Não Definido')
df['Marca'] = df['Marca'].fillna('Não Definido')