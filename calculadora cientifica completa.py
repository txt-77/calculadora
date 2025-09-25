from tkinter import *
from tkinter import font, messagebox, simpledialog
import math
import random
import functios
from fractions import Fraction
import locale
import re

# Configuraçoes globais
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Variaveis globais
ultimo_resultado = None
shift_active = False
alpha_active = False
hyp_mode = False

# Funçoes principais
def atualizar_tela(label, texto):
    label.config(text=texto)

def deletar(entrada):
    return entrada[:-1]

def fechar_programa(root):
    root.quit()

def adicionar_numero(tela, numero):
    entrada_atual = tela.cget("text")
    if entrada_atual == "0":
        atualizar_tela(tela, str(numero))
    else:
        atualizar_tela(tela, entrada_atual + str(numero))

def logaritmo(numero):
    return math.log10(numero)

# Funcoes dos botoes do feito pelo grupo

def botao_ans():
    entrada_atual = tela.cget("text")
    global ultimo_resultado
    if shift_active:
            return
     
    elif ultimo_resultado is not None:
        
            if entrada_atual and entrada_atual[-1] in ["+", "-", "×", "÷"]:
                atualizar_tela(tela, entrada_atual + str(ultimo_resultado))
            elif entrada_atual == "0":
                atualizar_tela(tela, str(ultimo_resultado))
            else:
                atualizar_tela(tela, entrada_atual + "×" + str(ultimo_resultado))

def botao_log():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            resultado = functios.logaritmo(numero)
            functios.atualizar_tela(tela, str(resultado))
        except:
            functios.atualizar_tela(tela, "Erro")

def botao_cos():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                resultado = math.degrees(math.acos(numero))
            elif hyp_mode:
                resultado = math.cosh(numero)
            else:
                resultado = math.cos(math.radians(numero))
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")


def botao_pol():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            magnitude = abs(numero)
            fase = math.degrees(math.atan(numero))
            resultado = f"{magnitude}∠{fase}°"
            functios.atualizar_tela(tela, resultado)
        except:
            functios.atualizar_tela(tela, "Erro")

def botao_del():
    entrada = tela.cget("text")
    nova_entrada = deletar(entrada)
    if not nova_entrada:
        nova_entrada = "0"
    atualizar_tela(tela, nova_entrada)

# Funcoes basicas 

def botao_x():
    fechar_programa(root)

def botao_numero(numero):
    adicionar_numero(tela, numero)

def botao_ponto():
    entrada_atual = tela.cget("text")
    if "." not in entrada_atual:
        if entrada_atual == "0":
            atualizar_tela(tela, "0.")
        else:
            atualizar_tela(tela, entrada_atual + ".")

def botao_multiplicar():
    entrada_atual = tela.cget("text")
    if entrada_atual and not entrada_atual.endswith("×"):
        atualizar_tela(tela, entrada_atual + "×")

def botao_igual():
    global ultimo_resultado
    entrada_atual = tela.cget("text")
    try:
        expressao = entrada_atual.replace("×", "*").replace("÷", "/")
        resultado = eval(expressao)
        atualizar_tela(tela, str(resultado))
        ultimo_resultado = resultado
    except:
        atualizar_tela(tela, "Erro")

def botao_somar():
    entrada_atual = tela.cget("text")
    if entrada_atual and not entrada_atual.endswith("+"):
        atualizar_tela(tela, entrada_atual + "+")

def botao_subtrair():
    entrada_atual = tela.cget("text")
    if entrada_atual and not entrada_atual.endswith("-"):
        atualizar_tela(tela, entrada_atual + "-")

def botao_dividir():
    entrada_atual = tela.cget("text")
    if entrada_atual and not entrada_atual.endswith("÷"):
        atualizar_tela(tela, entrada_atual + "÷")

def botao_ac():
    atualizar_tela(tela, "0")

# funcoes de feitas por outros grupos

def botao_sin():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                resultado = math.degrees(math.asin(numero))
            elif hyp_mode:
                resultado = math.sinh(numero)
            else:
                resultado = math.sin(math.radians(numero))
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_tan():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                resultado = math.degrees(math.atan(numero))
            elif hyp_mode:
                resultado = math.tanh(numero)
            else:
                resultado = math.tan(math.radians(numero))
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_ln():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                resultado = math.e ** numero
            else:
                resultado = math.log(numero)
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_shift():
    global shift_active
    shift_active = not shift_active
    atualizar_botoes_shift()

def botao_alpha():
    global alpha_active
    alpha_active = not alpha_active
    atualizar_botoes_alpha()

def botao_hyp():
    global hyp_mode
    hyp_mode = not hyp_mode

def botao_x2():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            resultado = numero ** 2
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_x3():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                resultado = numero ** (1/3)
            else:
                resultado = numero ** 3
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_sqrt():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            resultado = math.sqrt(numero)
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_inverso():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            if shift_active:
                if numero < 0 or not numero.is_integer():
                    atualizar_tela(tela, "Erro")
                else:
                    resultado = math.factorial(int(numero))
                    atualizar_tela(tela, str(resultado))
            else:
                if numero == 0:
                    atualizar_tela(tela, "Erro")
                else:
                    resultado = 1 / numero
                    atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_exp():
    entrada_atual = tela.cget("text")
    atualizar_tela(tela, entrada_atual + "×10**(")

def botao_pi():
    atualizar_tela(tela, str(math.pi))

def botao_fracao():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            fracao = Fraction(numero).limit_denominator()
            atualizar_tela(tela, f"{fracao.numerator}/{fracao.denominator}")
        except:
            atualizar_tela(tela, "Erro")

def botao_nCr():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            if "," in entrada:
                n_str, r_str = entrada.split(",")
            else:
                partes = entrada.split()
                n_str, r_str = partes[0], partes[1] if len(partes) > 1 else "0"
            
            n = int(float(n_str))
            r = int(float(r_str))
            
            if r > n or n < 0 or r < 0:
                atualizar_tela(tela, "Erro: 0 ≤ r ≤ n")
            else:
                resultado = math.comb(n, r)
                atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_porcentagem():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            numero = float(entrada)
            resultado = numero / 100
            atualizar_tela(tela, str(resultado))
        except:
            atualizar_tela(tela, "Erro")

def botao_dms():
    entrada = tela.cget("text")
    if entrada and entrada != "0":
        try:
            if '°' in entrada or "'" in entrada:
                nums = re.findall(r'[-]?\d+(?:\.\d+)?', entrada)
                if len(nums) >= 3:
                    g = int(float(nums[0]))
                    m = int(float(nums[1]))
                    s = float(nums[2])
                    dec = g + (m / 60) + (s / 3600)
                    if g < 0:
                        dec *= -1
                    atualizar_tela(tela, str(round(dec, 6)))
                else:
                    atualizar_tela(tela, "Erro")
            else:
                val = float(entrada)
                sinal = -1 if val < 0 else 1
                val = abs(val)
                graus = int(val)
                minutos = int((val - graus) * 60)
                segundos = round(((val - graus) * 60 - minutos) * 60, 2)
                dms_str = f"{graus * sinal}° {minutos}' {segundos}\""
                atualizar_tela(tela, dms_str)
        except:
            atualizar_tela(tela, "Erro")

def atualizar_botoes_shift():
    if shift_active:
        btnSin.config(text="sin⁻¹")
        btnCos.config(text="cos⁻¹")
        btnTan.config(text="tan⁻¹")
        btnLog.config(text="10^x")
        btnLn.config(text="e^x")
        btnCube.config(text="³√")
        btnInverse.config(text="x!")
    else:
        btnSin.config(text="sin")
        btnCos.config(text="cos")
        btnTan.config(text="tan")
        btnLog.config(text="log")
        btnLn.config(text="ln")
        btnCube.config(text="x³")
        btnInverse.config(text="x⁻¹")

def atualizar_botoes_alpha():
    # Função para atualizar botões quando ALPHA está ativo
    pass

# Tela principal
root = Tk()
root.title("Calculadora Científica")

# Fontes
fontBotao = font.Font(family="Arial", size=9, weight="bold")
fontMini = font.Font(family="Arial", size=8, slant="italic")
fontLabel = font.Font(family="Arial", size=15)

tela = Label(height=2, borderwidth=0.5, relief="solid", anchor="e", background="White", font=fontLabel, text="0", width=21)
tela.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="ew")

frame6 = Frame(root)
frame6.grid(row=1, column=0, columnspan=6)

frame5 = Frame(root)
frame5.grid(row=2, column=0, columnspan=6, sticky="ew")

# Linha 1: SHIFT, ALPHA, REPLAY, MODE, X
Button(frame6, text="SHIFT", width=4, height=1, font=fontBotao, fg="orange", 
       command=botao_shift).grid(row=1, column=0, pady=1, padx=3)
Button(frame6, text="ALPHA", width=4, height=1, font=fontBotao, fg="red", 
       command=botao_alpha).grid(row=1, column=1, pady=1, padx=3)
Button(frame6, text="MODE", width=4, height=1, font=fontBotao).grid(row=1, column=4, pady=1, padx=3)
Button(frame6, text="X", width=4, height=1, font=fontBotao, bg="red", fg="white", 
       command=botao_x).grid(row=1, column=5, pady=1, padx=3)

# SETAS DO REPLAY
Button(frame6, text="↑", width=4, height=1, font=fontBotao).grid(row=1, column=2, columnspan=2, pady=1, sticky="s")
Button(frame6, text="←", width=3, height=1, font=fontBotao).grid(row=2, column=2, padx=3)
Button(frame6, text="→", width=3, height=1, font=fontBotao).grid(row=2, column=3, padx=3)
Button(frame6, text="↓", width=4, height=1, font=fontBotao).grid(row=3, column=2, columnspan=2, pady=1)

# Linha 2: x^-1, nCr, Pol, Rec, x³, x^y 
Label(frame6, text="x!", fg="orange", font=fontMini).grid(row=2, column=0, sticky="s", pady=1)
btnInverse = Button(frame6, text="x⁻¹", width=3, height=1, font=fontBotao, command=botao_inverso)
btnInverse.grid(row=3, column=0, sticky="s", pady=1)

Label(frame6, text="nPr", fg="orange", font=fontMini).grid(row=2, column=1, sticky="s", pady=1)
Button(frame6, text="nCr", width=3, height=1, font=fontBotao, command=botao_nCr).grid(row=3, column=1, sticky="s", pady=1)

Label(frame6, text="Rec(", fg="orange", font=fontMini).grid(row=2, column=4, sticky="sw",pady=1)
Label(frame6, text=":", fg="red", font=fontMini).grid(row=3, column=4, sticky="se",pady=1)
Button(frame6, text="Pol(", width=3, height=1, font=fontBotao,command=lambda: botao_pol).grid(row=3, column=4, sticky="s" ,pady=1)

Label(frame6, text="³√x", fg="orange", font=fontMini).grid(row=2, column=5, sticky="s", pady=1)
btnCube = Button(frame6, text="x³", width=3, height=1, font=fontBotao, command=botao_x3)
btnCube.grid(row=3, column=5, sticky="s", pady=1)

# Linha 3: ab/c, x², √, log, ln, ^
Label(frame6, text="d/c", fg="orange", font=fontMini).grid(row=4, column=0, sticky="s", pady=1)
Button(frame6, text="a b/c", width=3, height=1, font=fontBotao, command=botao_fracao).grid(row=5, column=0, sticky="s", pady=1)

Label(frame6, text="∛x", fg="orange", font=fontMini).grid(row=4, column=1, sticky="s", pady=1)
Button(frame6, text="√", width=3, height=1, font=fontBotao, command=botao_sqrt).grid(row=5, column=1, sticky="s", pady=1)

Label(frame6, text="x√y", fg="orange", font=fontMini).grid(row=4, column=2, sticky="s", pady=1)
Button(frame6, text="x²", width=3, height=1, font=fontBotao, command=botao_x2).grid(row=5, column=2, sticky="s", pady=1)

Label(frame6, text="10^x", fg="orange", font=fontMini).grid(row=4, column=3, sticky="s", pady=1)
Button(frame6, text="^", width=3, height=1, font=fontBotao).grid(row=5, column=3, sticky="s", pady=1)

Label(frame6, text="10^x", fg="orange", font=fontMini).grid(row=4, column=4, sticky="s", pady=1)
btnLog = Button(frame6, text="log", width=3, height=1, font=fontBotao, command=botao_log)
btnLog.grid(row=5, column=4, sticky="s", pady=1)

Label(frame6, text="e^x", fg="orange", font=fontMini).grid(row=4, column=5, sticky="sw", pady=1)
Label(frame6, text="e", fg="red", font=fontMini).grid(row=4, column=5, sticky="se", pady=1)
btnLn = Button(frame6, text="In", width=3, height=1, font=fontBotao, command=botao_ln)
btnLn.grid(row=5, column=5, sticky="s", pady=1)

# Linha 4: hyp, sin, cos, tan, °, ,,
Label(frame6, text="A", fg="red", font=fontMini).grid(row=6, column=0, sticky="se", pady=1)
Button(frame6, text="(-)", width=3, height=1, font=fontBotao).grid(row=7, column=0, sticky="s", pady=1)

Label(frame6, text="B", fg="red", font=fontMini).grid(row=6, column=1, sticky="se", pady=1)
Label(frame6, text="←", fg="orange", font=fontMini).grid(row=6, column=1, sticky="sw", pady=1)
Button(frame6, text="°, ,,", width=3, height=1, font=fontBotao).grid(row=7, column=1, sticky="s", pady=1)

Label(frame6, text="C", fg="red", font=fontMini).grid(row=6, column=2, sticky="se", pady=1)
Button(frame6, text="hyp", width=3, height=1, font=fontBotao, command=botao_hyp).grid(row=7, column=2, sticky="s", pady=1)

Label(frame6, text="D", fg="red", font=fontMini).grid(row=6, column=3, sticky="se", pady=1)
Label(frame6, text="sin⁻¹", fg="orange", font=fontMini).grid(row=6, column=3, sticky="sw", pady=1)
btnSin = Button(frame6, text="sin", width=3, height=1, font=fontBotao, command=botao_sin)
btnSin.grid(row=7, column=3, sticky="s", pady=1)


Label(frame6, text="E", fg="red", font=fontMini).grid(row=6, column=4, sticky="se" ,pady=1)
Label(frame6, text="cos⁻¹", fg="orange", font=fontMini).grid(row=6, column=4, sticky="sw" ,pady=1)
btnCos = Button(frame6, text="cos", width=3, height=1, font=fontBotao,command=botao_cos)
btnCos.grid(row=7, column=4, pady=1)

Label(frame6, text="F", fg="red", font=fontMini).grid(row=6, column=5, sticky="se", pady=1)
Label(frame6, text="tan⁻¹", fg="orange", font=fontMini).grid(row=6, column=5, sticky="sw", pady=1)
btnTan = Button(frame6, text="tan", width=3, height=1, font=fontBotao, command=botao_tan)
btnTan.grid(row=7, column=5, pady=1)

# Linha 5: RCL, ENG, (, ), M+
Label(frame6, text="STO", fg="orange", font=fontMini).grid(row=8, column=0, sticky="s", pady=1)
Button(frame6, text="RCL", width=3, height=1, font=fontBotao).grid(row=9, column=0, sticky="s", pady=1)

Label(frame6, text="←", fg="orange", font=fontMini).grid(row=8, column=1, sticky="s", pady=1)
Button(frame6, text="ENG", width=3, height=1, font=fontBotao).grid(row=9, column=1, sticky="s", pady=1)

Button(frame6, text="(", width=3, height=1, font=fontBotao).grid(row=9, column=2, sticky="s", pady=1)

Label(frame6, text="X", fg="red", font=fontMini).grid(row=8, column=3, sticky="se", pady=1)
Button(frame6, text=")", width=3, height=1, font=fontBotao).grid(row=9, column=3, pady=1)

Label(frame6, text="Y", fg="red", font=fontMini).grid(row=8, column=4, sticky="se", pady=1)
Label(frame6, text=";", fg="orange", font=fontMini).grid(row=8, column=4, sticky="sw", pady=1)
Button(frame6, text=",", width=3, height=1, font=fontBotao).grid(row=9, column=4, pady=1)

Label(frame6, text="M", fg="red", font=fontMini).grid(row=8, column=3, sticky="se", pady=1)
Label(frame6, text="M-", fg="orange", font=fontMini).grid(row=8, column=3, sticky="sw", pady=1)
Button(frame6, text="M+", width=3, height=1, font=fontBotao).grid(row=9, column=5, pady=1)

# Linha 6: 7 8 9 DEL AC 
Button(frame5, text="7", width=5, height=2, font=fontBotao, command=lambda: botao_numero(7)).grid(row=11, column=0, padx=2, pady=2, sticky="s")
Button(frame5, text="8", width=5, height=2, font=fontBotao, command=lambda: botao_numero(8)).grid(row=11, column=1, padx=2, pady=2, sticky="s")
Button(frame5, text="9", width=5, height=2, font=fontBotao, command=lambda: botao_numero(9)).grid(row=11, column=2, padx=2, pady=2, sticky="s")

Label(frame5, text="INS", fg="orange", font=fontMini).grid(row=10, column=3, sticky="s", padx=2, pady=2)
Button(frame5, text="DEL", width=5, height=2, font=fontBotao, bg="red", fg="white", command=botao_del).grid(row=11, column=3, padx=2, pady=2, sticky="s")

Button(frame5, text="AC", width=5, height=2, font=fontBotao, bg="red", fg="white", command=botao_ac).grid(row=11, column=4, padx=2, pady=2, sticky="s")

# Linha 7: 4 5 6 × ÷ 
Label(frame5, text=" ").grid(row=12, column=0, sticky="s", padx=2, pady=2)
Button(frame5, text="4", width=5, height=2, font=fontBotao, command=lambda: botao_numero(4)).grid(row=13, column=0, padx=2, pady=2)
Button(frame5, text="5", width=5, height=2, font=fontBotao, command=lambda: botao_numero(5)).grid(row=13, column=1, padx=2, pady=2)
Button(frame5, text="6", width=5, height=2, font=fontBotao, command=lambda: botao_numero(6)).grid(row=13, column=2, padx=2, pady=2)
Button(frame5, text="×", width=5, height=2, font=fontBotao, command=botao_multiplicar).grid(row=13, column=3, padx=2, pady=2)
Button(frame5, text="÷", width=5, height=2, font=fontBotao, command=botao_dividir).grid(row=13, column=4, padx=2, pady=2)

# Linha 8: 1 2 3 - + 
Label(frame5, text="S-SUM", fg="orange", font=fontMini).grid(row=14, column=0, sticky="s", padx=2, pady=2)
Button(frame5, text="1", width=5, height=2, font=fontBotao, command=lambda: botao_numero(1)).grid(row=15, column=0, sticky="s", padx=2, pady=2)

Label(frame5, text="S-VAR", fg="orange", font=fontMini).grid(row=14, column=1, sticky="s", padx=2, pady=2)
Button(frame5, text="2", width=5, height=2, font=fontBotao, command=lambda: botao_numero(2)).grid(row=15, column=1, sticky="s", padx=2, pady=2)

Button(frame5, text="3", width=5, height=2, font=fontBotao, command=lambda: botao_numero(3)).grid(row=15, column=2, sticky="s", padx=2, pady=2)
Button(frame5, text="-", width=5, height=2, font=fontBotao, command=botao_subtrair).grid(row=15, column=3, sticky="s", padx=2, pady=2)
Button(frame5, text="+", width=5, height=2, font=fontBotao, command=botao_somar).grid(row=15, column=4, sticky="s", padx=2, pady=2)

# Linha 9: 0 . EXP Ans = 
Label(frame5, text="Rnd", fg="orange", font=fontMini).grid(row=16, column=0, sticky="s", padx=2, pady=2)
Button(frame5, text="0", width=5, height=2, font=fontBotao, command=lambda: botao_numero(0)).grid(row=17, column=0, padx=2, pady=2, sticky="s")

Label(frame5, text="Ran#", fg="orange", font=fontMini).grid(row=16, column=1, sticky="s", padx=2, pady=2)
Button(frame5, text=".", width=5, height=2, font=fontBotao, command=botao_ponto).grid(row=17, column=1, padx=2, pady=2, sticky="s")

Label(frame5, text="π", fg="orange", font=fontMini).grid(row=16, column=2, sticky="s", padx=2, pady=2)
Button(frame5, text="EXP", width=5, height=2, font=fontBotao, command=botao_exp).grid(row=17, column=2, padx=2, pady=2, sticky="s")

Label(frame5, text="DRG►", fg="orange", font=fontMini).grid(row=16, column=3, sticky="s", padx=2, pady=2)
Button(frame5, text="Ans", width=5, height=2, font=fontBotao,command=botao_ans).grid(row=17, column=3, sticky="s", padx=2, pady=2)

Label(frame5, text="%", fg="orange", font=fontMini).grid(row=16, column=4, sticky="s", padx=2, pady=2)
Button(frame5, text="=", width=5, height=2, font=fontBotao, command=botao_igual).grid(row=17, column=4, sticky="s", padx=2, pady=2)


root.mainloop()

