from random import choices, randint

class Monstro:
    def __init__(self, nome, vida, dano, destreza, arma = None):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.destreza = destreza
        if arma != None:
            self.arma = arma

    def __str__(self):
        return f"{self.nome}: Vida {self.vida}, Dano {self.dano}, Destreza {self.destreza}"
    
    def up_status(self, dano=0, vida=0, destreza=0):
        self.dano = self.dano + dano
        self.vida = self.vida + vida
        self.destreza = self.destreza + destreza

    def down_status(self, dano=0, vida=0, destreza=0):
        self.dano = self.dano - dano
        self.vida = self.vida - vida
        self.destreza = self.destreza - destreza

# Sistema de combate

class personagem():
    def __init__(self, nome, vida, dano, destreza, ):
        self.nome = nome
        self.dano = dano
        self.vida = vida
        self.destreza = destreza
        self.maxdano = dano
        self.maxvida = vida

    def __str__(self):
        return f"Nome: {self.nome}\nDano: {self.dano}\nVida: {self.vida}\nDestreza: {self.destreza}"
    
    def up_status(self, dano=0, vida=0, destreza=0):
        self.dano = self.dano + dano
        self.vida = self.vida + vida
        self.destreza = self.destreza + destreza

    def down_status(self, dano=0, vida=0, destreza=0):
        self.dano = self.dano - dano
        self.vida = self.vida - vida
        self.destreza = self.destreza - destreza

#####

class arma():
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f"{self.nome}:\nDano {self.dano}"

class cura():
    def __init__(self, nome, cura):
        self.nome = nome
        self.dano = cura
    def __str__(self):
        return f"{self.nome}:\nCura {self.cura}"
# Sistema de usar um item

#personagens = [
#    ["Alrindel", 15, 13, 25],
#    ["Baruk", 20, 20, 7],
#    ["Gideon", 35, 26, 8],
#    ["Lyra", 9, 8, 16],
#    ["Valeria", 15, 27, 19]
#]

personage = [
    personagem("Alrindel", 15, 13, 25),
    personagem("Baruk", 20, 20, 7),
    personagem("Gideon", 35, 26, 8),
    personagem("Lyra", 9, 8, 16),
    personagem("Valeria", 15, 27, 19)
]

def atacar_player(personagem, Monstro, arma = None):
    opcao = [1, 2]
    chance = [(personagem.destreza), (Monstro.destreza / 2)]
    chanceC = [1, 9]
    acerto = choices(opcao, chance)
    acerto = int(acerto[0])
    if arma == None:
        class arma():
            def __init__(self, nome, dano):
                self.nome = nome
                self.dano = dano
        arma = arma("mão", 4)
    if acerto == 1:
        critico = choices(opcao, chanceC)
        critico = int(critico[0])
        if critico == 1:
            dano = arma.dano + personagem.dano
            return dano
        if critico == 2:
            dano = arma.dano + (randint(1, (int(personagem.dano / 2))))
            return dano
    elif acerto == 2:
        erro = 0
        return erro
    else:
        return ("erro total")
    print("FIM")

def atacar_monstro(personagem, Monstro, arma = None):
    opcao = [1, 2]
    chance = [(personagem.destreza / 2), (Monstro.destreza)]
    chanceC = [1, 9]
    acerto = choices(opcao, chance)
    acerto = int(acerto[0])
    if arma == None:
        class arma():
            def __init__(self, nome, dano):
                self.nome = nome
                self.dano = dano
        arma = arma("mão/pata/garra", (int(Monstro.dano / 2)))
    if acerto == 2:
        critico = choices(opcao, chanceC)
        critico = int(critico[0])
        if critico == 1:
            dano = arma.dano + Monstro.dano
            return dano
        if critico == 2:
            dano = arma.dano + (randint(1, (int(Monstro.dano / 2))))
            return dano
    elif acerto == 1:
        erro = 0
        return erro
    else:
        return ("erro total")
    print("FIM")

def curar():
# Monstros Fáceis
monstrosFaceis = [
    Monstro("Goblin", 50, 10, 10, arma("Adaga enferrujada", 8)),
    Monstro("Esqueleto Guerreiro", 60, 18, 12, arma("Espada longa", 8)),
    Monstro("Fantasma", 80, 15, 20),  # Fantasmas não precisam de armas físicas
    Monstro("Lobo Gigante", 70, 20, 18),  # Lobos atacam com garras e presas
    Monstro("Harpia", 100, 22, 25)  # Harpias normalmente atacam com garras
]

# Monstros Moderados
monstrosModerados = [
    Monstro("Orc", 120, 25, 8, arma("Machado de guerra", 17)),
    Monstro("Basilisco", 150, 35, 10),  # Basiliscos usam ataques naturais
    Monstro("Mago Negro", 90, 25, 14, arma("Cajado mágico", 12)),
    Monstro("Quimera", 160, 40, 16),  # Quimeras não usam armas
    Monstro("Beholder", 170, 35, 19)  # Beholders usam ataques mágicos
]

# Monstros Difíceis
monstrosDificeis = [
    Monstro("Troll", 180, 30, 5, arma("Clava", 14)),
    Monstro("Dragão Jovem", 250, 40, 15),  # Dragões usam garras e fogo
    Monstro("Minotauro", 200, 38, 7, arma("Machado duplo", 18)),
    Monstro("Ciclope", 280, 45, 6, arma("Clava", 14)),
    Monstro("Vampiro", 110, 30, 22, arma("Espada cerimonial", 28)),
    Monstro("Golem de Pedra", 220, 28, 3),  # Golems não usam armas
    Monstro("Dragão Adulto", 300, 50, 17),  # Dragões usam ataques naturais
    Monstro("Fênix", 260, 48, 24),  # Fênix usa fogo e asas
    Monstro("Manticora", 190, 42, 13),  # Mantícoras atacam com garras e caudas
    Monstro("Griffo", 130, 32, 20)  # Grifos usam garras e bicos
]

drops_facil = [
    {"nome": "Moeda de cobre", "tipo": "moeda"},
    {"status": cura("Poção de cura leve", 15), "tipo": "cura"},
    {"status": cura("Poção de cura moderada", 45), "tipo": "cura"},
    {"nome": "Erva medicinal", "tipo": "cura"},
    {"nome": "Pedra bruta", "tipo": "mineral"},
    {"nome": "Pedaço de couro", "tipo": "equipamento"},
    {"nome": "Osso de animal", "tipo": "mineral"}
]

drops_moderado = [
    {"nome": "Moeda de prata", "tipo": "moeda"},
    {"status": cura("Poção de cura moderada", 45), "tipo": "cura"},
    {"nome": "Pedra preciosa", "tipo": "mineral"},
    {"nome": "Metal bruto", "tipo": "mineral"},
    {"nome": "Pedaço de pele de animal", "tipo": "equipamento"},
    {"nome": "Osso de criatura", "tipo": "mineral"},
    {"nome": "Armadura de couro média", "tipo": "equipamento"}
]

drops_dificil = [
    {"nome": "Moeda de ouro", "tipo": "moeda"},
    {"status": cura("Poção de cura potente", 75), "tipo": "cura"},
    {"nome": "Gemas preciosas", "tipo": "mineral"},
    {"nome": "Metal raro", "tipo": "mineral"},
    {"status": cura("Poção de cura moderada", 45 ), "tipo": "cura"},
    {"nome": "Osso de monstro", "tipo": "mineral"},
    {"nome": "Armadura de aço", "tipo": "equipamento"}
]

armas = [
    {
        "status": arma("Adaga enferrujada", 8),
        "tipo": "arma"
    },
    {
        "status": arma("Espada longa", 8),
        "tipo": "arma"
    },
    {
        "status": arma("Machado de guerra", 17),
        "tipo": "arma"
    },
    {
        "status": arma("Cajado mágico", 12),
        "tipo": "arma"
    },
    {
        "status": arma("Clava", 14),
        "tipo": "arma"
    },
    {
        "status": arma("Machado duplo", 18),
        "tipo": "arma"
    },
    {
        "status": arma("Espada cerimonial", 24),
        "tipo": "arma"
    }
]

inventário = [{
        "status": arma("Espada Longa", 8),
        "tipo": "arma"
    },
    {
        "status": arma("Arco Composto", 6),
        "tipo": "arma"
    },
    # Equipamentos

    {
        "nome": "Escudo de Batalha",
        "tipo": "equipamento",
        "defesa": 5,
        "propriedades": ["bloqueio"]
    },
    {
        "nome": "Capuz do Ladrão",
        "tipo": "equipamento",

    },
    {
        "nome": "Bota de Velocidade",
        "tipo": "equipamento",

    }
]
trabalhos = [
    {
        "nome": "Atendente de Loja",
        "função": "Auxiliar clientes, organizar produtos e realizar vendas",
        "tempo": 8,
        "dinheiro": "15"
    },
    {
        "nome": "Garçom",
        "função": "Atender os clientes",
        "tempo": 6,
        "dinheiro": "7"
    },
    {
        "nome": "Caçador",
        "função": "Caçar animais ou pessoas (maioria criminosos)",
        "tempo": "Até concluir",
        "dinheiro": "25"
    },
    {
        "nome": "Ajudande de fazenda",
        "função": "Plantar, regar, colher etc.",
        "tempo": 10,
        "dinheiro": "18"
    }
]

# Ferimentos

# Ferimentos Leves
ferimentos_leves = [
    "Arranhão",
    "Contusão leve",
    "Laceração superficial",
    "Torção de dedo",
    "Queimadura de primeiro grau",
    "Machucado no joelho",
    "Dor muscular leve"
]

# Ferimentos Moderados

ferimentos_moderados = [
    "Corte profundo",
    "Fratura na costela",
    "Queimadura de segundo grau",
    "Deslocamento de ombro",
    "Concussão leve",
    "Laceração extensa",
    "Torção de tornozelo",
    "Perfuração muscular",
    "Entorse no pulso",
    "Fratura no dedo",
    "Lesão no ombro",
    "Lesão no braço"
]

# Ferimentos Graves

ferimentos_graves = [
    "Fratura exposta",
    "Concussão severa",
    "Queimadura de terceiro grau",
    "Hemorragia externa",
    "Fratura múltipla",
]

# Ferimentos Críticos

ferimentos_criticos = [
    "Amputação de membro",
    "Dano cerebral grave",
    "Hemorragia interna massiva",
    "Perfuração de órgão vital",
    "Parada cardíaca",
    "Lesão cerebral traumática",
    "Fratura de crânio",
    "Perda de membro por necrose",
    "Lesão medular completa",
    "Falha respiratória devido a lesões",
    "Perfuração no abdômen",
    "Lesão na coluna vertebral"    
]

# Ferimentos especiais

ferimentos_especiais = [
    "Perda de visão temporária",
    "Dano pulmonar",
]
