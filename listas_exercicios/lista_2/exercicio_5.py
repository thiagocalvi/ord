#5. A quebra de linha em arquivos de texto muda dependendo do S.0. No DOS/Windows é utilizado o par de
#caracteres ‘\r’ ‘\n’ (decimal ASCII 13 e 10). Já no Unix/Linux, é utilizado apenas o caractere ‘\n’. Faça um
#programa que converta arquivos de texto do Windows para Linux e vice-versa. Seu programa deve receber
#o nome do arquivo a ser convertido e o sentido da conversão (se Windows → Linux ou Linux → Windows).
#O resultado da conversão deve ser gravado em um novo arquivo, preservando os dados do arquivo
#original. Lembre-se de abrir os arquivos em modo binário (tanto o de leitura quanto o de escrita), para
#que você consiga processar os caracteres de quebra de linha corretamente.

import sys

def main():
    if len(sys.argv) != 4:
        print("Use python \"exercicio_5.py <nome_do_arquivo> <sitema de origem> <sistema de destino>\"")
        sys.exit(1)

    nomeArq = sys.argv[1]
    try:
        arq = open(nomeArq, 'rb')
        newArq = open(nomeArq+"_"+sys.argv[3], 'wb')
        if sys.argv[2].upper() == "WINDOWS" and sys.argv[3].upper() == "LINUX":
            win_to_linux(arq, newArq)

        elif sys.argv[2].upper() == "LINUX" and sys.argv[3].upper() == "WINDOWS":
            linux_to_win(arq, newArq)

        arq.close()
        newArq.close()

    except FileNotFoundError:
        print("Error")


def ler_caracter(nomeArq):
    caracter_binario = nomeArq.read(1) 
    return caracter_binario

def win_to_linux(arq, newArq):
    caracter = ler_caracter(arq)
    
    while caracter:
        if caracter == b'\r':
            newArq.write(b'\n')
        else:
            newArq.write(caracter)
        caracter = ler_caracter(arq)


def linux_to_win(arq, newArq):
    caracter = ler_caracter(arq)
    
    while caracter:
        if caracter == b'\n':
            newArq.write(b'\r')
        else:
            newArq.write(caracter)
        
        caracter = ler_caracter(arq)

if __name__ == "__main__":
    main()

