from dao.conexao import Conexao
from model.squad import Squad
from model.backend import BackEnd
from model.frontend import FrontEnd
from model.sgbd import SGBD

class SquadDao(Conexao):
    def select_all(self):
        self.cursor.execute("SELECT * FROM 02_JM_Squad")
        ret = self.cursor.fetchall()
        return ret

    def select_byId(self, id):
        self.cursor.execute(f"SELECT * FROM 02_JM_Squad WHERE Id = {id}")
        ret = self.cursor.fetchone()
        return ret

    def update(self, squad : Squad):
        self.cursor.execute(f"update 02_JM_Squad set Nome = '{squad.nome}', Descricao = '{squad.descricao}', NumeroPessoas = {squad.numeroPessoas}, id_backEnd = {squad.id_linguagemBack}, id_frontEnd = {squad.id_linguagemFront}, id_sgbd = {squad.id_sgbd} where Id = {squad.id}")
        self.conexao.commit()

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM 02_JM_Squad WHERE Id = {id}")
        self.conexao.commit()
    
    def insert(self, squad : Squad):
        self.cursor.execute(f"insert into 02_JM_Squad (Nome,Descricao,NumeroPessoas,id_frontEnd,id_backEnd,id_sgbd) values ('{squad.nome}','{squad.descricao}',{squad.numeroPessoas}, {squad.id_linguagemFront},{squad.id_linguagemBack},{squad.id_sgbd})")
        self.conexao.commit()