import random
from funções import lista, texto
from itens import monstrosFaceis, inventário, trabalhos, monstrosModerados, monstrosDificeis

#HUD

esc = """Opções:

1-Lutar
2-Invetário
3-Trabalhar
4-Usar cura

Ação: """
print("\n")
print("""
      Olá usuário, muito obrigado e bem vindo ao jogo que fiz de RPG
      Este jogo é focado mais em combate que em história, não temos eventos por enquanto
      então, F. Mas ainda dá para se divertir \n 
      """)

opcao = False
op = [1, 2, 3, 4]
c_cura = 0

while True:
    opcao = int(input(esc))

    try:
        if opcao not in (op):
            print("Opção inexistente")

    except:
        print("Erro")
    else:
        if opcao == 1:
            opcao = int(input("""
Escolha a dificuldade:

1-Facil
2-Moderado
3-Dificil

R: """))
            try:

                if opcao not in (op):
                    print("Opção inexistente")

            except:
                print("Erro")
            erro = False

            while True:
                try:
                    opcao2 = str(input(
"""
Tem certeza? S/N

R: """)).upper()
                except:
                    if opcao2 not in ("SN"):
                        print("Opção inexistente")
                    else: 
                        print("Erro")
                else:
                    if opcao2 == "S":
                        if opcao == 1:
                            monstro_atual = random.choice(lista.get_list(monstrosFaceis))
                            print(monstro_atual)
                        elif opcao == 2:
                            monstro_atual = random.choice(lista.get_list(monstrosModerados))
                            print(monstro_atual)
                        elif opcao == 3:
                            monstro_atual = random.choice(lista.get_list(monstrosDificeis))
                            print(monstro_atual)
                    elif opcao2 == "N":
                        break

    if opcao == 2:
        print(texto.linha(30))
        for i, item in enumerate(inventário):
        
            print(f"{i + 1} - {item['nome']}")
        print(texto.linha(30), "\n")

    if opcao == 3:
        print(texto.linha(30), "\n")
        for i, item in enumerate(trabalhos):
            try:
                if item["tempo"] in int:
                    print(f"{i + 1} - {item['nome']}\n", f"Tempo: {item["tempo"]}H", end="\n \n")
            except:
                print(f"{i + 1} - {item['nome']}\n", f"Tempo: {item["tempo"]}", end="\n \n")
        print(texto.linha(30), "\n")
    if opcao == 4:
        print(texto.linha(30), end="\n \n")
        for i, item in enumerate(inventário):
            if item["tipo"] == "cura":
                print(f"{i} - {item['nome']}", end="\n \n")
                c_cura += 1
        if c_cura == 0:
            print("\033[1;31mVocê não tem nenhuma cura\033[m", end='\n \n')
        c_cura = 0
