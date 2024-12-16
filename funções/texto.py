# Diretório de funções

def linha(tam=10):
    if tam == 0:
        tam = 10
    return ("\033[1;37m-\033[m" * tam)
    