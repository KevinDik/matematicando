from random import randint


class Calcular:
    def __init__(self, dificuldade, /):
        self.__dificuldade = dificuldade
        self.__valor1 = self._gerar_valor
        self.__valor2 = self._gerar_valor
        self.__operacao = randint(1, 2)
        self.__resultado = self._gerar_resultado

    @property
    def dificuldade(self):
        return self.__dificuldade

    @property
    def valor1(self):
        return self.__valor1

    @property
    def valor2(self):
        return self.__valor2

    @property
    def operacao(self):
        return self.__operacao

    @property
    def resultado(self):
        return self.__resultado

    def __str__(self):
        op = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'valor 1: {self.valor1} \nvalor 2: {self.valor2} ' \
               f'\ndificuldade: {self.dificuldade} \noperação: {op}'

    @property
    def _gerar_valor(self):
        pass

    @property
    def _gerar_resultado(self):
        pass

    def checar_resultado(self, resposta):
        pass

    def mostar_operacao(self):
        pass
