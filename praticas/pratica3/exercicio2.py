from sys import argv
import io

VALOR_BAIXO = ''
VALOR_ALTO = '~'

numEOF = 0

def inicialize(caminho: str, numListas: int):
    nomes = [VALOR_BAIXO] * numListas
    anteriores = [VALOR_BAIXO] * numListas
    listas = [VALOR_BAIXO] * numListas
    for i in range(numListas):
        nomearq = f'{caminho}/lista{1}.txt'
        listas[i] = open(nomearq, 'r')
    
    saida = open("saida.txt", 'w')

    return anteriores, nomes, listas, saida, True


def finalize(listas: list[io.TextIOWrapper], saida: io.TextIOWrapper, numListas: int):
    for i in range(numListas):
        listas[i].close()

    saida.close()


def leia_nome(lista: io.TextIOWrapper, nome_ant: str, existem_mais_nomes: bool, numListas: int):
    global numEOF
    nome = lista.readline()
    
    if not nome:
        nome = VALOR_ALTO
        numEOF += 1
        
        if numEOF == numListas:
            existem_mais_nomes = False
    
    else:
        if nome <= nome_ant:
            raise ValueError(f'Erro de sequência na {lista.name} -> {nome}')
    
    return nome, nome, existem_mais_nomes



def kwaymerge(caminho: str, numListas: int) -> None:
    try:  
        anteriores, nomes, listas, saida, existem_mais_nomes = inicialize(caminho, numListas)        

        for i in range(numListas):
            nomes[i], anteriores[i], existem_mais_nomes = leia_nome(listas[i], anteriores[i], existem_mais_nomes, numListas)

        while existem_mais_nomes:
            menor = 0
            for i in range(numListas):
                if nomes[i] < nomes[menor]:
                    menor = i
            saida.write(nomes[menor])
            nomes[menor], anteriores[menor], existem_mais_nomes = leia_nome(listas[menor], anteriores[menor], existem_mais_nomes, numListas)

        finalize(listas, saida, numListas)

    except Exception as e:
        print(f'Erro: {e}')


def main() -> None:
    modoDeUso = f'\nModo de uso:\n$ {argv[0]} diretorio_listas numListas'
    if len(argv) < 3:
        raise TypeError('Número incorreto de argumentos.'+ modoDeUso)
    kwaymerge(argv[1], int(argv[2]))



if __name__ == '__main__':
    main() 