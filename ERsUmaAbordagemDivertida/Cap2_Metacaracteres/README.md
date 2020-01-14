# Capítulo 2: Metacaracteres

## Metacaracteres

+ Nomes dos Metacaracteres:

|Metacaractere|      Nome        |Metacaractere|      Nome         |
|    ---      |      ---         |    ---      |       ---         |
|     .       |     Ponto        |     ^       |    Circunflexo    |
|     []      |     Lista        |     $       |    Cifrão         |
|     [^]     |     Lista negada |     \b      |    Borda          |
|     ?       |     Opcional     |     \       |    Escape         |
|     *       |     Asterisco    |     |       |    Ou             |
|     +       |     Mais         |     ()      |    Grupo          |
|     {}      |     Chaves       |     \1      |    Retrovisor     |

### Funções

#### Representantes

| Metacaractere |  Nome         |          Função                  |
|      ---      |  ---          |           ---                    |
|       .       |  Ponto        |   Um caractere qualquer          |
|      [...]    |  Lista        |   Lista de caracteres            |
|      [^...]   |  Lista Negada |   Lista de caracteres proibidos  |

#### Quantificadores

| Metacaractere |  Nome         |          Função                  |
|      ---      |  ---          |           ---                    |
|       ?       |  Opcional     |   Zero ou um                     |
|       *       |  Asterisco    |   Zero, um ou mais               |
|       +       |  Mais         |   Um ou mais                     |
|     {n,m}     |  Chaves       |   De n até m                     |

#### Âncoras

| Metacaractere |  Nome         |          Função                  |
|      ---      |  ---          |           ---                    |
|       ^       |  Circunflexo  |   Início da linha                |
|       $       |  Cifrão       |   Final da linha                 |
|      \b       |  Borda        |   Início ou fim de palavra       |

#### Outros

| Metacaractere |  Nome         |          Função                  |
|      ---      |  ---          |           ---                    |
|       \c      |  Escape       |   Torna literal o caractere c    |
|       |       |  Ou           |   Ou um ou outro                 |
|     (...)     |  Grupo        |   Delimita um grupo              |
|     \1...\9   |  Retrovisor   |   Texto casado nos grupos 1..9   |

+ Lembrando que curingas de linha de comando e ERs são diferentes.

## Metacaracteres tipo Representante

+ São metacaracteres que tem o objetivo representar um ou mais caracteres;

#### Ponto

+ O ponto é o metacaractere que representa um caractere qualquer, ou seja, podemos usar ele para procurar aquela palavra que a gente esqueceu, mas lembramos como ela se parece;
+ Exemplo:
  ```ponto
  Frase: War Never Changes
  ER: ...er
  
  Saída: Never
  ```
+ Resumo:
  + O ponto dar match com qualquer caractere;
  + O ponto é um curinga para dar match com um caractere;
  + O ponto dar match com ponto.

### Lista

+ Diferente do ponto, a lista só vai dar match com os caracteres selecionados dentro dela, exemplo:
  ```lista
  Frase: Maior que a tristeza de não haver vencido é a vergonha de nao ter lutado!
  ER: n[ãa]o
  
  Saída: não, nao
  ```

#### Intervalo em listas

+ Dentro de uma lista quase todos os caracteres são normais;
+ Com exceção do ' - ' hifen que representa em uma lista um intervalo;
+ Exemplo:
  ```listaIntervalo
  Frase: Maior que a tristeza de não haver vencido é a vergonha de nao ter lutado! 23:08.
  ER: [0-2][0-9]:[0-5][0-9]

  Saída: 23:08
  ```
+ No exemplo acima foi criado uma ER que dita o formato de hora(24), então se escreve **[0-9]** é como se fosse **[0123456789]**;
+ Esses intervalos funciona com diversos tipos de caracteres letras(a-z ou A-Z), números(0-9), simbolos(:-@) e etc;
+ Para referenciar o **-** é so colocar ele no final da lista **[a-z-]**;
+ Para referenciar um colchete basta colocalos na ordem inversa **[][]**;
+ A ordem dos intervalos respeita a **tabela ASCII**.

#### Dominando caracteres acentuados (POSIX)

+ POSIX é um padrão internacional que define regras de intervalo;
+ Ele é divido em classes:

| Classe POSIX  |    Similar    |          Significa               |
|      ---      |      ---      |           ---                    |
|   [:upper:]   | [A-Z]         |   Letras maiúsculas              |
|   [:lower:]   | [a-z]         |   Letras minúsculas              |
|   [:alpha:]   | [A-Za-z]      |   Maiúsculas/minúsculas          |
|   [:alnum:]   | [A-Za-z0-9]   |   Letras e números               |
|   [:digit:]   | [0-9]         |   Números                        |
|   [:xdigit:]  | [0-9A-Fa-f]   |   Números hexadecimais           |
|   [:punct:]   | [.,!?:...]    |   Sinais de pontuação            |
|   [:blank:]   | [ \t]         |   Espaço e Tabulação             |
|   [:space:]   | [ \t\n\r\f\v] |   Caracteres brancos             |
|   [:cntrl:]   |               |   Caracteres de controle         |
|   [:graph:]   | [^ \t\n\r\f\v |   Números                        |
|   [:print:]   | [^\t\n\r\f\v] |   Números hexadecimais           |

+ Note que os colchetes fazem parte do POSIX, então para incluir ele numa lista ficaria *[[:lower:]]*, lembrando que *[:lower:]* POSIX puro, [[:lower:]] POSIX dentro de uma lista;
+ Exemplo:
  ```telephone
  Frase: Telefone de teste 3258-8795
  ER: [[:digit:]-]

  Saída: 3258-8795
  ```
+ Resumo:
  + Lista dar Match em quem ela conhece;
  + Dentro da lista qualquer caractere é normal com exceção do hifen;
  + Dentro da lista hifen é intervalo;
  + Um hifen literal tem que ser o último da lista;
  + Um ] literal tem que ser o primeiro da lista;
  + Os intervalos respeitam a tabela ASCII.

### Lista negada

+ Tudo que se aplica na lista, se aplica na lista negada;
+ Diferente da lista, lista negada dará Match com os caracteres diferentes do que está dentro dela;
+ Lista negada consiste em **[^0-9]**, parecido com a lista, só que após o colchete inicial vem um circunflexo;
+ Para ignorar o **^** basta colocar ele em qualquer posição que não seja a primeira;
+ Exemplo:
  ```listaNegada
  Frase: 1234 lamplight PO box 9x ^
  ER: [^[:digit:]^]

  Saída: lamplight PO box 
  ```
+ Resumo:
  + Lista negada segue as regras de uma lista normal;
  + Um ^ literal não pode ser o primeiro da lista;
  + Classes POSIX também podem ser negadas.

## Metacarecteres tipo Quantificador

+ São metacaracteres que ditão a quantidade de repetição que o caractere anterior pode ter.

### Opcional

+ O metacaractere Opcional dita que se tiver tal caractere aceite e se não tiver também aceite;
+ Exemplo:
  ```opcional
  Frase: anda
  ER: anda[rs]?

  Saída: anda
  ```
#### Como ler uma ER

+ Primeiro lê-se uma ER da esquerda para direita, *átomo(caractere)* por átomo;
+ Segundo analisa-se as possibilidades;
+ No exemplo **fala[r!]** primeiro se lê f > a > l > a, depois analisa-se as possibildades, ou falar ou fala!.

+ Resumo:
  + O opcional é opcional;
  + Útil para procurar variações de palavras;
  + Podemos tornar opicional caracteres e metacaracteres;
  + Leia a ER átomo por átomo da esquerda para direita;
  + Leia a ER, entenda e analise as possibilidades.

### Asterisco

+ Um parecido com o opcional com a diferença que ele pode ter, não ter ou ter vários;
+ Exemplo:
  ```asterisco
  Frase: site www.google.cooooom
  ER: w*.go*gle.co*m

  Saída: www.google.cooooom
  ```
+ Resumo:
  + O asterisco repete em qualquer quantidade;
  + Quantificadores são gulosos eles tentaram repetir o maior número de vezes possivel;
  + O curinga .* é o tudo e o nada, qualquer coisa.

### Mais

+
