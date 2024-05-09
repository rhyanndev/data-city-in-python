import pandas as pd

# Carregar o arquivo CSV para um DataFrame
df = pd.read_csv("clientes.csv")  

# Contar o número total de clientes
total_clientes = len(df)

# Contar o número de clientes com mais de 60 anos
clientes_acima_de_60 = len(df[df['age'] > 60])

# Calcular o percentual de clientes com mais de 60 anos
percentual_acima_de_60 = (clientes_acima_de_60 / total_clientes) * 100

# Exibir o resultado com duas casas decimais
print("Percentual de clientes acima de 60 anos:", "{:.2f}".format(percentual_acima_de_60), "%")
