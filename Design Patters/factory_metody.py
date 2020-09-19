from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:

        print('Carro de Luxo está buscando cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro de Popular está buscando cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)
    @staticmethod
    @abstractclassmethod
    def get_carro(tipo: str) -> Veiculo: pass
        
    def buscar_cliete(self):
        self.carro.buscar_cliente()


    
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'
    def buscar_cliete(self):
        self.carro.buscar_cliente()

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
    def buscar_cliete(self):
        self.carro.buscar_cliente()

if __name__== '__main__':
    from random import choice
    veiculos_disponiveis_zonanorte = ['luxo', 'popular']
    veiculos_disponiveis_zonasul = ['luxo']
    print("Zona Norte")
    for i in range(10):
        carro = ZonaNorteVeiculoFactory.get_carro(choice(veiculos_disponiveis_zonanorte))
        carro.buscar_cliente()

    print("Zona sul")

    for i in range(10):
        carro2 = ZonaSulVeiculoFactory.get_carro(choice(veiculos_disponiveis_zonasul))
        carro2.buscar_cliente()