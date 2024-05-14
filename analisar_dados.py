import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do Excel
df = pd.read_csv(f'historico_nvdc34_05_23_05_24.csv')

# Converter a coluna 'DATA' para o tipo datetime
df["DATA"] = pd.to_datetime(df["DATA"], format='%d/%m/%Y')
df['FECHAMENTO'] = pd.to_numeric(df['FECHAMENTO'].str.replace(',', '.'))
df['ABERTURA'] = pd.to_numeric(df['ABERTURA'].str.replace(',', '.'))

# Filtrar os dados para o período entre 02/05/2023 e 30/04/2024
mask = (df['DATA'] >= '2024-03-30') & (df['DATA'] <= '2024-04-30')
df_periodo = df.loc[mask]

# Gráfico da variação do preço de fechamento
plt.figure(figsize=(14,7))
plt.plot(df_periodo['DATA'], df_periodo['FECHAMENTO'], label='Preço de Fechamento')
# plt.ylim(df_periodo['FECHAMENTO'].min, df_periodo['FECHAMENTO'].max)
plt.title('Variação do Preço de Fechamento das Ações')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()
plt.show()

# Gráfico da variação do preço de abertura
plt.figure(figsize=(14,7))
plt.plot(df_periodo['DATA'], df_periodo['ABERTURA'], label='Preço de Abertura', color='orange')
plt.title('Variação do Preço de Abertura das Ações')
plt.xlabel('Data')
plt.ylabel('Preço de Abertura')
plt.legend()
plt.show()

