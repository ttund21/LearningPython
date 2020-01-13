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


