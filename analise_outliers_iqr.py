import pandas as pd

# Carregar base para tratamento estatístico
df = pd.read_csv('/data/ecommerce_ex3.csv')

# 1 - Calcular o intervalo interquartil (IQR) para a métrica de avaliações
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# 2 - Definir o limite superior para identificar outliers estatísticos
limite_alto = q3 + 1.5 * iqr

# 3 - Filtrar os produtos que possuem um número de avaliações acima do limite superior
df_avaliados = df[df['N_Avaliacoes'] > limite_alto]
