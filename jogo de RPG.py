import random
import time
from random import choices
from funções import lista, texto
from itens import monstrosFaceis, inventário, trabalhos, monstrosModerados, monstrosDificeis, personagem, Monstro, personage, atacar_player, arma, atacar_monstro
from IA_grog import combate
### progressão de cenários

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers.string import StrOutputParser
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

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
      então, F. Mas ainda dá para se divertir \n \n""")
opcao = False
op = [1, 2, 3, 4]
c_cura = 0

while True:
    print("Escolha um personagem: (Número que ele está)", end="\n \n")
    for i, perso in enumerate(personage):
        print(f"{i + 1} - ", end="")
        print(perso, end="\n \n")
    person = int(input("\nR:"))

    if person == 1:
        personagem = personagem("Alrindel", 15, 13, 25)
        break  
    elif person == 2:
        personagem = personagem("Baruk", 20, 20, 7)
        break  
    elif person == 3:
        personagem = personagem("Gideon", 35, 26, 8)
        break  
    elif person == 4:
        personagem = personagem("Lyra", 9, 8, 16)
        break  
    elif person == 5:
        personagem = personagem("Valeria", 40, 27, 19)
        break 
    else:
        print("Digite uma seleção válida", end="\n \n")

print(personagem)
evento = ""
while evento != "02":
    opcao = int(input(esc))

    try:
        if opcao not in (op):
            print("Opção inexistente")

    except:
        print("Erro")
    else:
        if opcao == 1:
            opcao2 = int(input("""
Escolha a dificuldade:

1-Facil
2-Moderado
3-Dificil

R: """))
            try:

                if opcao2 not in (op):
                    print("Opção inexistente")
            except:
                print("Erro")
            erro = False

            while evento != "02":
                try:
                    opcao3 = str(input("""
Tem certeza? S/N

R: """)).upper()
                    texto.linhas(1)
                except:
                    if opcao3 not in ("SN"):
                        print("Opção inexistente")
                    else: 
                        print("Erro")
                else:
                    if opcao3 == "S":
                        
                            if opcao2 == 1:
                                monstro_atual = random.choice(lista.get_list(monstrosFaceis))
                            elif opcao2 == 2:
                                monstro_atual = random.choice(lista.get_list(monstrosModerados))
                            elif opcao2 == 3:
                                monstro_atual = random.choice(lista.get_list(monstrosDificeis))
                            print(monstro_atual, end="\n  \n")
                            combate(inimigo=monstro_atual)
                            while True:
                                texto.linha(25)
                                cont = 0
                                for i, item in enumerate(inventário):
                                    cont += 1
                                    if cont == 1:
                                        lista_armas = []
                                    if item["tipo"] == "arma":
                                        arma_atual = item['status']
                                        print(f"{i + 1} - {arma_atual.nome}")
                                        lista_armas.append(arma_atual)
                                texto.linha(25)
                                arma_equi = int(input("Escolha uma arma (pelo número): "))
                                arma_atual = lista_armas[arma_equi - 1]
                                dano_player = atacar_player(personagem, monstro_atual, arma_atual)
                                vidaM = monstro_atual.vida - dano_player
                                print(vidaM)

                                texto.processando(2)

                                if vidaM <= 0:
                                    print("Monstro derrotado")
                                    evento = "01" # Monstro derrotado
                                    break
                                if dano_player != 0:
                                    print(f"Você deu {dano_player} de dano. Agora é o turno do seu inimigo!")
                                    monstro_atual.down_status(vida=dano_player)
                                else:
                                    print(f"Você \033[31mErrou o golpe\033[m. Agora é o turno do seu inimigo!")

                                dano_monstro = atacar_monstro(personagem, monstro_atual)
                                personagem.down_status(vida=dano_monstro)

                                texto.processando(3.5)

                                if personagem.vida <= 0:
                                    evento = "02"
                                    break
                                if dano_monstro != 0:
                                    print(f"O monstro deu {dano_monstro} de dano. Agora é o seu turno!")
                                else:
                                    print(f"O monstro \033[32mErrou o golpe\033[m. Agora é o seu turno!")
                                time.sleep(1)
                                print(f"Você está com {personagem.vida}/{personagem.maxvida} de vida.")

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
                if isinstance(item["tempo"], int):
                    print(f"{i + 1} - {item['nome']}\n", f"Tempo: {item["tempo"]}h", end="\n \n")
                else:
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
print("Você morreu...")
