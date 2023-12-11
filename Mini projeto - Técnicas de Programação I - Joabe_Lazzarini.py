# Databricks notebook source
# MAGIC %md
# MAGIC Mini projeto - Técnicas de Programação I
# MAGIC
# MAGIC Objetivo:
# MAGIC
# MAGIC Você tem a tarefa de criar uma simulação para um jogo de dados. Essa simulação tem como objetivo reunir estatísticas para analisar a justiça do jogo, possíveis resultados e fazer previsões sobre jogos futuros.
# MAGIC
# MAGIC Desafios do Projeto:
# MAGIC
# MAGIC Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.
# MAGIC
# MAGIC Múltiplas Simulações: Use a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). Armazene o resultado de cada jogo em um array NumPy.
# MAGIC
# MAGIC Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:
# MAGIC
# MAGIC A média dos resultados.\
# MAGIC O lançamento máximo e mínimo.\
# MAGIC O número de vezes que cada possível lançamento (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12) ocorreu.
# MAGIC
# MAGIC Teste de Hipótese:\
# MAGIC Agora vamos fazer um pouco de teste de hipóteses:\
# MAGIC Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?\
# MAGIC O que isso significa para um jogador do jogo de dados?
# MAGIC
# MAGIC Entregáveis
# MAGIC Um script Python (arquivo .py ou .ipynb) com a sua solução para os desafios apresentados.
# MAGIC Tempo de apresentação: A depender da quantidade de grupos. (Aproximadamente de 15 ~ 20 minutos)

# COMMAND ----------

import numpy as np

def simular_lancamento():
    dado1 = np.random.randint(1, 7) # Metodo randint - retorna numeros aleatorios de 1 à 6
    dado2 = np.random.randint(1, 7) # Metodo randint - retorna numeros aleatorios de 1 à 6
    return dado1 + dado2

def simular_n_jogos(n):
    resultados = np.array([simular_lancamento() for _ in range(n)]) # list comprehension - visão mais phytonica para simular um número n de jogos, chamando a função simular_lancamento repetidamente e armazenar os resultados em um array.
    return resultados

def analisar_resultados(resultados):
    media = np.mean(resultados) # Metodo Mean  - calcula a media do array resultados
    lancamento_maximo = np.max(resultados) # Metodo max  - calcula qual foi o lançamento maximo do array "resultados"
    lancamento_minimo = np.min(resultados) # Metodo min - calcula qual foi lançamento minimo do array "resultado"
    
    contagem_lancamentos = np.bincount(resultados)[2:]

    print("Média dos resultados:", media)
    print("Lançamento máximo:", lancamento_maximo)
    print("Lançamento mínimo:", lancamento_minimo)
    print("Número de vezes que cada possível lançamento ocorreu:")
    for i, contagem in enumerate(contagem_lancamentos, start=2):
        print(f"{i}: {contagem} vezes")

    return contagem_lancamentos

"""
numpy.bincount
Conta o número de ocorrências de cada valor na matriz de inteiros não negativos. O número de caixas (de tamanho 1) é uma unidade maior que o maior valor em x. Se min...
"""

def teste_hipotese(resultados):
    probabilidade_esperada = 1/6  # Probabilidade de cada resultado em um jogo justo

    frequencia_relativa = np.bincount(resultados)[2:] / len(resultados)
    erro_medio_quadratico = np.sum((frequencia_relativa - probabilidade_esperada) ** 2)

    print("\nTeste de hipótese:")
    if erro_medio_quadratico < 0.01:  
        print("A simulação coincide com a suposição de um jogo justo.")
    else:
        print("A simulação não coincide com a suposição de um jogo justo.")

def executar_simulacao_e_analise(numero_jogos):
    resultados = simular_n_jogos(numero_jogos)
    contagem_lancamentos = analisar_resultados(resultados)
    teste_hipotese(resultados)

#Imprime os resultados para a analise
resultados = simular_n_jogos(numero_jogos)
contagem_lancamentos = analisar_resultados(resultados)
teste_hipotese(resultados)
