# Diretório de funções

def linha(tam=10):
    if tam == 0:
        tam = 10
    return print("\033[1;37m-\033[m" * tam)

def linhas(tam=0):
    if tam != 0:
        tam = tam - 1
    return print(("\n" * tam))

def processando(tempo=1):
    import time
    if tempo == 0:
        tempo = 1
    time.sleep(tempo / 2)
    print("Processando", end="", flush=True)
    time.sleep(tempo / 4)
    print(".", end="", flush=True)
    time.sleep(tempo / 4)
    print(".", end="", flush=True)
    time.sleep(tempo / 4)
    print(".", flush=True)
