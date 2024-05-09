import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv")

# Encontrar a linha com o maior salário
linha_maior_salario = df.loc[df['monthly_income'].idxmax()]

# Extrair o estado da linha com o maior salário
estado_maior_salario = linha_maior_salario['state']

print("O estado onde a pessoa com o maior salário está localizada é:", estado_maior_salario)