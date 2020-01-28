from dao.sgbd_dao import SGBD, SGBDDao  

class SGBDController:
    def __init__(self):
        self.sd = SGBDDao()

    def select_all(self):
        lista = self.sd.select_all()
        lista_retorno = []
        for i in lista:
            s = SGBD(i[0],i[1],i[2],i[3])
            lista_retorno.append(s)

        return lista_retorno

    def select_byId(self, id):
        s = self.sd.select_byId(id)
        ret = SGBD(s[0],s[1],s[2],s[3])
        return ret

    def insert(self, sgbd : SGBD):
        return self.sd.insert(sgbd)

    def update(self, sgbd : SGBD):
        self.sd.update(sgbd)

    def delete(self, id):
        self.sd.delete(id)

