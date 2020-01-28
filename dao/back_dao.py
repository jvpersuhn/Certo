import MySQLdb
from model.backend import BackEnd
from dao.conexao import Conexao

class BackDao(Conexao):
    def select_all(self):
        self.cursor.execute('SELECT * FROM 02_JM_BackEnd')
        return self.cursor.fetchall()

    def select_byId(self,id):
        self.cursor.execute(f"SELECT * FROM 02_JM_BackEnd where id = {id}")
        return self.cursor.fetchone()
        
    def update(self, back : BackEnd):
        comand = f"UPDATE 02_JM_BackEnd  SET Nome = '{back.nome}', Descricao = '{back.descricao}', Versao = '{back.versao}' WHERE ID = {back.id}"
        self.cursor.execute(comand)
        self.conexao.commit()

    def insert(self, back: BackEnd):
        self.cursor.execute(f"INSERT INTO 02_JM_BackEnd(Nome,Descricao,Versao) VALUES('{back.nome}','{back.descricao}','{back.versao}')")
        self.conexao.commit()
        return self.cursor.lastrowid
            
    def delete(self,id):
        self.cursor.execute(f"DELETE FROM 02_JM_BackEnd WHERE ID={id}")
        self.conexao.commit()