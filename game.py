from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    continuar: int = 0
    jogar(pontos, continuar)


def jogar(pontos: int, continuar: int) -> None:
    if continuar > 0:
        dificuldade: int = continuar
    else:
        dificuldade: int = int(input('Informe o nivel de dificuldade desejado entre 1 e 4: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe a resposta para: ')
    calc.mostrar_operacao()

    resultado: int = int(input('R: '))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo? (0 - Não, 1 - Sim, 2 - Mudar dificuldade): '))

    if continuar == 2:
        jogar(pontos, 0)
    elif continuar == 1:
        jogar(pontos, dificuldade)
    else:
        print(f'Voce finalizou com {pontos} pontos.')
        print('Até a próxima')


if __name__ == '__main__':
    main()
