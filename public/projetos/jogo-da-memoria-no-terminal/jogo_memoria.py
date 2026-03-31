import random


def criar_tabuleiro():
    pares = ["A", "B", "C", "D"]
    cartas = pares * 2
    random.shuffle(cartas)
    return cartas


def exibir_tabuleiro(cartas, reveladas):
    print("\nTabuleiro:")
    for i, carta in enumerate(cartas):
        if reveladas[i]:
            print(f"[{i + 1}:{carta}]", end=" ")
        else:
            print(f"[{i + 1}:*]", end=" ")
    print("\n")


def escolher_posicao(mensagem, total, bloqueadas=None):
    while True:
        try:
            posicao = int(input(mensagem)) - 1

            if posicao < 0 or posicao >= total:
                print("Posição inválida. Escolha um número dentro do tabuleiro.")
                continue

            if bloqueadas and posicao in bloqueadas:
                print("Você já escolheu essa posição nesta rodada. Escolha outra.")
                continue

            return posicao
        except ValueError:
            print("Digite apenas números inteiros.")


def jogar():
    print("=== Jogo da Memória no Terminal ===")
    print("Encontre todos os pares iguais.\n")

    cartas = criar_tabuleiro()
    reveladas = [False] * len(cartas)
    pares_encontrados = 0
    tentativas = 0
    total_pares = len(cartas) // 2

    while pares_encontrados < total_pares:
        exibir_tabuleiro(cartas, reveladas)

        pos1 = escolher_posicao("Escolha a 1ª posição: ", len(cartas))
        if reveladas[pos1]:
            print("Essa carta já foi encontrada. Escolha outra.\n")
            continue

        pos2 = escolher_posicao(
            "Escolha a 2ª posição: ",
            len(cartas),
            bloqueadas={pos1}
        )
        if reveladas[pos2]:
            print("Essa carta já foi encontrada. Escolha outra.\n")
            continue

        tentativas += 1

        print(f"\nVocê revelou: posição {pos1 + 1} = {cartas[pos1]}")
        print(f"Você revelou: posição {pos2 + 1} = {cartas[pos2]}")

        if cartas[pos1] == cartas[pos2]:
            print("Par encontrado!\n")
            reveladas[pos1] = True
            reveladas[pos2] = True
            pares_encontrados += 1
        else:
            print("Não foi dessa vez. Tente novamente.\n")

    print("Parabéns! Você encontrou todos os pares!")
    print(f"Total de tentativas: {tentativas}")


if __name__ == "__main__":
    jogar()
