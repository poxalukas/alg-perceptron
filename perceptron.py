# perceptron.py 
import numpy as np 
import random

class Perceptron(object): 
   def __init__(self, taxa = 0.1, iteracoes = 10): 
      self.taxa = taxa 
      self.iteracoes = iteracoes 

   def fit(self, x, y):
      self.auxiliar=(1+x.shape[1])
      self.peso = [] #cria um vetor de tamanho x+1 para os pesos
      for i in range((self.auxiliar)):
         self.peso.append(random.randint(0,1))

      print(("Valor inicial dos pesos:",self.peso))
      self.lista_pesos = []  #vetor de erros acumulados

      for i in range(self.iteracoes):
         erro = 0
         for xi, xj in zip(x, y):
            delta_w = self.taxa * (xj - self.predict(xi)) 
            self.peso[1:] += delta_w * xi
            self.peso[0] += delta_w
            if(delta_w!= 0):
               erro += int(delta_w != 0.0)
               print("imput esperado ",xj," imput obtido:",self.peso[0])
         self.lista_pesos.append(erro)
      print(("Valor final dos pesos:",self.peso))
      return self

   def predict(self, X):
      return np.where(self.imput(X) >= 0.0, 1, 0)

   def imput(self, X):
      return np.dot(X, self.peso[1:]) + self.peso[0]