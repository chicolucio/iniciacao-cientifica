# Ambientes virtuais e unidades

A partir de agora iremos usar alguns pacotes que não fazem parte da instalação
padrão do Anaconda. É uma boa prática evitar instalar novos pacotes diretamente
no ambiente base, então criaremos um ambiente virtual com pacotes que nos serão
úteis.

- Veja [este vídeo](https://youtu.be/8laFJI2l3gU) sobre ambientes virtuais,
especialmente o trecho que fala sobre o `conda`, o gerenciador presente no
Anaconda;
- crie um ambiente virtual chamado `chemistry` e instale o interpretador Python
e os seguintes pacotes nesse ambiente:
  - NumPy
  - SciPy
  - MatPlotLib
  - Pandas
  - pint
  - chempy
  - mendeleev
  - molmass
  - sympy
- busque na internet a documentação de cada pacote para saber como instalar e
entenda seu papel
- veja [este artigo](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/) 
para ver como deixar o ambiente visível para uso em um Jupyter Notebook
- para unidades usaremos o pacote `pint`. Veja [este vídeo](https://www.youtube.com/watch?v=FDxivogkYbY) 
e o artigo na descrição do mesmo para entender o uso do pacote. Busque, também,
a documentação do pacote na internet.
- abra o script `van_der_waals.py` e o respectivo arquivo de testes:
  - veja se consegue reconhecer que a função resolve a equação de van der Waals
  em sua forma cúbica
  - com a ajuda da documentação do `pint` e dos testes, identifique o papel do
  *decorator* `wraps`
    - com o visto na documentação, entenda o porquê do uso de
    `GAS_CONSTANT.magnitude` dentro do corpo da função e não da constante
    diretamente
  - busque a documentação do `Polynomial` do NumPy utilizado e entenda a parte
  final da função, que retorna a raiz real
  - rode os testes e veja que estão passando. Modifique as tolerâncias e veja o
  que muda no resultado dos testes.

## Exercícios

- documente a função `van_der_waals`
- com o *wraps* do `pint` force a função criada por você na aula 2 para o
cálculo de velocidade média a trabalhar no SI
- faça o mesmo para a função de lançamento de vertical fornecida em aulas
anteriores
- crie uma função, e seus respectivos testes, para o cálculo do volume molar de
um gás ideal. Force que ela funcione no SI
