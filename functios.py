import math

def multiplicar(x, y):
    return x * y

def logaritmo(x, base=10):
    """Calcula logaritmo de x na base especificada"""
    try:
        if x <= 0:
            return "Erro"
        return math.log(x, base)
    except:
        return "Erro"

def deletar(entrada: str):
    """Remove o último caractere da string da tela"""
    return entrada[:-1] if entrada else ""

def fechar_programa(root):
    """Fecha o programa"""
    root.quit()

# Variável global para a tela
entrada_tela = ""

def atualizar_tela(label, texto):
    """Atualiza o texto na tela"""
    global entrada_tela
    entrada_tela = texto
    label.config(text=texto)

def adicionar_numero(label, numero):
    """Adiciona um número à tela"""
    entrada_atual = label.cget("text")
    if entrada_atual == "0":
        atualizar_tela(label, str(numero))
    else:
        atualizar_tela(label, entrada_atual + str(numero))

def limpar_tela(label):
    """Limpa a tela (função AC)"""
    atualizar_tela(label, "0")
