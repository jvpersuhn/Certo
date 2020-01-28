from dao.back_dao import BackDao, BackEnd 

class BackController:
    def __init__(self):
        self.dao = BackDao()

    def select_all(self):
        lista = self.dao.select_all()
        lista_retorno = []
        for b in lista:
            ba = BackEnd(b[0], b[1], b[2], b[3])
            lista_retorno.append(ba)
        return lista_retorno
    
    def select_byId(self,id):
        lista = self.dao.select_byId(id)
        b = BackEnd(lista[0],lista[1],lista[2],lista[3])
        return b
    
    def update(self, back : BackEnd):
        self.dao.update(back)

    def insert(self, back : BackEnd):
        return self.dao.insert(back)
        
    def delete(self, id):
        self.dao.delete(id)

        