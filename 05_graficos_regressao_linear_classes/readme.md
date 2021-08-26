# Gráficos, regressão linear e classes

Vamos agora aprender a obter dados a partir de arquivos para criar gráficos. No
processo, vamos aprender ainda como fazer uma regressão linear e como criar
classes em Python.

- veja o capítulo 6 do livro do Pine para uma noção sobre gráficos
- veja [esse artigo](https://cienciaprogramada.com.br/2020/09/graficos-python-pint-matplotlib/) 
para entender a integração do `pint` com o `matplotlib`
- veja [essa playlist](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) sobre classes
- agora, abra e rode o arquivo `main.py` na pasta `massa_molar_gas_ideal`
    - veja se consegue entender como se obtém a massa molar do gás a partir de
    dados de pressão e de densidade
    - procure a documentação de métodos de pacotes que foram utilizados e busque
    entender o que fazem
    - qual o papel das funções no arquivo `helpers.py`?
    - compare agora com o código disponível no arquivo `main_with_class.py`
        - verifique que os resultados obtidos são iguais
        - quais as vantagens desse código sobre o do outro arquivo?

## Exercícios

- documente a classe `IdealGas`
- na pasta `cinetica` há um arquivo com dados experimentais de tempo vs
concentração para uma determinada espécie química em uma reação. Determine a
ordem da reação com relação a essa espécie. Faça:
    - os gráficos de concentração vs tempo; ln(concentração) vs tempo; e inverso
    da concentração vs tempo
    - para cada um dos gráficos, a regressão linear
    - o cálculo da constante de velocidade 
