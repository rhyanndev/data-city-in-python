import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv") 

# Criar uma lista com os estados desejados
estados = ['SP', 'RJ', 'MG', 'ES', 'DF']

# Iterar sobre cada estado e encontrar o menor salário
for estado in estados:
    # Filtrar o DataFrame para incluir apenas as linhas onde o estado é o atual na iteração
    df_estado = df[df['state'] == estado]
    
    # Encontrar o menor salário no estado atual
    menor_salario_estado = df_estado['monthly_income'].min()
    
    print(f"O menor salário no estado de {estado} é: {menor_salario_estado}")