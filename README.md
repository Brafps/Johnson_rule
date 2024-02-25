# Problema de Sequenciamento de Johnson

Bem-vindo ao repositório dedicado ao Problema de Sequenciamento de Johnson! Neste espaço, exploraremos a regra de Johnson, uma heurística valiosa para otimizar a ordem de execução de tarefas em ambientes de produção. 

## O que é o Problema de Sequenciamento de Johnson?

O Problema de Sequenciamento de Johnson é um desafio clássico de otimização, com aplicações práticas em diversos setores. Ele se concentra na organização eficiente da ordem de execução de tarefas em máquinas, buscando minimizar o tempo total de conclusão.

## A Regra de Johnson em Ação

Como ela é implementada:

0. Tenha uma lista com algumas tarefas que necessitem de dois estágios para serem concluídas.
1. Encontre o menor tempo de processamento na lista de tarefas.
2. Se o menor tempo estiver no primeiro estágio, aloque a tarefa na primeira sequência disponível. Se estiver no segundo estágio, aloque a tarefa na última sequência disponível.
3. Elimine a tarefa da lista.
4. Volte ao passo 1.

### Exemplo para aplicar

Uma Fábrica tem dois processos sequênciais, o de montagem e o de teste. Dada uma lista com seis produtos: cachorros:


<center>

Id | Montagem | Teste
:---: | :---: | :---:
1 | 5 | 3
2 | 4 | 6
3 | 2 | 4
4 | 9 | 2
5 | 8 | 5
6 | 6 | 2

</center>

Qual a melhor sequencia de entrada deles, para realizar o trabalho no menor tempo possível?

Imagine também um dia de trabalho em uma cozinha movimentada. A regra de Johnson poderia ser aplicada para otimizar a sequência de preparação de pratos, minimizando o tempo necessário para concluir as diferentes etapas.



### Aplicação em Processos Complexos

Em ambientes de manufatura, a regra de Johnson pode ser fundamental para otimizar a produção em várias máquinas. Por exemplo, na fabricação de componentes eletrônicos, a ordem eficiente das etapas de produção pode reduzir significativamente o tempo total de fabricação.



### Implementações em Python e R

Encontrará neste repositório implementações práticas do Problema de Sequenciamento de Johnson em Python e R (construção). O notebook (python) está bem explicativo fornecendo uma introdução passo a passo à aplicação da regra de Johnson.


> Espero que este repositório seja útil para sua jornada de aprendizado em otimização e sequenciamento!