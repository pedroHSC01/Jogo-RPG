class Monstro:
    def __init__(self, nome, vida, dano, destreza):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.destreza = destreza

    def __str__(self):
        return f"{self.nome}: Vida {self.vida}, Dano {self.dano}, Destreza {self.destreza}"

# Sistema de combate

class personagem():
    def __init__(self, nome, dano, vida, destreza):
        self.nome = nome
        self.dano = dano
        self.vida = vida
        self.destreza = destreza
    def __str__(self):
        return f"Nome: {self.nome}\nDano: {self.dano}\nVida: {self.vida}\nDestreza: {self.destreza}"

personagens = [
    ["Alrindel", 15, 13, 25],
    ["Baruk", 20, 20, 7],
    ["Gideon", 35, 26, 8],
    ["Lyra", 9, 8, 16],
    ["Valeria", 15, 27, 19],
]
personage = [
    personagem("Alrindel", 15, 13, 25),
    personagem("Baruk", 20, 20, 7),
    personagem("Gideon", 35, 26, 8),
    personagem("Lyra", 9, 8, 16),
    personagem("Valeria", 15, 27, 19)
]

def combate():
    player_status = [
        {
            "pdano": personagem.dano,
            "pvida": personagem.vida,
            "pdest": personagem.destreza
        }
    ]
    monstro_status = [
        {
            "mdano": Monstro.dano,
            "mvida": Monstro.vida,
            "mdest": Monstro.destreza
        }
    ]


# Monstros Fáceis

monstrosFaceis = [
    Monstro("Goblin", 50, 10, 10),
    Monstro("Esqueleto Guerreiro", 60, 18, 12),
    Monstro("Fantasma", 80, 15, 20),
    Monstro("Lobo Gigante", 70, 20, 18),
    Monstro("Harpia", 100, 22, 25)
]

# Monstros Moderados

monstrosModerados = [
    Monstro("Orc", 120, 25, 8),
    Monstro("Basilisco", 150, 35, 10),
    Monstro("Mago Negro", 90, 25, 14),
    Monstro("Quimera", 160, 40, 16),
    Monstro("Beholder", 170, 35, 19)
]

# Monstros Difíceis

monstrosDificeis = [
    Monstro("Troll", 180, 30, 5),
    Monstro("Dragão Jovem", 250, 40, 15),
    Monstro("Minotauro", 200, 38, 7),
    Monstro("Ciclope", 280, 45, 6),
    Monstro("Vampiro", 110, 30, 22),
    Monstro("Golem de Pedra", 220, 28, 3),
    Monstro("Dragão Adulto", 300, 50, 17),
    Monstro("Fênix", 260, 48, 24),
    Monstro("Manticora", 190, 42, 13),
    Monstro("Griffo", 130, 32, 20)
]

inventário = [
    # Armas

    {
        "nome": "Espada Longa",
        "tipo": "arma",
        "dano": 8,
        "propriedades": ["cortante", "perfurante"],
        "encantamento": "Fogo",
    },
    {
        "nome": "Arco Composto",
        "tipo": "arma",
        "dano": 6,
        "alcance": "longo",
        "propriedades": ["perfurante"],
        "munição": "Flechas"
    },
    
    # Equipamentos

    {
        "nome": "Escudo de Batalha",
        "tipo": "equipamento",
        "defesa": 5,
        "material": "metal",
        "propriedades": ["bloqueio", "resistência a impacto"]
    },
    {
        "nome": "Capuz do Ladrão",
        "tipo": "equipamento",
        "bonus": "furtividade +2",
        "propriedades": ["camuflagem"]
    },
    {
        "nome": "Bota de Velocidade",
        "tipo": "equipamento",
        "bonus": "velocidade +3",
        "propriedades": ["agilidade"]
    },

    # Curas

    {
        "nome": "poção de cura 20",
        "tipo": "cura",
        "bonus": "recupera 20 de vida",
    },
    {
        "nome": "poção de cura 100",
        "tipo": "cura",
        "bonus": "recupera 100 de vida",
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
