#8. Faça um programa que leia várias strings a partir da entrada padrão e as escreva em um arquivo. No
#arquivo, cada string deve ser precedida por um número inteiro de 2 bytes que corresponde ao seu
#comprimento. Assim, o arquivo resultante conterá tanto números binários quanto strings.

def main():
    nomeArq = input("Informe o nome do arquivo: \n")
    try:
        arq = open(nomeArq, 'wb')
        entrada = input("Informe a entrada (ou deixe em branco pra sair): \n")
        while entrada != "":
            escrever_dado(entrada, arq)
            entrada = input("Informe a entrada (ou deixe em branco pra sair): \n")
    except:
        print("Error")

    arq.close()


def escrever_dado(entrada, arq):
    entrada_binario = entrada.encode()
    tam = len(entrada_binario)
    tam_binario = int.to_bytes(tam)

    arq.write(tam_binario)
    arq.write(entrada_binario)

main()