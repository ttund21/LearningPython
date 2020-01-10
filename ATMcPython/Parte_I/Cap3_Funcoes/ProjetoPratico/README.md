# Projetos práticos

Para exercitar, escreva programas que executem as tarefas a seguir.


## Sequência de Collatz

+ Crie uma função chamada collatz() que tenha um parâmetro de nome number.
Se number for par, collatz() deverá exibir number // 2 e retornar esse valor. Se
number for ímpar, collatz() deverá exibir e retornar 3 * number + 1.

+ Em seguida, crie um programa que permita que o usuário digite um inteiro e
fique chamando collatz() com esse número até a função retornar o valor 1.
(De modo bastante surpreendente, essa sequência, na realidade, funciona para
qualquer inteiro – cedo ou tarde, ao usar essa sequência, você chegará em 1!
Até mesmo os matemáticos não têm muita certeza do motivo. Seu programa
está explorando o que chamamos de sequência de Collatz, às vezes chamada
de “o mais simples problema matemático impossível”.)

+ Lembre-se de converter o valor de retorno de input() em um inteiro usando
a função int(); caso contrário, o valor será do tipo string.

+ Dica: um number inteiro será par se number % 2 == 0 e ímpar se number %
2 == 1.
+ A saída desse programa poderá ter uma aparência semelhante a:
  ```saida
  Enter number:
  3
  10
  5
  16
  8
  4
  2
  1
  ```

## Validação de dados de entrada
+ Acrescente instruções try e except no projeto anterior para detectar se o
usuário digitou uma string que não corresponda a um inteiro.
+  Normalmente, a função int() gerará um erro ValueError se receber uma string que não seja um
inteiro, como em int('puppy').
+ Na cláusula except, exiba uma mensagem ao usuário informando-lhe que um inteiro deve ser fornecido.
