from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers.string import StrOutputParser
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

combate = """Sua missão é simular um combate em um RPG, aqui estão os status dos usuários, Dragrao, vida: 100 menos 20. player vida: 30 menos 10. Se o player ou o jogador tiver ferido, diga onde ele está ferido, quão grave é a ferida.{text}"""

prompt = PromptTemplate.from_template(template=combate)
chat = ChatGroq(model="Llama3-8b-8192")

chain = prompt|chat

a = chain.invoke("Status do combate")
print(a)
