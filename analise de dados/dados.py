import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de dados
data = {
    'Ano': [2018, 2019, 2020, 2021, 2022],
    'Vendas': [150, 200, 100, 300, 350]
}

# Cria um DataFrame
df = pd.DataFrame(data)

# Analisa os dados (neste caso, apenas imprimindo a média)
media_vendas = df['Vendas'].mean()
print(f"Média de Vendas: {media_vendas}")

# Gera um gráfico de linha
plt.plot(df['Ano'], df['Vendas'], marker='o')

# Adiciona título e rótulos
plt.title('Vendas Anuais')
plt.xlabel('Ano')
plt.ylabel('Vendas')

# Exibe o gráfico
plt.show()
