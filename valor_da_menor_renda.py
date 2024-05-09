import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv")  

# Filtrar o DataFrame para incluir apenas as linhas onde o estado é "DF"
df_df = df[df['state'] == 'DF']

# Encontrar o menor salário no estado do DF
menor_salario_df = df_df['monthly_income'].min()

print("O menor salário no estado do DF é:", menor_salario_df)
