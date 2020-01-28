import MySQLdb
from model.frontend import FrontEnd
from dao.conexao import Conexao

class FrontDao(Conexao):
    def select_all(self):
        self.cursor.execute('SELECT * FROM 02_JM_FrontEnd')
        return self.cursor.fetchall()

    def select_byId(self,id):
        self.cursor.execute(f"SELECT * FROM 02_JM_FrontEnd WHERE ID={id}")
        return self.cursor.fetchone()
        
    def update(self, front : FrontEnd):
        self.cursor.execute(f"UPDATE 02_JM_FrontEnd  SET Nome = '{front.Nome}', Descricao = '{front.Descricao}', Versao = '{front.Versao}' WHERE ID = {front.id}")
        self.conexao.commit()

    def insert(self, front: FrontEnd):
        self.cursor.execute(f"INSERT INTO 02_JM_FrontEnd(Nome,Descricao,Versao) VALUES('{front.Nome}','{front.Descricao}','{front.Versao}')")
        self.conexao.commit()
        return self.cursor.lastrowid
    
    def delete(self,id):
        self.cursor.execute(f"DELETE FROM 02_JM_FrontEnd WHERE ID={id}")
        self.conexao.commit()
