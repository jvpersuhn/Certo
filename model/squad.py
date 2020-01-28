class Squad:
    def __init__(self, id, nome, descricao, numeroPessoas):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.numeroPessoas = numeroPessoas
        self.__id_linguagemBack = 'Null'
        self.__id_linguagemFront = 'Null'
        self.__id_sgbd = 'Null'
        self.__linguagemBack = None
        self.__linguagemFront = None
        self.__sgbd = None
    
    def __str__(self):
        return f'{self.id} {self.nome} {self.descricao} {self.numeroPessoas} {self.linguagemBack} {self.linguagemFront} {self.sgbd}' 
    
    @property
    def id_linguagemBack(self):
        return self.__id_linguagemBack

    @id_linguagemBack.setter
    def id_linguagemBack(self, l):
        self.__id_linguagemBack = l

    @property
    def id_linguagemFront(self):
        return self.__id_linguagemFront

    @id_linguagemFront.setter
    def id_linguagemFront(self, l):
        self.__id_linguagemFront = l

    @property
    def id_sgbd(self):
        return self.__id_sgbd

    @id_sgbd.setter
    def id_sgbd(self, l):
        self.__id_sgbd = l

    @property
    def linguagemBack(self):
        return self.__linguagemBack

    @linguagemBack.setter
    def linguagemBack(self, l):
        self.__linguagemBack = l

    @property
    def linguagemFront(self):
        return self.__linguagemFront

    @linguagemFront.setter
    def linguagemFront(self, l):
        self.__linguagemFront = l

    @property
    def sgbd(self):
        return self.__sgbd

    @sgbd.setter
    def sgbd(self, l):
        self.__sgbd = l