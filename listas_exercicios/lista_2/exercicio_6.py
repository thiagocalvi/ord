#6. Faça um programa que leia uma sequência de 10 números inteiros a partir da entrada padrão e, a seguir,
#escreva a sequência em um arquivo em formato binário. Considere que todos os inteiros deverão ser
#armazenados no arquivo com 4 bytes de tamanho.

import struct

def main():
    nomeArq = input("Informe o nome do arquivo: ")
    try:
        arq = open(nomeArq, 'wb')
        
        for x in range(10):
            number = input(f"Infome o {x+1}° número: ")
            escrever(number, arq)

        arq.close()
    
    except FileNotFoundError:
        print("Error")
    
def escrever(number, arq):
    num = int(number)
    arq.write(struct.pack('i', num))

main()