class SGBD:
    def __init__(self,id,nome,descricao,versao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.versao = versao

    def __str__(self):
        return f'{self.id} {self.nome} {self.descricao} {self.versao}'