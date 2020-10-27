from modelos.calcular import Calcular


def jogar(pontos):
    dificuldade = int(
        input('Informe o nivel de dificuldade desejado: (1, 2, 3, 4)'))
    calc = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')

    continuar = int(input('Deseja continuar no jogo 1 - sim | 0 - não: '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print('Até a próxima')


def main():
    pontos = 0
    jogar(pontos)


if __name__ == '__main__':
    main()
