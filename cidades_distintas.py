import pandas as pd

# Carregar o DataFrame dos clientes
df_clientes = pd.read_excel("clientes_teste.xlsx")

# Filtrar os clientes que são do estado do Rio Grande do Sul (RS)
clientes_rs = df_clientes[df_clientes['state'] == 'RS']

# Extrair as cidades dos clientes do RS
cidades_rs = clientes_rs['city']

# Identificar as cidades distintas
cidades_distintas_rs = cidades_rs.unique()

# Contar o número total de cidades distintas
total_cidades_distintas_rs = len(cidades_distintas_rs)

# Listar as cidades distintas
print("Total de cidades distintas entre os clientes do RS:", total_cidades_distintas_rs)
print("Cidades distintas entre os clientes do RS:")
for cidade in cidades_distintas_rs:
    print(cidade)