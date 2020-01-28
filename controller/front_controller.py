from dao.front_dao import FrontDao, FrontEnd

class FrontController:
    def __init__(self):
        self.dao = FrontDao()
        
    def select_all(self):
        lista = self.dao.select_all()
        lista_retorno = []
        for b in lista:
            ba = FrontEnd(b[0], b[1], b[2], b[3])
            lista_retorno.append(ba)
        return lista_retorno
    
    def select_byId(self, id):
        lista = self.dao.select_byId(id)
        b = FrontEnd(lista[0],lista[1],lista[2],lista[3])
        return b
    
    def update(self, front : FrontEnd):
        self.dao.update(front)

    def insert(self, front : FrontEnd):
        return self.dao.insert(front)
        
    def delete(self, id):
        self.dao.delete(id)

        