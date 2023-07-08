import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um array NumPy com dados aleatórios
data = np.random.randn(100)

# Criando um dataframe do Pandas a partir dos dados do NumPy
df = pd.DataFrame(data, columns=['Valor'])

# Plotando um histograma usando o Seaborn e o Matplotlib
sns.histplot(data=df, x='Valor', kde=True)

# Adicionando um título ao gráfico usando o Matplotlib
plt.title('Histograma')

# Exibindo o gráfico
plt.show()
