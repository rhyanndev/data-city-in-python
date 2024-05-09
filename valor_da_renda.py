import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv")  

# Filtrar o DataFrame para incluir apenas as linhas onde o estado é "DF"
df_df = df[df['state'] == 'DF']

# Encontrar o maior salário no estado do DF
maior_salario_df = df_df['monthly_income'].max()

print("O maior salário no estado do DF é:", maior_salario_df)