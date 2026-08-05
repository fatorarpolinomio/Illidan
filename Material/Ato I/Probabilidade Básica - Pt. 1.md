# Probabilidade Básica - Pt. 1

Aqui, vamos tratar da base para começar a entender as modelagens que poderemos fazer.

As escolhas ótimas a serem definidas pelos algoritmos que vamos aprender no futuro são todas baseadas em probabilidade e em alguns conceitos levemente mais abstratos que não são aprendidos normalmente no ensino médio.

A ideia é apresentar os tópicos com algum rigor matemático, mas, imediatamente, migrar para implementações computacionais, feitas manualmente e/ou com auxílio de alguma biblioteca.

Para aprofundamento efetivo, buscar diretamente da fonte, como os materiais deixados nas referências, é uma escolha adequada.

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

std::vector<string> faces = {"cara", "coroa"};
```

Essa é uma maneira de definir o nosso conjunto, mas poderíamos utilizar outras estruturas de dados livremente, contanto que não exista nenhum "atrito" na hora de realizarmos consultas. Dependendo, um **Hash Map** pode ser viável.

Para o caso do dado:

```cpp
#include <unordered_map>

std::unordered_map<string, int> faces;

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

std::unordered_map<int, string> faces;

faces[1] = "cara";
faces[2] = "coroa";
```

Depende das suas escolhas para a programação e do que você acha mais confortável. 

Às vezes, também, podemos estar construindo um projeto que depende de otimização e bom desempenho para trabalhar com milhares e milhares de valores. Aqui, a escolha da estrutura correta pode ser um grande diferencial.

## Probabilidade

Em um experimento, é necessário associar para cada **Evento A** no **Espaço Amostral S** um número **Pr(A)** que indica a probabilidade de **A** acontecer.

O número **Pr(A)** deve satisfazer três axiomas básicos para satisfazer a definição matemática de probabilidade:

1) Para todo **Evento A**, **Pr(A) >= 0**;
2) **Pr(S) = 1**;
3) Para toda sequência finita de **eventos disjuntos** **A1, A2, ...**,

(Imagem do produtório x Somatório)

A **interpretação clássica** de probabilidade é baseada no conceito de **resultados equiprováveis**. 

Por exemplo, quando uma moeda é lançada, temos duas possíveis saídas: **cara** ou **coroa**. Assumindo que esses resultados têm chances iguais de acontecer, eles devem ter a mesma probabilidade. Como a soma das probabilidades deve ser 1, a probabilidade de ser cara e a probabilidade de ser coroa devem ser 1/2.

No caso, se os resultados dos experimentos são **equiprováveis**, calcular probabilidades se reduz a uma contagem.

Temos que: Pr(A) = **|A|/|S|**

**Exemplo 1: rolando dado**

É nítido que, dentre as seis possibilidades com chances iguais, a probabilidade de sair um resultado em específico é: **1/6**.

```cpp
#include <iostream>
#include <vector>

int main(){
    std::vector<int> faces = {1, 2, 3, 4, 5, 6};

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

> Perceba que ocorreu ali uma aproximação no valor de ponto flutuante.

## O que é Probabilidade Condicional?

## Lei da Probabilidade Total

## Independência
