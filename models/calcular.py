from random import randint


class Calcular:

    def __init__(self, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor1
        self.__valor2: int = self._gerar_valor2
        self.__operacao: int = randint(1, 3)  # Gerar de 1 a 3 ( 1 = Somar , 2  = Diminuir , 3 = Multiplicar)
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f"Valor 1: {self.valor1}     Valor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}"

    @property
    def _gerar_valor1(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(1, 50)
        elif self.dificuldade == 3:
            return randint(1, 100)
        elif self.dificuldade == 4:
            return randint(1, 1000)
        else:
            return randint(1, 100000)

    @property
    def _gerar_valor2(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 5)
        elif self.dificuldade == 2:
            return randint(1, 100)
        elif self.dificuldade == 3:
            return randint(1, 200)
        elif self.dificuldade == 4:
            return randint(1, 1000)
        else:
            return randint(1, 200000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            return None

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return None

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
            certo = False
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        return print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?: ')
