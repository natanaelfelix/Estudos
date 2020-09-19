from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None: pass
    print('Carro de Luxo está buscando cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None: pass
    print('Carro de Popular está buscando cliente...')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'

if __name__== '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular']
    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()
