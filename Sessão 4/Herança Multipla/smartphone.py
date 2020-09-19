from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin): #agora temos a funcionalidade de logo aqui dentro
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
    def conectar(self):
        if not self._ligado:
            info = (f'{self._nome} não está ligado!')
            self.log_info(info)
            return
        if self._conectado:
            error = (f'{self._nome}, já está conectado!')
            print(error)
            self.log_info(error)
        info = (f'{self._nome} está conectado!')
        print(info)
        self.log_info(info)
        self._conectado = True
    def desconectar(self):
        if not self._conectado:
            error = (f'{self._nome}, não está conectado!')
            print(error)
            self.log_error(error)
            return
        info = (f'{self._nome}, foi desconetado desconetado!')
        print(info)
        self.log_info(info)
        self._conectado = False
