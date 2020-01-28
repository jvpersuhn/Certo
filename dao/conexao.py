import MySQLdb

class Conexao():
    def __init__(self):
        self.host = 'mysql.padawans.dev'
        self.database = 'padawans13'
        self.user = 'padawans13'
        self.paswd = 'mj2019'

        self.conexao = MySQLdb.connect(host=self.host, database=self.database, user=self.user, passwd=self.paswd)
        self.cursor = self.conexao.cursor()