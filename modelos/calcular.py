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
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self):
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            self.valor1 * self.valor2

    def checar_resultado(self, resposta):
        certo = False
        if self.resultado == resposta:
            print('Resposta correta')
            certo = True
        else:
            print('Resposta errada')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    @property
    def _op_simbolo(self):
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def mostrar_operacao(self):
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
