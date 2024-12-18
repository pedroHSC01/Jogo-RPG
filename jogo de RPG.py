import random
from funções import lista, texto
from itens import monstrosFaceis, inventário, trabalhos, monstrosModerados, monstrosDificeis, personagem, personagens, Monstro

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
      então, F. Mas ainda dá para se divertir \n 
      """)
opcao = False
op = [1, 2, 3, 4]
c_cura = 0

while True:
    print("Escolha um personagem: (Número que ele está)", end="\n \n")
    for i, perso in enumerate(personagens):
        print(f"{i + 1} - {perso[0]}")
        print(f"dano - {perso[1]}\n", f"vida - {perso[2]}\n", f"destreza - {perso[3]}\n")
    person = int(input("\n R:"))

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
        personagem = personagem("Valeria", 15, 27, 19)
        break 
    else:
        print("Digite uma seleção válida", end="\n \n")

print(personagem.nome,
      personagem.dano,
      personagem.vida,
      personagem.destreza)

while True:
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

            while True:
                try:
                    opcao3 = str(input(
"""
Tem certeza? S/N

R: """)).upper()
                except:
                    if opcao3 not in ("SN"):
                        print("Opção inexistente")
                    else: 
                        print("Erro")
                else:
                    if opcao3 == "S":
                        if opcao2 == 1:
                            monstro_atual = random.choice(lista.get_list(monstrosFaceis))
                            break
                        elif opcao2 == 2:
                            monstro_atual = random.choice(lista.get_list(monstrosModerados))
                            break
                        elif opcao2 == 3:
                            monstro_atual = random.choice(lista.get_list(monstrosDificeis))
                            break

                        Resumo = f"Monstro que estamos lutando '{monstro_atual.nome}'. Vida do player {personagem.vida}, vida do monstro {monstro_atual.vida}"
                        print(Resumo)

                        _ = load_dotenv(find_dotenv())

                        combate = f"""Sua missão é simular um combate em um RPG, aqui estão os status dos usuários {Resumo}. Se o player ou o jogador tiver ferido, diga onde ele está ferido, quão grave é a ferida."""

                        prompt = PromptTemplate.from_template(template=combate)
                        chat = ChatGroq(model="Llama3-8b-8192")

                        chain = prompt|chat
                        
                        print(chain.invoke("Status do combate."))
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
