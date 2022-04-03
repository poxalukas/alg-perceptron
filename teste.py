import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from perceptron import Perceptron
import matplotlib.pyplot as plt

#tratando a planilha
df = pd.read_csv('csv.csv')
df.tail()
x=df.iloc[0:4,[1,2]].values
y=df.iloc[0:4,3].values

#gerando o neuronio artificial
perceptron=Perceptron(taxa=0.1,iteracoes=30)
#gerando os pesos
perceptron.fit(x,y)


#plotando o grafico
plt.plot(perceptron.lista_pesos,marker='o')
plt.xlabel('Iteraçoes') 
plt.ylabel('Número de classificações erradas')
plt.show ()