class FrontEnd:
    def __init__(self, id, Nome, Descricao, Versao):
        self.id = id
        self.nome = Nome
        self.descricao = Descricao
        self.versao = Versao

    def __str__(self):
        return  f"{self.id},{self.nome},{self.descricao},{self.versao}"