#7. Faça um programa que leia uma sequência de 10 valores de 4 bytes a partir do arquivo criado no exercício
#anterior e os imprima como na saída padrão como números inteiros.

import struct

def main():
    nomeArq = input("Informe o nome do arquivo: ")

    try:
        arq = open(nomeArq, 'rb')

        for x in range(10):
            print(ler_valor(arq, 4))

    except FileNotFoundError:
        print("Error")


def ler_valor(arq, q_bytes):
    num = arq.read(q_bytes)
    num_int = struct.unpack('i', num)
    return num_int 


main()