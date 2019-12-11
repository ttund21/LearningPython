# FUNÇÕES

## Anotações:

+ Função é como se fosse um miniprograma dentro de um programa;
+ Blocos de códigos que podemos reutilizar;
+ Umas das melhores práticas é evitar sempre a duplicação de códigos;
+ Exemplo sem o uso de função:
  ```exemplosemfuncao
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  ```
+ Exemplo usando função:
  ```exemplocomfuncao
  def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello There.')
    
  hello()
  hello()
  hello()
  ```

### Instruções def com parâmetros

