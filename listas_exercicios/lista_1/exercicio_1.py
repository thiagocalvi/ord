def main():
    nomeArq = input("Informe o nome do arquivo: ")
    input_operacao = input("Informe a  operação [leitura = r], [escrita = w]")

    if input_operacao == 'r':
        ler_dados_arq(nomeArq)
    
    elif input_operacao == 'w':
        escrever_campo(nomeArq)


def escrever_campo(nomeArq):
    try:
        arq = open(nomeArq, 'w')
        entrada = ler_dados_entrada()
        while entrada != "":
            arq.write(entrada + "|")
            entrada = ler_dados_entrada()
        arq.close()

    except Exception as e:
        print(f"Erro: {e}")

def ler_dados_entrada():
    entrada = input("Informe o dado a ser gravado no arquivo (ou deixe em branco para sair): ")
    return entrada

def ler_campo(entrada):
    campo = ""
    arq = entrada
    c = arq.read(1)
    while c != "|" and c != "":
        campo += c
        c = arq.read(1)
    return campo

def ler_dados_arq(nomeArq):
    try:
        arq = open(nomeArq, 'r')
        campo = ler_campo(arq)
        while campo != "":
            print(campo + " ")
            campo = ler_campo(arq)

        arq.close()
    
    except Exception as e:
        print(f"Erro: {e}")

main()