from input import *

def constroi_livro():
    livro = f'{get_autor()} {get_frase("Título")}.{get_tradutor()} {get_edicao()} {get_local()}: {get_editora()}, \
{get_ano("Ano de publicação: ")}. {get_paginacao()}'
    return livro


def constroi_trabacademico():
    trab = f'{get_autor()} {get_frase("Título")}. {get_ano("Ano de despósito: ")}. \
{get_paginacao()} {get_frase("Tipo", True, "Informe o tipo de trabalho (e.g. tese, dissertação etc.)")} \
({get_frase("Grau", True, "Informe o grau (e.g. Mestrado em Ciência da Computação)")}) \
- {get_frase("Instituição")}, {get_local()}, {get_ano("Ano de defesa: ")}. {get_acesso()}.'
    return trab


def constroi_video():
    while True:
        autoria = input("Autor do vídeo ou nome do canal? (A/C): ").upper()
        if autoria == 'A':
            autoria = get_autor()
            break
        elif autoria == 'C':
            autoria = get_frase("Nome do canal") + '.'
            break
        else:
            print("Erro! Tente novamente.")
    video = f'{autoria} {get_frase("Título do vídeo")}. {get_local()}: {get_frase("Nome do canal")}, {get_ano("Ano de publicação: ")}. \
{get_frase("Elemento", True, "Informe o que se está referenciando (e.g. 1 vídeo, 2 vídeos, 1 playlist etc.)")} \
({get_frase("Duração do vídeo (n min)")}). {get_acesso()}.'
    return video


def constroi_pag():
    pag = f'{get_autor()} {get_frase("Título")}. In: {get_frase("Nome do site")}. {get_local()}, '
    print("Data de publicação: ")
    pag += f'{get_data()}. {get_acesso()}.'
    return pag