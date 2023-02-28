from datetime import datetime

def get_autor():
    n_autores = get_inteiro_positivo("Informe o número de autores: ")
    et_al = False
    autor = ""
    if n_autores > 3:
        print("\nSó é possível adicionar 3 autores no máximo, portanto, usaremos a expressão \
'et al' após o nome do 1º autor.")
        n_autores = 1
        et_al = True
    print("\nDigite nome e sobrenome do autor (nesta ordem). A inicial do nome também é aceita.")
    for i in range(n_autores):
        nome = input(f'{i+1}º autor: ')
        nome = nome.split()
        autor += f'{nome[-1].upper()},'
        for j in range(len(nome)-1):
            autor += f' {nome[j][0].upper()}.'
        if i != n_autores - 1:
            autor += "; "
    if et_al:
        autor += ". et al."
    return autor


def get_frase(tipo, AVISO = False, msg_aviso = ''):
    if AVISO:
        print('\n' + msg_aviso)
    while True:
        frase = input(f'{tipo}: ')
        if frase == '':
            print("\nErro! Tente novamente.\n")
        else:
            break
    frase = frase.strip()
    if frase[-1] == ".":
        return frase[:-1]
    else:
        return frase


def get_tradutor():
    while True:
        traduzido = input("\nO livro é traduzido? (s/n): ")
        traduzido = traduzido.lower()
        if traduzido == 's':
            nome = input("Digite o nome do tradutor: ")
            nome = nome.split()
            tradutor = nome[-1].upper() + ','
            for i in range(len(nome)-1):
                tradutor += f' {nome[i][0].upper()}.'
            return f' Tradução: {tradutor}'
        elif traduzido == 'n':
            return None


def get_edicao():
    n_edicao = get_inteiro_positivo("\nInforme a edição: ")
    while True:
        ingles = input("A publicação é em inglês? (s/n): ")
        ingles = ingles.lower()
        if ingles == 'n':
            return f'{n_edicao}. ed.'
        elif ingles == 's':
            if n_edicao == '1':
                return "1st ed."
            elif n_edicao == '2':
                return "2nd ed."
            elif n_edicao == '3':
                return "3rd ed."
            else:
                return f'{n_edicao}th ed.'
        print("\nErro! Digite 's' ou 'n' para prosseguir.\n")


def get_local():
    print("\nInforme o local de publicação. Se o local puder ser identificado mas não estiver \
registrado, utilize colchetes para identificá-lo. Caso não seja possível identificar o \
local, pressione Enter.")
    local = input("\nLocal de publicação: ")
    if local == '':
        return "[s.l.]"
    else:
        return local


def get_editora():
    print("\nInforme a editora. Caso a editora não puder ser identificada, pressione Enter")
    editora = input("Editora: ")
    if editora == '':
        return "[s.n.]"
    else:
        return editora


def get_ano(msg):
    ANO_ATUAL = datetime.now().year
    ano = str(get_inteiro_positivo(msg, ANO_ATUAL))
    return ano


def get_paginacao():
    tipo = input("\nPaginação, Intervalo de páginas, Volume, Fascículo? (P/I/V/F): ")
    tipo = tipo.upper()
    if tipo == 'N':
        return None
    elif tipo == 'P':
        print("\nInforme a página referenciada. Caso tenha utilizado o livro inteiro como \
referência, informe o número total de páginas do livro.")
        paginacao = str(get_inteiro_positivo("Paginação: "))
        return f'{paginacao} p.'
    elif tipo == 'I':
        lim_inferior = str(get_inteiro_positivo("Limite inferior: "))
        lim_superior = str(get_inteiro_positivo("Limite superior: "))
        return f'p. {lim_inferior}-{lim_superior}'
    elif tipo == 'V':
        volume = str(get_inteiro_positivo("Volume: "))
        return f'v. {volume}'
    elif tipo == 'F':
        fasciculo = str(get_inteiro_positivo("Fascículo: "))
        return f'n. {fasciculo}'


def get_data():
    MESES = {1:(31,"jan."), 2:(0,"fev."), 3:(31,"mar."), 4:(30,"abr."), 5:(31,"mai."), 6:(30,"jun."),\
             7:(31,"jul."), 8:(31,"ago."), 9:(30,"set."), 10:(31,"out."), 11:(30,"nov."), 12:(31,"dez.")}
    ANO_ATUAL = datetime.now().year
    MES_ATUAL = datetime.now().month
    DIA_ATUAL = datetime.now().day
    ano = get_inteiro_positivo("Ano: ", ANO_ATUAL)
    if ano == ANO_ATUAL:
        mes = get_inteiro_positivo("Mês: ", MES_ATUAL)
        if mes == MES_ATUAL:
            dia = get_inteiro_positivo("Dia: ", DIA_ATUAL)
        else:        
            dia = get_inteiro_positivo("Dia: ", MESES[mes][0])
    else:
        mes = get_inteiro_positivo("Mês: ", 12)
        if mes == 2:
            if ano%4==0 and (ano%100!=0 and ano%400==0):
                dia = get_inteiro_positivo("Dia: ", 29)
            else:
                dia = get_inteiro_positivo("Dia: ", 28)
        else:        
            dia = get_inteiro_positivo("Dia: ", MESES[mes][0])
    return f'{dia} {MESES[mes][1]} {ano}'


def get_acesso():
    print("\nInforme a disponibilidade e a data de acesso.")
    url = input("url: ")
    print("\nData de acesso: ")
    data = get_data()
    return f'Disponível em: {url}. Acesso em: {data}'


def get_inteiro_positivo(msg="Digite um número inteiro positivo: ", lim=0):
    while True:
        try:
            num = int(input(msg))
            if num <= 0:
                print("O número deve ser maior que 0.\n")
            elif lim == 0:
                return num
            elif num > lim:
                print(f'O número digitado deve ser menor ou igual a {lim}')
            else:
                return num
        except (TypeError, ValueError):
            print("Erro! Digite um número inteiro maior que 0.\n")