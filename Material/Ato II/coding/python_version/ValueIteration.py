import numpy as np


def value_iteration(
    discount_rate: float,
    threshold: float,
    actions: list,
    states: list,
    rewards: list,
    trans_func_per_action: list,
):

    # Vamos inicializar V(s) para todo estado pertencente
    # ao nosso conjunto de estados
    state_values = np.zeros(len(states))

    # Definindo lista de políticas ótimas para cada estado
    optimal_policy = np.zeros(len(states))
    # Definindo um Delta maior que Threshold,
    # para que ele consiga entrar no while
    delta = threshold + 1.0

    # Loop principal
    while delta > threshold:
        delta = 0.0
        for single_state in states:
            # Primeira atribuição dentro do loop
            old_value = state_values[single_state]  # v <- V(s)
            # Variável para guardar a melhor ação para um estado em questão
            best_action = actions[0]
            # Para o próximo passo, vamos inicializar max_value
            max_value = -1e9

            # Rodando a Action Value Function,
            # ao mesmo tempo que pegamos a ação que maximiza o
            # valor retornado
            for single_action in actions:
                temp = 0.0
                for single_state_apostrophe in states:
                    # Pegando a matriz com probabilidades de transição
                    # com base na ação em questão
                    matriz = trans_func_per_action[single_action]

                    # Pegando a probabilidade de transição para o par
                    # (s, s') em questão.
                    trans_prob = matriz[int(single_state)][int(single_state_apostrophe)]
                    if trans_prob > 0:
                        expected_value = trans_prob * (
                            rewards[single_state_apostrophe]
                            + (discount_rate * state_values[single_state_apostrophe])
                        )
                        temp += expected_value
                # Atualizando max_value, se necessário
                if temp > max_value:
                    max_value = temp
                    best_action = single_action
            # Atualizando a política ótima
            optimal_policy[single_state] = best_action
            # Atualizando a lista com maior valor
            state_values[single_state] = max_value
            # Pegando o maior valor entre os dois
            delta = max(delta, abs(old_value - state_values[single_state]))
    print("Valores de Estado:", state_values)
    return optimal_policy


def value_iteration_vetorial(
    discount_rate: float,
    threshold: float,
    actions: list,
    states: list,
    rewards: list,
    trans_func_per_action: list,
):
    # 1. Preparação dos Dados
    # P vira uma Matriz 3D no formato: (Ações, Estados Atuais, Estados Futuros)
    P = np.array(trans_func_per_action)
    R = np.array(rewards)
    V = np.zeros(len(states))
    optimal_policy = np.zeros(len(states))

    delta = threshold + 1.0

    # Loop principal de convergência
    while delta > threshold:
        # --- A EQUAÇÃO DE BELLMAN EM 2 LINHAS ---

        # Passo 1: Calcula o [ R(s') + gama * V(s') ] para todos os estados de uma vez
        v_target = R + (discount_rate * V)

        # Passo 2: O Somatório de Bellman!
        # O operador '@' multiplica a matriz 3D 'P' pelo vetor 'v_target'.
        # O NumPy faz a soma das probabilidades automaticamente e devolve 'Q',
        # uma matriz onde as linhas são as Ações e as colunas são os Estados.
        Q = P @ v_target

        # --- EXTRAINDO A POLÍTICA E OS VALORES ---

        # Pega a "nota" da melhor ação para cada estado (axis=0 olha pelas linhas/ações)
        new_V = np.max(Q, axis=0)

        # Pega o "índice" (o número) da melhor ação para cada estado
        optimal_policy = np.argmax(Q, axis=0)

        # Atualiza o delta checando a maior diferença de V(s) do tabuleiro inteiro
        delta = np.max(np.abs(new_V - V))

        # Salva as notas para o próximo loop
        V = new_V

    print(f"Valores dos Estados V(s):\n{V}")
    return optimal_policy
