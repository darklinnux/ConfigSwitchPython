class Switch:
    
    def __init__(self, nome,ip,user, password):
        self.nome = nome
        self.ip = ip
        self.user = user
        self.password = password
    
    def __openConection(self):
        pass
    
    def __configPort(self, numbPort, numbVlan):
        pass
        
    def configurarPorta(self, numbPort, numbVlan):
        self.__configPort(numbPort, numbVlan)