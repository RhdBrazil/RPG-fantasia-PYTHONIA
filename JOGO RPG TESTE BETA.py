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
        print_slow("Os olhos pertencem a um esquilo gigante. Ele ri da sua audácia e te dá uma noz dourada.")
        decisao_floresta_sombria("noz dourada")
    elif escolha == "2":
        print_slow("A árvore na verdade era um troll disfarçado. Ele te encara com fome...")
        decisao_floresta_sombria("troll")
    else:
        print_slow("O vento sopra forte... e nada acontece. Tente de novo!")
        floresta_sombria()

def decisao_floresta_sombria(evento):
    if evento == "noz dourada":
        print_slow("Com sua nova e misteriosa noz dourada, você sente que algo mudou em seu destino...")
        escolha = input("1 - Comê-la imediatamente\n2 - Guardá-la com cuidado\nEscolha: ")

        if escolha == "1":
            print_slow("A noz era mágica! Você cresce 3 metros e assusta um grupo de goblins. Agora é chamado de 'Gigante Nutrição'.")
        elif escolha == "2":
            print_slow("Mais tarde, um mago lhe oferece uma grande quantia de ouro pela noz. Agora você é rico e respeitado!")
        else:
            print_slow("Você se distrai olhando um esquilo normal. Quando percebe, a noz sumiu! Azar seu.")

    elif evento == "troll":
        escolha = input("1 - Tentar conversar com o troll\n2 - Correr desesperadamente\nEscolha: ")

        if escolha == "1":
            print_slow("O troll fica surpreso com sua coragem e, em vez de comer você, decide que agora são amigos. Você ganhou um companheiro troll!")
        elif escolha == "2":
            print_slow("Você corre o mais rápido que pode, mas tropeça numa raiz. O troll ri e te deixa escapar, pois acha que já sofreu o suficiente.")
        else:
            print_slow("O troll se cansa da sua indecisão e vai embora. Você sobreviveu, mas se sente um pouco tolo.")

def cidade_eldoria():
    print_slow("Você chega à grande Cidade de Eldoria, onde tudo parece mais caro do que deveria ser...")
    escolha = input("1 - Ir ao mercado negociar com um mercador duvidoso\n2 - Explorar os becos escuros\nEscolha: ")

    if escolha == "1":
        print_slow("O mercador te vende um mapa falso. Você aprende uma valiosa lição sobre confiança.")
        decisão_cidade_eldoria("mapa falso")
    elif escolha == "2":
        print_slow(
            "Nos becos, um ladrão tenta te roubar. Mas ele escorrega numa casca de banana e você fica com a bolsa dele.")
        decisão_cidade_eldoria("ladrão falha no roubo")
    else:
        print_slow("Você se distrai olhando um pombo e perde sua carteira. Escolha direito!")
        cidade_eldoria()

def decisão_cidade_eldoria(evento):
    if evento == "mapa falso":
        print_slow("você agora fica diante de uma situação onde deve reportar pelos crimes ou perdoar pelo erro do mercador")
        escolha = input("1 reportar os crimes cometidos pelo mercador às autoridades de eldoria\n2 - perdoar pelo erro cometido do mercador\nescolha: ")
        if escolha == "1":
            print_slow("você vai até o soldado oficial de eldoria e reporta o crime do mercador")
        elif escolha =="2":
            print_slow("você lembra que devemos perdoar sempre pelos erros cometidos pelos outros pois estão no seu momento evolutivo do universo")
        else:
            print_slow("o mercador vendo que cometeu o erro e foi pego no ato se arrepende e extorna o valor que foi pago")
    elif evento == "ladrão falha no roubo":
        print_slow("você agora se depara de uma situação da qual ou você tira vantagem da situação ou faz o certo")
        escolha = input("1 rouba a bolsa do ladrão e sai correndo\n2 jogar a bolsa na direção do ladrão para distraí-lo e poder fugir\nescolha: ")
        if escolha == "1":
            print_slow("você roubou o ladrão,deu fuga, e quando ve o conteúdo da bolsa está cheio de drogas ilícitas e dinheiro de tráfico, você perdeu moralmente")
        elif escolha == "2":
            print_slow("você fugiu e saiu correndo, foi o mais sensato a se fazer no calor do momento, você venceu moralmente")
        else:
            print_slow("um oficial da lei aparece numa ronda e você é pego numa situação complicada e é encostado juntamente ao ladrão, você perdeu.")











inicio()