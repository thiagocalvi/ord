def leia_campo(ENTRADA):
    campo = ""
    c = ENTRADA.read(1)
    while c != "|" and c != "":
        campo += c
        c = ENTRADA.read(1)

    return campo


def le_campos():
    NOME_ARQ = input("Informe o nome do arquivo a ser lido: ")

    try: 
        ENTRADA = open(NOME_ARQ ,'r')
        
        campo = leia_campo(ENTRADA)
        contador = 1

        while campo != "":
            print(f"Campo #{contador}: {campo}")
            campo = leia_campo(ENTRADA)
            contador += 1

        ENTRADA.close()

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    except Exception as e:
        print(f"Erro: {e}")

le_campos()