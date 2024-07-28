#3. Faça um programa que solicite ao usuário o nome de um arquivo de texto para que espaços repetidos
#sejam removidos. Um novo arquivo deve ser criado com o resultado da remoção.

def main():
    nomeArq = input("Informe o nome do arquivo: ")
    escrever_campo(nomeArq)


def escrever_campo(nomeArq):
    arqRef = open(nomeArq+"_refatorado", 'w')
    arq = open(nomeArq, 'r')
    campo = ler_campo(arq)
    esp_vazio = False

    while campo != "":
        if campo == " ":
            esp_vazio = True
        else: 
            arqRef.write(campo)
            campo = ler_campo(arq)

        while esp_vazio:
            campo = ler_campo(arq)
            if campo == " ":
                esp_vazio = True
            else:
                arqRef.write(" ")
                esp_vazio = False


    arqRef.close()
    arq.close()
    
def ler_campo(nomeArq):
    return nomeArq.read(1)

main()


