# alg-perceptron
Implementaçao do algorimto de neuronios virtuais em python,perceptron, que foi sugerido pelo professor Celso da UFG

foi implementado um algoritmo simples com duas funçoes: 
  teste
  perceptron

onde a de teste, busca na nossa base de dados, no caso o csv.csv(sem imaginaçao), e tratamos essa base com panda do py onde passamos a variavel x os valores da coluna 2 e 3 da nossa base e a y o valor esperado que o nosso neuronio retorne apos verificar os pesos

criamos a classe do Perceptron e recebemos por parâmetro a taxa de aprendizado e o número de iterações (épocas).
Agora, vamos aos métodos dessa classe:
O primeiro e mais importante é o método que servirá para treinar a classe, o fit, que recebe como parâmetro o conjunto de dados, chamado de dataset, com os inputs no parâmetro X e os rótulos do dataset no y:

Aqui primeiramente iniciamos os pesos como um vetor de valores aleatorio entre 0 e 1 e criamos a lista de erros. Depois abrimos o laço que vai repetir o treinamento para todas as épocas. Dentro dele iniciamos uma variável erro ao valor 0 e percorremos o dataset usando o método zip para juntar os inputs ao rótulo, a cada iteração pegamos os inputs na variável xi e o rótulo na variável xj.
Calculamos o delta, que é chama o método predict e ele recebe como parâmetro um vetor de inputs:

Esse método é simples, ele apenas chama o net_input para calcular o produto entre os pesos e os inputs, e com esse resultado usa a função where da biblioteca NumPy para retornar 1 caso seja maior ou igual a 0 e -1 caso não seja.
Por último temos o método net_input, que recebe como parâmetro um vetor de entradas:

Esse método retorna o produto escalar entre o vetor de entradas xi e o vetor de pesos somado com o bias.

Entao apos uma sequencia de epocas, treinamos nosso perceptron para poder dizer, quem é compositor e quem é um cientista.Apos treinarmos nosso neuronio, plotamos um grafico mostrando a quantidade de erros pelas epocas.

Questoes:
1.O programa de treinamento funciona sempre
ou depende da seqüência de valores
informados durante o treinamento?
O programa depende dos valores informados e dos valores dos pesos aleatorios, podendo ocorrer de nao conseguir identificar quem é quem e nao conseguir distinguir cientista de compositor

2.Qual o número máximo de interações para
corrigir os pesos?
Depende dos valores de peso, da lista passada, da ordenaçao da lista, em media 10 geraçoes sao suficientes pra esse exercicio proposto, porem pode acontecer de ser em uma geraçao(caso de pesos perfeitos) ou de nao corrigir em nenhum momento(caso de erros do perceptron)
