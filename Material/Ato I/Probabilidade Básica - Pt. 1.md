# Probabilidade Básica - Pt. 1

Aqui, vamos tratar da base para começar a entender as modelagens que poderemos fazer.

As escolhas ótimas a serem definidas pelos algoritmos que vamos aprender no futuro são todas baseadas em probabilidade e em alguns conceitos levemente mais abstratos que não são aprendidos normalmente no ensino médio.

A ideia é apresentar os tópicos com algum rigor matemático, mas, imediatamente, migrar para implementações computacionais, feitas manualmente e/ou com auxílio de alguma biblioteca.

Para aprofundamento efetivo, buscar diretamente da fonte, como os materiais deixados nas referências, é uma escolha adequada.

Caso você já tenha afinidade com probabilidade básica, é provável que você não precise ler essa parte. Haverá um **mapa mental** no final deste capítulo para que você **refresque seus miolos** sempre que necessário. 

(Apesar de que, para seu aprendizado, é muito mais válido que você mesmo(a) faça seu próprio mapa mental)

## O que é Probabilidade?

Primeiro, para entender probabilidade, é necessário pensar em **experimentos**.


### Experimento e Evento

De acordo com o livro **Probability And Statistics**, de DeGroot e Schervish,

Um **experimento** é qualquer processo, **real ou hipotético**, onde os possíveis resultados podem ser identificados à princípio. 

A partir disso, podemos abstrair o conceito de **evento**, que é um conjunto bem definido de possíveis resultados de um experimento.

A coleção dos possíveis resultados de um experimento é chamada de **Espaço Amostral** do experimento.

Por exemplo, podemos pensar nas faces de um dado. Como poderíamos representar em código um conjunto com todas as faces de um dado normal? 

Observe:

```cpp
#include <vector>

std::vector<int> faces = {1, 2, 3, 4, 5, 6};
```

Caso você não tenha visto a nossa Trilha de C++, logo acima utilizamos a `<vector>` para definir um **array** de inteiros, com todas as faces de um **D6** padrão.

Poderíamos pensar, também, em uma moeda:

```cpp
#include <vector>
#include <string>

std::vector<std::string> faces = {"cara", "coroa"};
```

Essa é uma maneira de definir o nosso conjunto, mas poderíamos utilizar outras estruturas de dados livremente, contanto que não exista nenhum "atrito" na hora de realizarmos consultas. Dependendo, um **Hash Map** pode ser viável.

Para o caso do dado:

```cpp
#include <unordered_map>
#include <string>

std::unordered_map<std::string, int> faces;

faces["face_1"] = 1;
faces["face_2"] = 2;
faces["face_3"] = 3;
faces["face_4"] = 4;
faces["face_5"] = 5;
faces["face_6"] = 6;
```

Para o caso da moeda:

```cpp
#include <unordered_map>
#include <string>

std::unordered_map<int, std::string> faces;

faces[1] = "cara";
faces[2] = "coroa";
```

Depende das suas escolhas para a programação e do que você acha mais confortável. 

Às vezes, também, podemos estar construindo um projeto que depende de otimização e bom desempenho para trabalhar com milhares e milhares de valores. Aqui, a escolha da estrutura correta pode ser um grande diferencial.

Vale ressaltar que, em **C++**, para conjuntos pequenos, contínuos e bem definidos (como faces de um D6), um `std::vector` (ou `std::array`) será **infinitamente** mais rápido do que um `std::unordered_map`. O Hash Map exige o cálculo de hashes e alocação dinâmica de nós, gerando um overhead que prejudica a localidade de cache.

Emtão, a partir daqui, usaremos a `<vector>` para fins de simplicidade e otimização.

## Probabilidade

Em um experimento, é necessário associar para cada **Evento A** no **Espaço Amostral S** um número **Pr(A)** que indica a probabilidade de **A** acontecer.

O número **Pr(A)** deve satisfazer três axiomas básicos para satisfazer a definição matemática de probabilidade:

1) Para todo **Evento A**, **Pr(A) >= 0**;
2) **Pr(S) = 1**;
3) Para toda sequência finita de **eventos disjuntos** **A1, A2, ...**,


$$ \Pr \left( \bigcup_{i=1}^{n} A_i \right) = \sum_{i=1}^{n} \Pr(A_i) $$

A **interpretação clássica** de probabilidade é baseada no conceito de **resultados equiprováveis**. 

Por exemplo, quando uma moeda é lançada, temos duas possíveis saídas: **cara** ou **coroa**. Assumindo que esses resultados têm chances iguais de acontecer, eles devem ter a mesma probabilidade. Como a soma das probabilidades deve ser 1, a probabilidade de ser cara e a probabilidade de ser coroa devem ser 1/2.

No caso, se os resultados dos experimentos são **equiprováveis**, calcular probabilidades se reduz a uma contagem.

Temos que: Pr(A) = **|A|/|S|**

**Exemplo 1: rolando dado**

É nítido que, dentre as seis possibilidades com chances iguais, a probabilidade de sair um resultado em específico é **1/6**. Isso, pois, dividimos o nosso **Espaço Amostral** em seis partes iguais! 

```cpp
#include <iostream>
#include <vector>

int main(){
    std::vector<int> faces = {1, 2, 3, 4, 5, 6};

    // Abaixo, usaremos o método size() para obtermos o tamanho do arranjo
    
    std::cout << "Tamanho do conjunto: " << faces.size() << std::endl;

    float probA = 1.0 / faces.size();

    std::cout << "Probabilidade de sair um número qualquer em um D6: " << probA << std::endl;
    return 0;
}
```

Compilando e rodando:

```sh
Tamanho do conjunto: 6
Probabilidade de sair um número qualquer em um D6: 0.166667
```

> Perceba que ocorreu ali uma aproximação no valor de ponto flutuante. O resultado poderia ser diferente caso usássemos double ou invés de float? Verifique.

Bacana! Mas, e se quisermos saber a probabilidade de obtermos resultados específicos em dois lançamentos sequenciais do dado?

É intuitivo que, quando jogamos o mesmo dado duas vezes, os dois lançamentos são independentes, correto? Pelo menos, em condições normais de temperatura e pressão.

Ao levar em conta que o acontecimento de B não interfere em nada na probabilidade de acontecer A, dizemos que A e B são **independentes**.

## Independência

Dois eventos A e B são independentes se **Pr(A ∩ B) = Pr(A) Pr(B)**.

De maneira um pouco simplista, intersecção **A ∩ B** diz respeito, justamente, a quando **duas coisas acontecem simultaneamente**. **Pr(A ∩ B)** é a probabilidade de acontecer A **E** acontecer B. Ela é traduzida matematicamente na forma de multiplicação.

**Exemplo 2: uma coisa E outra**

Voltando para o exemplo do dado: se jogarmos ele duas vezes seguidas, qual a probabilidade de obtermos o **número 1** no primeiro e o **número 2** no segundo?

Sendo A = obter 1 no primeiro, B = obter 2 no segundo: **Pr(A ∩ B) = Pr(A) Pr(B) = 1/6 x 1/6 = 1/36**.

## A Probabilidade da União de Eventos

Para eventos disjuntos A1, A2, ..., sabemos que:

$$ \Pr \left( \bigcup_{i=1}^{n} A_i \right) = \sum_{i=1}^{n} \Pr(A_i) $$

Além disso, para todos os eventos A1 e A2, desconsiderando dependência ou independência, temos que:

**Pr(A1 ∪ A2) = Pr(A1) + Pr(A2) − Pr(A1 ∩ A2).**

Esse resultado pode ser expandido para um número árbitrário finito de eventos. Porém, demonstrar isso foge da proposta deste material. Novamente, a consulta das fontes é recomendada para aprofundamento.

**Exemplo 3: uma coisa OU outra**

Retornando para o exemplo do lançamento do dado, como computamos a probabilidade de obtermos um resultado OU outro? Exemplificadamente, qual a probabilidade de lançarmos um dado e obtermos como resultado **o número 1** ou **o número 2**?

Perceba que esse evento o qual estamos descrevendo é a união de dois eventos particulares. Como foi descrito acima, obtemos a probabilidade a partir de:

**Pr(A) = Pr(A1 ∪ A2) = Pr(A1) + Pr(A2) − Pr(A1 ∩ A2).**

Onde:

(i) A = Obter 1 ou 2;
(ii) A1 = Obter 1;
(iii) A2 = Obter 2;

Ora, é intuitivo pensar que não podemos obter 1 e 2 ao mesmo tempo num lançamento de um único dado. Então, **Pr(A1 ∩ A2) = 0**.

Assim, 

**Pr(A) = Pr(A1 ∪ A2) = Pr(A1) + Pr(A2)**

A probabilidade de obter uma das faces de um dado D6 em um lançamento é **1/6**. Logo:

**Pr(A) = Pr(A1 ∪ A2) = Pr(A1) + Pr(A2) = 1/6 + 1/6 = 2/6 = 1/3**

## Probabilidade Condicional

Suponha que temos conhecimento de que um **evento B** aconteceu. Queremos computar a probabilidade de acontecer outro **evento A**, levado em conta que **B** aconteceu.

A nova probabilidade será chamada de **"Probabilidade de um evento A, dado que B aconteceu"**. Ela será denotada por **Pr(A|B)**.

Se Pr(B > 0), computamos essa probabilidade da seguinte maneira:

**Pr(A|B) = Pr(A ∩ B) / Pr(B)**.

**Pr(A|B)** não é definida se **Pr(B) = 0**. (Consegue imaginar o porquê?)

**Exemplo 4: Suponha que dois dados D6 foram rolados e foi observado que a soma T dos dois números foi ímpar. Qual a probabilidade de T ser menor do que 8?** 

Seja **A** o evento **"T < 8"** e seja **B** o evento **"T é ímpar"**. Assim, **A ∩ B** é o evento onde T é 3, 5 ou 7.

Podemos chegar nos seguintes valores de **Pr(A ∩ B)** e **Pr(B)**:

**Pr(A ∩ B) = 2/36 + 4/36 + 6/36 = 12/3 = 1/3.**

**Pr(B) = 2/36 + 4/36 + 6/36 + 4/36 + 2/36 = 18/36 = 1/2.** 

Logo,

**Pr(A|B) = Pr(A ∩ B)/Pr(B) = 2/3**

## Lei da Probabilidade Total

Suponha que os eventos **B1, ..., Bk** formam uma partição do espaço amostral **S** e **Pr(Bj) > 0** para **j = 1, ..., k**. Então, para todo evento **A** em **S**,

(Imagem de Pr(A) = somatório de j=1 até k de Pr(Bj)Pr(A|Bj))

Chegamos nesse resultado a partir do seguinte raciocício:

Os eventos B1 ∩ A, B2 ∩ A, ..., Bk ∩ A formarão uma partição de A, da maneira a qual está ilustrada na figura abaixo. Logo, escrevemos:

A = (B1 ∩ A) ∪ (B2 ∩ A) ∪ ... ∪ (Bk ∩ A).

Além disso, dado que os **k eventos** são disjuntos,

Pr(A) = somatório de j = 1 até k (Pr(Bj ∩ A)).

Finalmente, se **Pr(Bj) > 0** para **j = 1, ..., k**, então **Pr(Bj ∩ A) = Pr(Bj)Pr(A|Bj)**. Substituindo na equação acima, chegaremos no resultado descrito anteriormente.
