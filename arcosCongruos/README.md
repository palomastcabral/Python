## Arcos Côngruos

Estudando o círculo trigonométrico, decidi criar um algoritmo em Python para encontrar arcos côngruos (que possuem mesmo ponto de partida e de chegada). Quis fazer isso porque:

1) eu gosto muito de utilizar a programação para aplicar o que eu estudo

2) fazer isso me permite entender mais a fundo o mecanismo de determinados cálculos

3) estou estudando Python, então quero criar programas nessa linguagem para praticar

-----------------------------

Exemplo sobre o que é a MDP:

980º = 2 voltas completas no círculo trigonométrico (2 * 360º) + 260º

Então, a MDP = 260º

-----------------------------

Em uma divisão negativa, eu acreditava que a diferença seria apenas que o quociente e o resto seriam negativos. Porém:

-980/360 = 100 (??)

Não deveria ser resto = -260º? Depois eu faria o cálculo da diferença entre 360º e |-260º| e descobriria o valor correto da MPD, que realmente é 100°. Mas esse resultado surgia antes mesmo desse cálculo.

-----------------------------

Decidi alterar todo o programa para linguagem C. Compilei e executei pelo Replit. Mas o resultado não foi 100, e sim um resto negativo (-260). Ainda no Replit, o Python manteve um resto positivo (100).

Além disso, pesquisei o resultado dessa divisão negativa no aplicativo MathWay, onde o resto dessa divisão negativa foi = 0 (o que não faz sentido nem agora que compreendi toda a situação).

-----------------------------

Até que pesquisei sobre a Divisão Euclidiana. Segundo a definição, o resto de uma divisão deve ser maior ou igual a zero (e menor que o divisor).

Para isso, em vez de:
-980/360 ter quociente = -2 e resto = -260,

Posso calcular:
-980/360 com quociente = -3 (valor que, em módulo, é imediatamente superior ao quociente utilizado anteriormente).

Assim:
-980/360 = -3, com resto 100.

E é por isso que o resultado do algoritmo em Python gerava esse valor (100), porque o interpretador da linguagem já estava impedindo o resto de obter valor zero.

-----------------------------

Após entender isso, e como eu queria criar todo o algoritmo simulando o mecanismo matemático (de forma que eu conseguisse demonstrar como são os cálculos de uma MDP quando um ângulo é negativo), fiz os cálculos mantendo sempre o ângulo positivo. Assim, o interpretador não faria os cálculos por mim.

Por fim, tornei o ângulo negativo novamente.

-----------------------------
