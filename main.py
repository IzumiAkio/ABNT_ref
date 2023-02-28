from construtor import *
from datetime import datetime
from time import sleep
import pandas as pd
import os
import csv

def main():

    qtd_ref = get_inteiro_positivo("Digite o número de referências bibliográficas utilizadas: ")
    lista_ref = []

    while len(lista_ref) < qtd_ref:
        os.system('cls')
        print("(L)ivro, (T)rabalho acadêmico, (V)ideo, (P)ágina da internet.")
        tipo_ref = input(f'Qual será o tipo da {len(lista_ref)+1}ª referência? ')
        tipo_ref = tipo_ref.upper()
        if tipo_ref == 'L':
            lista_ref.append(constroi_livro())
        elif tipo_ref == 'T':
            lista_ref.append(constroi_trabacademico())
        elif tipo_ref == 'V':
            lista_ref.append(constroi_video())
        elif tipo_ref == 'P':
            lista_ref.append(constroi_pag())
        else:
            print("Erro! Tente novamente.")
            sleep(2)
    
    lista_ref = sorted(lista_ref)

    nome_arq = input("\n\nDê um nome ao arquivo: ")

    arquivo_salvar = pd.DataFrame(lista_ref)
    arquivo_salvar.to_csv(f'{nome_arq}.txt', index=False, header=False, quoting=csv.QUOTE_NONE, sep='\t')

    return None


if __name__ == '__main__':
    main()