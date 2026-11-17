import pandas as pd

# Carregar base com colunas mistas e strings complexas
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# 1 - Criar a coluna 'Condicao_Atual': Extrai a primeira parte antes do separador "|"
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip() if pd.notnull(x) and '|' in str(x) else str(x).strip())

# 2 - Criar a coluna 'Qtd_Vendidos': Extrai o valor numérico após o "|", removendo a palavra "vendidos"
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split('|')[1].strip().split(' ')[0] if pd.notnull(x) and '|' in str(x) and len(x.split('|')) > 1 else 'Nenhum')

# 3 - Converter a coluna 'Desconto' para string para permitir manipulação de texto
df['Desconto'] = df['Desconto'].astype(str)

# 4 - Modificar a coluna 'Desconto' para remover o símbolo '%' e manter apenas o valor numérico
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0].strip() if pd.notnull(x) and '%' in str(x) else x)