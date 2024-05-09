import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv")  

# Criar uma lista com os estados desejados
estados = ['SP', 'RJ', 'MG', 'ES', 'DF']

# Iterar sobre cada estado e encontrar o maior salário
for estado in estados:
    # Filtrar o DataFrame para incluir apenas as linhas onde o estado é o atual na iteração
    df_estado = df[df['state'] == estado]
    
    # Encontrar o maior salário no estado atual
    maior_salario_estado = df_estado['monthly_income'].max()
    
    print(f"O maior salário no estado de {estado} é: {maior_salario_estado}")
