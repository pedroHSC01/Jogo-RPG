from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers.string import StrOutputParser
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv


def combate(cont = 1, lesao = "", debuf = "", inimigo = "goblin"):
    for i in range(0, cont):
        _ = load_dotenv(find_dotenv())

        if cont == 1:
            template = f"""Sua missão é simular um cenário em um RPG, você só vai dizer os elementos que estão no ambiente. Inimigo: {inimigo}. Ferimentos: {lesao} . Se este campo estiver vazio, é porque o player não teve nenhuma lesao ou ferimento. Debuf do usuário: {debuf}. Se este campo estiver vazio, é porque o player não teve nenhuma lesao ou ferimento.
            Não diga o debuf ou os status do usuário
            """ + """ {text}

            Faça um texto, sem nenhuma formatação nas frases (sem negrito, sem itálico, etc.), e você só vai fazer um relatório
            então não precisa dizer "oque quer fazer logo em seguida", ou "Oque você faz", etc... e não precisa dizer que o player/monstro conseguiu algum buff ou debuff.
             E NÃO precisa falar os status do player ou do monstro (vida, dano, etc...). Use no máximo 5 linhas"""
            cont += 1
        
        combate = template

        prompt = PromptTemplate.from_template(template=combate)
        chat = ChatGroq(model="Llama3-8b-8192")

        chain = prompt|chat

        a = chain.invoke("Status do combate").content

        if cont != 2:
            template = f"""Chat passado: {a}. Sua missão é simular um cenário em um RPG, você só vai dizer os elementos que estão no ambiente. Inimigo: {inimigo}. Ferimentos: {lesao} . Se este campo estiver vazio, é porque o player não teve nenhuma lesao ou ferimento. Debuf do usuário: {debuf}. Se este campo estiver vazio, é porque o player não teve nenhuma lesao ou ferimento.
            
            Não diga o debuf ou os status do usuário""" + """ {text} Faça um texto, sem nenhuma formatação nas frases (sem negrito, sem itálico, etc.), e você só vai fazer um relatório
            então não precisa dizer "oque quer fazer logo em seguida", e não precisa dizer que o player/monstro conseguiu algum buff ou debuff. E NÃO precisa falar os status do player ou do monstro (vida, dano, etc...). Use no máximo 5 linhas"""

        return print(a)

combate()
