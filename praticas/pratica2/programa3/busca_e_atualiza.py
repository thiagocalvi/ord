import io

TAM_REG = 64
TAM_CAB = 4

def menu():
    print('''\n\n\n\t PROGRAMA PARA INSERCAO E ALTERACAO DE REGISTROS')
    \n\nSuas opcoes sao:\n
    \t1. Inserir um novo registro
    \t2. Buscar um registro por RRN para alteracoes
    \t3. Sair do programa\n''')
    
    opcao = int(input('Digite o numero da sua opcao: '))
    
    return opcao


def le_campos():
    campos = ['Sobrenome: ', 'Nome: ', 'Endereco: ', 'Cidade: ', 'Estado: ', 'CEP: ']
    buffer = ''
    for string in campos:
        campo = input(string)
        buffer += campo + '|'
    buffer = buffer.encode()
    buffer = buffer.ljust(TAM_REG, b'\0')
    return buffer


def le_rrn():
    rrn = int(input('\n\nDigite o RRN do registro: '))
    return rrn


def le_reg_e_mostra(rrn: int, arq: io.BufferedRandom):
    try:
        # calcule o offset e faça o seek
        offset = rrn * TAM_REG + TAM_CAB
        arq.seek(offset)   

        # leia e decodifique o buffer
        buffer = (arq.read(TAM_REG)).decode()
        
        # remova caracteres '\0' à direita do buffer
        buffer = buffer.rstrip('\0')
        
        # imprima os campos
        print('\n\nConteudo do registro\n')
        for campo in buffer.split(sep='|'):
            if campo:
                print(f'\t{campo}')
    except OSError as e:
        print(f'Erro le_reg_e_mostra: {e}')


def modifica_reg():
    print('\n\nVoce quer modificar este registro?\n')
    resp = input('   Responda S ou N, seguido de <Enter> ==> ').casefold()
    if resp == 's':
        return True
    else:
        return False


def main():
    nomeArq = input('Digite o nome do arquivo: ')
    try:
        try:
            arq = open(nomeArq, 'r+b')
            # leia o cabeçalho e decodifique-o
            cab = arq.read(TAM_CAB)
            totalReg = int.from_bytes(cab)
        except FileNotFoundError:
            arq = open(nomeArq, 'w+b')
            # inicialize o cabeçalho e grave-o
            totalReg = 0
            cab = totalReg.to_bytes(TAM_CAB)
            arq.write(cab)

        opcao = menu()
        
        while (opcao < 3):
            # inserir
            if opcao == 1:

                print('Digite os dados do novo registro:\n')
                reg = le_campos()
                offset = totalReg * TAM_REG + TAM_CAB
                arq.seek(offset)
                arq.write(reg)
                totalReg += 1
            # buscar
            elif opcao == 2:
                rrn = le_rrn()
                if rrn >= totalReg:
                    print('\nRRN invalido...Retornando para o menu...')
                else:
                    le_reg_e_mostra(rrn, arq)
                    # modificar?
                    if modifica_reg():
                        print('Digite os dados do novo registro:\n')
                        reg = le_campos()
                        offset = rrn * TAM_REG + TAM_CAB
                        arq.seek(offset)
                        arq.write(reg)

            opcao = menu()
            # fim while
        arq.seek(0)
        arq.write(totalReg.to_bytes(TAM_CAB))
        arq.close()
    except OSError as e:
        print(f'Erro main: {e}')


main()