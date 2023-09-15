from funcoes import *
from time import sleep

Mega = 60
Quina = 80
Lotofacil = 25
Lotomania = 100

while True:
    print('\033[35mQual loteria deseja fazer? ')
    sleep(1)
    print("\033[36m==-==" * 10)
    print("""\033[33m    [1] Mega Sena
    [2] Lotofácil
    [3] Quina
    [4] Lotomania
    [5] sair do programa""")
    print("\033[36m==-==" * 10)
    sleep(1)
    opcao = int(input("\033[32mDigite uma das opções: "))

    if opcao == 1:
        Loto = 'Mega Sena e pode escolher entre 6 e 15 número por jogo'
        escolha = 6

    if opcao == 2:
        Loto = 'Lotofácil e pode escolher entre 15, 16, 17 e 18 número por jogo'
        escolha = 15

    if opcao == 3:
        Loto = 'Quina e pode escolher entre 5 e 15 número por jogo'
        escolha = 5

    if opcao == 4:
        Loto = 'Lotomania'
        escolha = 50
        numero = 50


    if opcao == 4:
        print(f"Voçe escolheu {Loto}. ")

    else:
        sorteio = input(f"Voçe escolheu {Loto}.\nQual a quantidade de numero por jogo deseja?  ")
        numero = LeiaIntJogo(sorteio, escolha)
        
    jogos = LeiaInt(input("Quantos jogos deseja gerar? "))

    if opcao == 1:
        jogos = GerarJogo(numero, jogos, Mega)
        for jogo in jogos:
            print(jogo)

    if opcao == 2:
        jogos = GerarJogo(numero, jogos, Lotofacil)
        for jogo in jogos:
            print(jogo)

    if opcao == 3:
        jogos = GerarJogo(numero, jogos, Quina)
        for jogo in jogos:
            print(jogo)

    if opcao == 4:
        jogos = GerarJogo(numero, jogos, Lotomania)
        for jogo in jogos:
            print(jogo)

    if opcao == 5:
        break
