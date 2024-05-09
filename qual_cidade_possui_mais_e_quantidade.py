import pandas as pd

# Carregar os DataFrames para as tabelas de carros e clientes
df_carros = pd.read_excel("auto_carros.xlsx")  
df_clientes = pd.read_excel("clientes_teste.xlsx")  

# Realizar a junção (merge) dos DataFrames usando a coluna id_client como chave de junção
df_completo = pd.merge(df_carros, df_clientes, on='id_client')

# Filtrar os carros da marca "Ford"
df_ford = df_completo[df_completo['auto_brand'] == 'Ford']

# Contar a quantidade de carros por cidade do cliente
contagem_cidades = df_ford['auto_brand'].groupby(df_ford['city']).count()

# Encontrar a cidade com mais carros da marca "Ford"
cidade_mais_carros_ford = contagem_cidades.idxmax()
quantidade_carros_ford = contagem_cidades.max()

print("A cidade com mais carros da marca Ford é:", cidade_mais_carros_ford)
print("Quantidade de carros da marca Ford na cidade:", quantidade_carros_ford)