def main():
    nomeArq = input("Informe o nome do arquivo: ")
    try:
        ENTRADA = open(nomeArq, 'rb')
        RRN = int(input("Informe o RRN: "))
        if RRN >= total_reg(ENTRADA):
            print("RRN invalido")
            return 0
            
        offset = RRN * 64 + 4
        ENTRADA.seek(offset)

        reg = ler_reg(ENTRADA)
        i = 1
        for x in reg:
            print(f"Campo {i}: {x}")
            i += 1

        ENTRADA.close()
    
    except FileNotFoundError:
        print("Error")


def total_reg(entrada):
    total_reg = entrada.read(4)
    total_reg_int = int.from_bytes(total_reg)
    return total_reg_int

def ler_reg(entrada):
    buffer = entrada.read(64)
    buffer_string = buffer.decode()

    return buffer_string.split("|")

main()