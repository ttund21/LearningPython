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
+ Lista de quantificadores não gulosos:

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

+ São metacaracetres representado por uma barra-invertida(\) seguida de uma letra;
+ Lista de metacaracteres barra-letra:

  |  b-l |  Equivalente POSIX  |        Significa       |
  |  --- |          ---        |           ---          |
  |  \d  |     [[:digit:]]     |  Dígito                |
  |  \D  |     [^[:digit:]]    |  Não-dígito            |
  |  \w  |     [[:alnum:]]     |  Palavra               |
  |  \W  |     [^[:alnum:]]    |  Não-palavra           |
  |  \s  |     [[:space:]]     |  Branco                |
  |  \S  |     [^[:space:]]    |  Não-branco            |
  |  \a  |     [[:alpha:]]     |  Alfabeto              |
  |  \A  |     [^[:alpha:]]    |  Não-alfabeto          |
  |  \h  |     [[:alpha:]_]    |  Cabeça de palavra     |
  |  \H  |     [^[:alpha:]_]   |  Não-cabeça de palavra |
  |  \l  |     [[:lower:]]     |  Minúsculas            |
  |  \L  |     [^[:lower:]]    |  Não-minúsculas        |
  |  \u  |     [[:upper:]]     |  Maiúsculas            |
  |  \U  |     [^[:upper:]]    |  Não-maiúsculas        |
    
