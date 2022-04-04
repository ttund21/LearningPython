# Operadores Regex

**.** - Dar match em qualquer caractere;

**^** - Sinaliza para dar match em qualquer que começar com, ex: "^s";

**\$** - Sinaliza para dar match em qualquer que terminar com, ex: "s\$";

**[]** - Cria uma lista de caracteres aceitos, ex: [t,p,l];

**[0-9]** - Números de 1 a 9;

**[a-z]** - Letras minuscula de a - z;

**[A-Z]** - Letras maiuscula de A - Z;

**[a-zA-Z]** - Letras minuscula e maiuscula de a - z;

**[^]** - Da macth se não houver os caracteres da lista ex: [^a-zA-Z];

**\*** - significa "ZERO ou mais repetições da coisa anterior", a "coisa anterior" pode ser um único caractere, uma classe ou um grupo de caracteres entre parênteses;

**\+** - parecido com o '*' mas a lógica é "UMA ou mais repetições da coisa anterior";

**\?** - "ZERO ou UMA repetição da coisa anterior";

**{}** - Entre x a y de repetições de algo, ex: (spam){1,3}\$.

**()** - Agrupa caracteres como se fosse um só, para ser usado com outros metacaracteres;

**|** - Significa "ou", ex: gr(a|e)y;

**\1** até \99 - Invoca o grupo pelo número, ex: ^(quero)(-| )\1$;

**\d** - Dar match com digitos ou seja [0-9];

**\s** - Dar match com espaços em branco [ \t\n\r\f\v];

**\w** - Dar macth em letras maiuscula e minuscula, digitos e underscore, [a-zA-Z0-9_];

**\D** - Faz o contrário [^0-9];

**\S** - Faz o contrário [^ \t\n\r\f\v];

**\W** - Faz o contrário [^a-zA-Z0-9_];

**\A** - Afirma a posição no início da string;

**\Z** - Afirma a posição no final da string;

**\b** - A sequência \b corresponde à string vazia entre os caracteres \w e \W;

**\B** - A sequência \B corresponde à string vazia em qualquer outro lugar;

