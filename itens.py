class Monstro:
    def __init__(self, nome, vida, dano, destreza):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.destreza = destreza

    def __str__(self):
        return f"{self.nome}: Vida {self.vida}, Dano {self.dano}, Destreza {self.destreza}"


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
        "encantamento": "Fogo"
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
    }
]

trabalhos = [
    {
        "nome": "Atendente de Loja",
        "função": "Auxiliar clientes, organizar produtos e realizar vendas",
        "tempo": "8",
        "dinheiro": "15"
    },
    {
        "nome": "Garçom",
        "função": "Atender os clientes",
        "tempo": "6",
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
        "tempo": "10",
        "dinheiro": "18"
    }
]
