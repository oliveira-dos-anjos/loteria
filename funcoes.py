from random import randint

# Função para verificar o que o input recebeu e salvar a quantidade de números por jogo
def LeiaIntJogo(msg, escolha):
    num = escolha
    try:
        n = int(msg)

    except ValueError:
        print("O valor não corresponde a um número valido")
        n = LeiaInt(input("digite novamente "))
    except KeyboardInterrupt:
        print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
        return 0
    if n < escolha:
        n = LeiaIntJogo((input(f"Digite um valor igual ou maior a {num}: ")), num)
    return n

def LeiaInt(msg):
    try:
        n = int(msg)

    except ValueError:
        print("O valor não corresponde a um número valido")
        n = LeiaInt(input("digite novamente "))
    except KeyboardInterrupt:
        print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
        return 0
    return n



def GerarJogo(numero, jogos, Jogo):
   # Lista para armazenar os jogos
    jogos_gerados = []

    for _ in range(jogos):
        lista = []
        while len(lista) < numero:
            n = randint(1, Jogo)
            if n not in lista:
                lista.append(n)
        
        jogos_gerados.append(lista)

    return jogos_gerados
            
