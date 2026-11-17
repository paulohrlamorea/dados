import pandas as pd

# Carregar a base de continuação
df = pd.read_csv('/data/ecommerce_ex2.csv')

# 1 - Trate os campos 'Marca', 'Material' e 'Temporada' para os valores serem em minúsculo
df['Marca'] = df['Marca'].str.lower()
df['Material'] = df['Material'].str.lower()
df['Temporada'] = df['Temporada'].str.lower()

# 2 - Remover linhas duplicadas para garantir integridade
df = df.drop_duplicates()

# 3 - Remover linhas com menos de 8 valores não nulos (utilizando o parâmetro thresh)
df = df.dropna(thresh=8)