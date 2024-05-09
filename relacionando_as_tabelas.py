import pandas as pd

# Carregar os DataFrames para as tabelas de carros e clientes
df_carros = pd.read_csv("auto.csv", sep='\t')  
df_clientes = pd.read_excel("clientes_teste.xlsx") 

# Realizar a junção (merge) dos DataFrames usando a coluna id_cliente como chave de junção
df_completo = pd.merge(df_carros, df_clientes, on='id_client')

# Exibir o DataFrame resultante
print(df_completo)