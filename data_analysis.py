import os
import pandas as pd
import matplotlib.pyplot as plt

# Acessar o caminho para os dados utilizando a variável de ambiente DATA_PATH
data_path = os.environ.get('DATA_PATH') 
print(data_path)
# Lê o arquivo CSV
dados = pd.read_csv("dados.csv")

# Cria o gráfico de barras
plt.bar(dados["nome"], dados["pontuacao"])
plt.xlabel("Nomes")
plt.ylabel("Pontuações")
plt.title("Pontuações dos Alunos")
plt.xticks(rotation=45)
plt.tight_layout()

# Exibe o gráfico
plt.show()