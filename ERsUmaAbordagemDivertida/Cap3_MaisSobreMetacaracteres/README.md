# Capítulo 3: Mais Sobre Metacaracteres

## Quantificadores gulosos vs não-gulosos

+ Como já visto anteriormente quantificadores tentam casar com maior número possivel de átomos;
+ Um exemplo:
  ```gulosos
  Frase: <title> Gulosos <\title>
  ER: <.*>

  Saída: <title> Gulosos <\title>
  ```
+ Observe que a ER "<.\*>" vai casar do primeiro menor que até o último maior que da frase, e se quisermos apenas as tags?;
+ Daí surge os quantificadores não gulosos que vão casar apenas o necessário para finalizar a ER;
+ Exemplo:
  ```naoGulosos
  Frase: <title> Gulosos <\title>
  ER: <.*?>

  Saída: <title><\title>
  ```
+ Veja que o "não-guloso" casou apenas com o necessário;
+ Lista de quantifecadores não gulosos:

  | Metacaractere  |        Nome          |
  |       ---      |         ---          |
  |       ??       | Opcional não-guloso  |
  |       \*?      | Asterisco não-guloso |
  |       +?       | Mais não-guloso      |
  |      {n, m}    | Chaves não-gulosas   |

+ Observe o padrão de interrogação no final de cada quantificador, é isso que define um não-guloso;
+ Comparações entre os dois:
  + Gulosos:

    | Gulosos |  ---  |
    |   ---   |  ---  |
    | ab*     | abbbb |
    | ab+     | abbbb |
    | ab?     | ab    |
    | ab{1,3} | abbbb |

  + Não-gulosos:

    | Não-gulosos |  ---  |
    |     ---     |  ---  |
    |  ab*?       |   a   |
    |  ab+?       |   ab  |
    |  ab??       |   a   |
    |  ab{1,3}?   |   ab  |

## Metacaracteres tipo barra-letra
    
