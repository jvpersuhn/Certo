from model.sgbd import SGBD
from dao.conexao import Conexao
from model.sgbd import SGBD

class SGBDDao(Conexao):
    def select_all(self):
        self.cursor.execute("SELECT * FROM 02_JM_SGBD")
        return self.cursor.fetchall()

    def select_byId(self,id):
        self.cursor.execute(f"SELECT * FROM 02_JM_SGBD WHERE id={id}")
        return self.cursor.fetchone()

    def update(self,sgbd : SGBD):
        self.cursor.execute(f"UPDATE 02_JM_SGBD SET nome='{sgbd.nome}', descricao='{sgbd.descricao}', versao='{sgbd.versao}' where id = {sgbd.id}")
        self.conexao.commit()

    def delete(self,id):
        self.cursor.execute(f"DELETE FROM 02_JM_SGBD where id = {id}")
        self.conexao.commit()
    
    def insert(self,sgbd : SGBD):
        self.cursor.execute(f"INSERT INTO 02_JM_SGBD(Nome,Descricao,Versao) VALUES ('{sgbd.nome}','{sgbd.descricao}','{sgbd.versao}')")
        self.conexao.commit()
        return self.cursor.lastrowid