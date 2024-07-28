from dataclasses import dataclass

class IndexList:
    def __init__(self, id, offset):
        self.id = id
        self.offset = offset


@dataclass
class IndiceLinear:
    def __init__(self, file:str):
        self.file = file
        self.SIZEOF_TOTALREG = 4
        self.SIZEOF_TAMREG = 2
        self.indexList:list = []
        
    def openFile(self):
        self.file = open(self.file, "r+b")

    def closeFile(self):
        self.file.close()

    def readHeader(self):
        self.file.seek(0)
        header = self.file.read(self.SIZEOF_TOTALREG)
        return int.from_bytes(header)

    def createIndex(self):
        self.file.seek(self.SIZEOF_TOTALREG)
        offset = self.file.tell()
        tam_regitro = int.from_bytes(self.file.read(self.SIZEOF_TAMREG))

        while tam_regitro > 0:
            registro = self.file.read(tam_regitro).decode().split("|")            
            identificador = registro[0]
            self.indexList.append(IndexList(int(identificador), offset))
            offset = self.file.tell()
            tam_regitro = int.from_bytes(self.file.read(self.SIZEOF_TAMREG))
    
    def showIndexList(self):
        for x in self.indexList:
            print(f"ID: {x.id}, Offset: {x.offset}")

    def getId(self, x):
        return x.id

    def odenarIndex(self):
        self.indexList.sort(key=lambda obj: obj.id)


    def buscaRegistro(self):
        id = int(input("Informe o id do registro: "))
        i = 0
        f = len(self.indexList) - 1
        while i <= f:
            m = (i + f) // 2
            if self.indexList[m].id == id:
                self.file.seek(self.indexList[m].offset)
                registro = self.file.read(int.from_bytes(self.file.read(self.SIZEOF_TAMREG))).decode()
                registro = registro.split("|")

                print(f"Id: {registro[0]}")
                print(f"Nome: {registro[1]}")
                print(f"Título: {registro[2]}")
                print(f"Curso: {registro[3]}")
                print(f"Tipo: {registro[4]}")
    

            if self.indexList[m].id < id:
                i = m + 1
            else:
                f = m - 1
        return "Registro não encontado"



def main():
    file = input("Informe o nome do arquivo: ")
    a = IndiceLinear(file)
    a.openFile()
    print(f"Quantidade de registros: {a.readHeader()}")
    a.createIndex()
    a.odenarIndex()
    a.showIndexList()
    a.buscaRegistro()
    a.closeFile()

main()