from dao.squad_dao import Squad, SquadDao
from controller.back_controller import BackController, BackEnd
from controller.front_controller import FrontController, FrontEnd
from controller.sgbd_controller import SGBDController, SGBD

class SquadController:
    def __init__(self):
        self.sd = SquadDao()
        self.sc = SGBDController()
        self.bc = BackController()
        self.fc = FrontController()

    def select_all(self):
        lista = self.sd.select_all()
        retorno = []
        for i in lista:
            squad = Squad(i[0],i[1],i[2],i[3])
            if i[4] != None:
                squad.id_linguagemFront = i[4]
                squad.linguagemFront = self.fc.select_byId(i[4])
            if i[5] != None:
                squad.id_linguagemBack = i[5]
                squad.linguagemBack = self.bc.select_byId(i[4])
            if i[6] != None:
                squad.id_sgbd = i[6]
                squad.sgbd = self.sc.select_byId(i[6])
                
            retorno.append(squad)

        return retorno

    def select_byId(self, id):
        s = self.sd.select_byId(id)
        squad = Squad(s[0],s[1],s[2],s[3])
        squad.linguagemFront = self.fc.select_byId(s[4])
        squad.linguagemBack = self.bc.select_byId(s[5])
        squad.sgbd = self.sc.select_byId(s[6])
        return squad

    def insert(self, squad : Squad):
        self.sd.insert(squad)
    
    def update(self, squad : Squad):
        self.sd.update(squad)

    def delete(self,id):
        self.sd.delete(id)