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
|      \|       |  Ou           |   Ou um ou outro                 |
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
  Frase: www.gogle.com
  ER: w*.go*gle.com[0-9]*

  Saída: www.gogle.com
  ```
+ Resumo:
  + O asterisco repete em qualquer quantidade;
  + Quantificadores são gulosos eles tentaram repetir o maior número de vezes possivel;
  + O curinga .* é o tudo e o nada, qualquer coisa.

### Mais

+ Tem o fincionamento igual ao *asterisco*, com a diferença que não é mais opcional o átomo anterior;
+ Exemplo 1:
  ```mais1
  Frase: www.gogle.com
  ER: w*.go*gle.com[0-9]+

  Saída:
  ```
+ Exemplo 2:
  ```mais2
  Frase: www.google.com
  ER: w+.go+gle.com

  Saída: www.google.com
  ```
+ Resumo:
  + O mais repete em qualquer quantidade, pelo menos uma vez;
  + O mais é igual ao asterisco, só mais exigente.

### Chaves{n, m}

+ Chaves é o quantitficador mais controlado aonde você consegue definir o número de repetições;
+ Exemplo:
  ```chaves
  Frase: www.google.com
  ER: w{3}.go{2}gle.com

  Saída: www.google.com
  ```
+ Tabela de exemplos:

|Metacaractere|               Repetições               |
|     ---     |                  ---                   |
|     {1, 3}  |    De 1 a 3                            |
|     {3,}    |    Pelo menos 3 (3 ou mais)            |
|     {0, 3}  |    Até 3                               |
|     {3}     |    Exatamente 3                        |
|     {1}     |    Exatamente 1                        |
|     {0,1}   |    Zero ou 1 (igual ao opcional)       |
|     {0,}    |    Zero ou mais (igual ao asterisco)   |
|     {1,}    |    Um ou mais (igual o mais)           |

+ Resumo:
  + Chaves são precisas;
  + Você pode especificar um número exato, um mínimo, um máximo, ou uma faixa númerica;
  + Com a chaves é possivel simular o: *, + e ?.

## Metacaracteres tipo Âncora

+ São metacaracteres usados para marcar a posição.

### Circunflexo

+ Usado no inicio de uma ER, serve para marcar o começo da linha;
+ Exemplo:
  ```circunflexo
  Frase: 123 www.google.com 456
	 789 www.bing.com 123
  ER: ^[0-9]

  Saída: 1
         7
  ```
+ Resumo:
  + Server para procurar palavras no começo da linha;
  + Só é especial no começo da ER (e de uma lista).

### Cifrão

+ Usado no final de uma ER é útil para marcar o fim de uma linha;
+ Exemplo:
  ```cifrao
  Frase: 123 www.google.com 456
	 789 www.bing.com 123
  ER: [0-9]$

  Saída: 6
         3
  ```
+ Resumo:
  + Serve para prucurar palavras no fim da linha;
  + Só é especial no fim da ER.

### Borda

+ Usada para delimitar limites de uma palavra;
+ Exemplo:
  ```borda
  Frase: bom-dia dia melodia vadia
  ER: \bdia\b

  Saída: dia dia
  ```
+ Resumo:
  + Borda marca os limites de uma palavra;
  + Útil para caçar palavras exatas.

## Outros metacaracteres

### Escape

+ Utilizado para tornar um metacaractere um caractere, ou seja, torna ele literal;
+ Exemplo:
  ```Escape
  Frase: CPF: 000.000.008-00
  ER: [0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}

  Saída: 000.000.008-00
  ```
+ Resumo:
  + O escape retira o poder do metacaractere;
  + \* = [*] = asterisco literal;
  + O escape escapa o escape, *\\*.

### Ou

+ Usado para gerar alternativas, ou isso ou aquilo;
+ Exemplo:
  ```ou
  Frase: http://www.google.com.br
         ftp://www.google.com.br
         https://www.google.com.br
  ER: ftp://|http://

  Saída: http://
         ftp://
  ```
+ Resumo:
  + O ou indica alternativas;
  + Funciona em um caractere ou em vários;
  + O grupo multiplica o poder do ou.

### Grupo

+ Utilizado para agrupar caracteres;
+ Um dos metacaracteres mais importantes, pois com ele todos os outros tem seu poder aumentado;
+ Dentro de um grupo podemos ter caracteres, metacaracteres e também outros grupos;
+ Exemplo:
  ```grupo1
  Frase: CPF: 000.000.008-00
  ER: ([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}
  
  Saída: 000.000.008-00
  ```
+ Podemos agrupar tudo que quisermos dentro de um grupo:

|     Expressão    |           Casa com            |
|        ---       |              ---              |
|      (ha!)+      |    ha!, ha!ha!, ha!ha!ha!, ...   |
|  (\.[0-9]){3}    |    0.8.9, .1.2.3, .7.7.7, ...   |
|    ---    |    ---   |
