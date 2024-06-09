#4. Faça um programa que receba do usuário um arquivo de código em python e produza um novo arquivo
#contendo o mesmo código, mas com todos os comentários de linha removidos. Um comentário de linha
#começa com ‘#’ em qualquer posição de uma linha e se estende até o final dela.
def main():
    nomeArq = input("Informe o nome do arquivo: ")
    remover_comentarios(nomeArq)


def remover_comentarios(nomeArq):
    try:
        arq = open(nomeArq, 'r')
        arqRef = open(nomeArq+"_refatorado", 'w')
        caracter = ler_caracter(arq)

        while caracter != "":
            if caracter != "#":
                arqRef.write(caracter)
                caracter = ler_caracter(arq)
            else:
                while caracter == "#":
                    caracter = ler_caracter(arq)

        arq.close()
        arqRef.close()

    except FileNotFoundError:
        print("Erro")



def ler_caracter(nomeArq):
    return nomeArq.read(1)


main()