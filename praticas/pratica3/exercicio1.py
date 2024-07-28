import io

VALOR_BAIXO = ''
VALOR_AUTO = '~'

def inicialize():
    ant1, ant2 = VALOR_BAIXO

    lista1 = open("lista1.txt", 'r')
    lista2 = open("lista2.txt", 'r')
    saida = open("saida.txt", 'w')
    
    existem_mais_nomes = True

    return ant1, ant2, lista1, lista2, saida, existem_mais_nomes


def finalize(lista1: io.TextIOWrapper, lista2: io.TextIOWrapper, saida: io.TextIOWrapper) -> None:
    lista1.close()
    lista2.close()
    saida.close()

def leia_nome(lista: io.TextIOWrapper, nome_ant: str, nome_outra_lista: str, existem_mais_nomes: bool):
    nome = lista.readline()
    if not nome:
        if nome_outra_lista == VALOR_AUTO:
            existem_mais_nomes = False
        else:
            nome = VALOR_AUTO
    else:
        if nome <= nome_ant:
            raise KeyError  
        
    return nome, nome_ant, existem_mais_nomes

def merge():
    ant1, ant2, lista1, lista2, saida, existem_mais_nomes = inicialize()
    
    nome1, ant1, existem_mais_nomes = leia_nome(lista1, ant1, ant2, existem_mais_nomes)
    nome2, ant2, existem_mais_nomes = leia_nome(lista2, ant2, ant1, existem_mais_nomes)

    while existem_mais_nomes:
        if nome1 < nome2:
            saida.write(nome1)
            nome1, ant1, existem_mais_nomes = leia_nome(lista1, ant1, ant2, existem_mais_nomes)
        elif nome1 > nome2:
            saida.write(nome2)
            nome2, ant2, existem_mais_nomes = leia_nome(lista2, ant2, ant1, existem_mais_nomes)
        else:
            saida.write(nome1)
            nome1, ant1, existem_mais_nomes = leia_nome(lista1, ant1, ant2, existem_mais_nomes)
            nome2, ant2, existem_mais_nomes = leia_nome(lista2, ant2, ant1, existem_mais_nomes)

    finalize(lista1, lista2, saida)
