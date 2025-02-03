import time


def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def inicio():
    print_slow("Bem-vindo(a) ao Reino de Pythonia! Um lugar onde heróis são feitos... ou devorados por goblins!")
    print_slow("Você está na taverna 'O Orc Bêbado'. O que deseja fazer?")

    escolha = input("1 - Falar com o taverneiro\n2 - Falar com o misterioso homem encapuzado\nEscolha: ")

    if escolha == "1":
        falar_taverneiro()
    elif escolha == "2":
        falar_encapuzado()
    else:
        print_slow("Você tropeça e cai. Todos riem. Tente novamente!")
        inicio()


def falar_taverneiro():
    print_slow(
        "Taverneiro: 'Saudações, viajante! Dizem que uma grande aventura espera por aqueles que ousam ir até a Floresta Sombria.'")
    proxima_escolha()


def falar_encapuzado():
    print_slow(
        "O homem encapuzado olha para você e sussurra: 'A verdade está na Cidade de Eldoria... se tiver coragem.'")
    proxima_escolha()


def proxima_escolha():
    escolha = input("1 - Ir para a Floresta Sombria\n2 - Ir para a Cidade de Eldoria\nEscolha: ")

    if escolha == "1":
        floresta_sombria()
    elif escolha == "2":
        cidade_eldoria()
    else:
        print_slow("Um portal se abre e te joga de volta para a taverna. Escolha certo agora!")
        proxima_escolha()


def floresta_sombria():
    print_slow("Você entra na Floresta Sombria e logo percebe olhos brilhando na escuridão...")
    escolha = input("1 - Gritar 'Eu não tenho medo!'\n2 - Se esconder atrás de uma árvore\nEscolha: ")

    if escolha == "1":
        print_slow(
            "Os olhos pertencem a um esquilo gigante. Ele ri da sua audácia e te dá uma noz dourada. Você venceu... eu acho.")
    elif escolha == "2":
        print_slow("A árvore na verdade era um troll disfarçado. Ele te come. Fim de jogo.")
    else:
        print_slow("O vento sopra forte... e nada acontece. Tente de novo!")
        floresta_sombria()


def cidade_eldoria():
    print_slow("Você chega à grande Cidade de Eldoria, onde tudo parece mais caro do que deveria ser...")
    escolha = input("1 - Ir ao mercado negociar com um mercador duvidoso\n2 - Explorar os becos escuros\nEscolha: ")

    if escolha == "1":
        print_slow("O mercador te vende um mapa falso. Você aprende uma valiosa lição sobre confiança. Fim.")
    elif escolha == "2":
        print_slow(
            "Nos becos, um ladrão tenta te roubar. Mas ele escorrega numa casca de banana e você fica com a bolsa dele. Parabéns?")
    else:
        print_slow("Você se distrai olhando um pombo e perde sua carteira. Escolha direito!")
        cidade_eldoria()


inicio()