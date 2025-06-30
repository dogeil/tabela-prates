import math
from tqdm import tqdm
import numpy as np
import pandas as pd

# Função para encontrar números primos até um valor máximo
def encontrar_primos(numero_maximo):
    primos = []

    for num in tqdm(range(2, numero_maximo + 1), desc="Verificando primos"):
        eh_primo = True

        for divisor in range(2, int(math.sqrt(num)) + 1):
            if num % divisor == 0:
                eh_primo = False
                break

        if eh_primo:
            primos.append(num)

    return primos

lista_primos = encontrar_primos(1000000)
print(f"Foram encontrados {len(lista_primos)} números primos")


# Função para gerar uma matriz de divisibilidade
def gerar_matriz_divisibilidade(tamanho, salvar_csv=False, separador_csv=","):
    dados = np.zeros((tamanho, tamanho), dtype=int)

    for linha in tqdm(range(1, tamanho + 1), desc="Construindo matriz"):
        for coluna in range(tamanho):
            if coluna % linha == 0:
                dados[linha - 1][coluna] = 1

    # Criar DataFrame com rótulos
    df = pd.DataFrame(dados, index=range(1, tamanho + 1), columns=range(tamanho))

    if salvar_csv:
        df.to_csv("matriz_divisibilidade.csv", index_label="Divisor", sep=separador_csv)

    return df

df = gerar_matriz_divisibilidade(500, salvar_csv=True)