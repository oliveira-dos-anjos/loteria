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


# Função para ler os numeros inteiros para escolha de quantidade de jogos a serem gerados
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

def LeiaInt2(msg):
    while True:
        try:
            n = int(msg)

            if 1 <= n <= 5:
                return n
            else:
                msg = input("Não é uma opção válida! Digite novamente: ")

        except ValueError:
            print("O valor não corresponde a um número válido.")
            msg = input("Digite novamente: ")
        except KeyboardInterrupt:
            print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
            return 0

  


# Função para gerar os jogos
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
            
