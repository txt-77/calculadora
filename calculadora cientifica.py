from tkinter import *
from tkinter import font

root = Tk()
root.title("calculadora cientifica")

# Fontes
fontBotao = font.Font(family="Arial", size=9, weight="bold")
fontMini = font.Font(family="Arial", size=8, slant="italic")
fontLabel = font.Font(family="Arial", size=15)

Label(height=2,borderwidth=0.5,relief="solid",anchor="e",background="White",font=fontLabel).grid(row=0,column=0,columnspan=6,padx=5,pady=5,sticky="ew")
#  Linha 1: SHIFT , ALPHA , REPLAY , MODE , CLR 
Button( text="SHIFT", width=4, height=1, font=fontBotao, fg="orange").grid(row=1, column=0 ,pady=1)
Button( text="ALPHA", width=4, height=1, font=fontBotao, fg="red").grid(row=1, column=1 ,pady=1)
Button( text="MODE", width=4, height=1, font=fontBotao).grid(row=1, column=4 ,pady=1)

#  SETAS DO REPLAY

Button(text="↑", width=4, height=1, font=fontBotao).grid(row=1, column=2,columnspan=2, pady=1,sticky="s")
Button(text="←", width=3, height=1, font=fontBotao).grid(row=2, column=2)
Button(text="→", width=3, height=1, font=fontBotao).grid(row=2, column=3)
Button(text="↓", width=4, height=1, font=fontBotao).grid(row=3, column=2,columnspan=2, pady=1 )

#  Linha 2: x^-1 , nCr , Pol , Rec , x³ , x^y 
Label( text="x!", fg="orange", font=fontMini).grid(row=2, column=0, sticky="s",pady=1)
Button( text="x⁻¹", width=3, height=1, font=fontBotao).grid(row=3, column=0, sticky="s" ,pady=1)

Label( text="nPr", fg="orange", font=fontMini).grid(row=2, column=1, sticky="s" ,pady=1)
Button( text="nCr", width=3, height=1, font=fontBotao).grid(row=3, column=1, sticky="s" ,pady=1)

Label( text="Rec(", fg="orange", font=fontMini).grid(row=2, column=4, sticky="sw",pady=1)
Label( text=":", fg="red", font=fontMini).grid(row=3, column=4, sticky="se",pady=1)
Button( text="Pol(", width=3, height=1, font=fontBotao).grid(row=3, column=4, sticky="s" ,pady=1)

Label( text="³√x", fg="orange", font=fontMini).grid(row=2, column=5, sticky="s" ,pady=1)
Button( text="x³", width=3, height=1, font=fontBotao).grid(row=3, column=5, sticky="s" ,pady=1)

#  Linha 3: ab,c , x² , √ , log , ln , ^
Label( text="d/c", fg="orange", font=fontMini).grid(row=4, column=0, sticky="s",pady=1)
Button( text="a b/c", width=3, height=1, font=fontBotao).grid(row=5, column=0, sticky="s",pady=1)

Label( text="∛x", fg="orange", font=fontMini).grid(row=4, column=1, sticky="s" ,pady=1)
Button( text="√", width=3, height=1, font=fontBotao).grid(row=5, column=1, sticky="s",pady=1)

Label( text="x√y", fg="orange", font=fontMini).grid(row=4, column=2, sticky="s",pady=1)
Button( text="x²", width=3, height=1, font=fontBotao).grid(row=5, column=2, sticky="s",pady=1)

Label( text="10^x", fg="orange", font=fontMini).grid(row=4, column=3, sticky="s" ,pady=1)
Button( text="^", width=3, height=1, font=fontBotao).grid(row=5, column=3, sticky="s" ,pady=1)

Label( text="10^x", fg="orange", font=fontMini).grid(row=4, column=3, sticky="s" ,pady=1)
Button( text="log", width=3, height=1, font=fontBotao).grid(row=5, column=4, sticky="s" ,pady=1)

Label( text="e^x", fg="orange", font=fontMini).grid(row=4, column=4, sticky="sw" ,pady=1)
Label( text="e", fg="red", font=fontMini).grid(row=4, column=3, sticky="se" ,pady=1)
Button( text="In", width=3, height=1, font=fontBotao).grid(row=5, column=5, sticky="s" ,pady=1)

#  Linha 4: hyp , sin , cos , tan , RCL , ENG 
Label( text="A", fg="red", font=fontMini).grid(row=6, column=0, sticky="se" ,pady=1)
Button( text="(-)", width=3, height=1, font=fontBotao).grid(row=7, column=0, sticky="s" ,pady=1)

Label( text="B", fg="red", font=fontMini).grid(row=6, column=1, sticky="se" ,pady=1)
Label( text="←", fg="orange", font=fontMini).grid(row=6, column=1, sticky="sw" ,pady=1)
Button( text="sin", width=3, height=1, font=fontBotao).grid(row=7, column=1, sticky="s" ,pady=1)

Label( text="C", fg="red", font=fontMini).grid(row=6, column=2, sticky="se" ,pady=1)
Button( text="hyp", width=3, height=1, font=fontBotao).grid(row=7, column=2, sticky="s" ,pady=1)

Label( text="D", fg="red", font=fontMini).grid(row=6, column=3, sticky="se" ,pady=1)
Label( text="sin⁻¹", fg="orange", font=fontMini).grid(row=6, column=3, sticky="sw" ,pady=1)
Button( text="sin", width=3, height=1, font=fontBotao).grid(row=7, column=3, pady=1)

Label( text="E", fg="red", font=fontMini).grid(row=6, column=4, sticky="se" ,pady=1)
Label( text="cos⁻¹", fg="orange", font=fontMini).grid(row=6, column=4, sticky="sw" ,pady=1)
Button( text="cos", width=3, height=1, font=fontBotao).grid(row=7, column=4, pady=1)

Label( text="F", fg="red", font=fontMini).grid(row=6, column=5, sticky="se" ,pady=1)
Label( text="tan⁻¹", fg="orange", font=fontMini).grid(row=6, column=5, sticky="sw" ,pady=1)
Button( text="tan", width=3, height=1, font=fontBotao).grid(row=7, column=5, pady=1)

#  Linha 5: RCL , ENG , ( , ) , M+
Label( text="STO", fg="orange", font=fontMini).grid(row=8, column=0, sticky="s" ,pady=1)
Button( text="RCL", width=3, height=1, font=fontBotao).grid(row=9, column=0, sticky="s" ,pady=1)

Label( text="←", fg="orange", font=fontMini).grid(row=8, column=1, sticky="s" ,pady=1)
Button( text="ENG", width=3, height=1, font=fontBotao).grid(row=9, column=1, sticky="s" ,pady=1)

Button( text="(", width=3, height=1, font=fontBotao).grid(row=9, column=2, sticky="s" ,pady=1)

Label( text="X", fg="red", font=fontMini).grid(row=8, column=3, sticky="se" ,pady=1)
Button( text=")", width=3, height=1, font=fontBotao).grid(row=9, column=3, pady=1)

Label( text="Y", fg="red", font=fontMini).grid(row=8, column=4, sticky="se" ,pady=1)
Label( text=";", fg="orange", font=fontMini).grid(row=8, column=4, sticky="sw" ,pady=1)
Button( text=",", width=3, height=1, font=fontBotao).grid(row=9, column=4, pady=1)

Label( text="M", fg="red", font=fontMini).grid(row=8, column=3, sticky="se" ,pady=1)
Label( text="M-", fg="orange", font=fontMini).grid(row=8, column=3, sticky="sw" ,pady=1)
Button( text="M+", width=3, height=1, font=fontBotao).grid(row=9, column=5, pady=1)

#  Linha 6: 7 8 9 DEL AC 
Button( text="7", width=5, height=2, font=fontBotao).grid(row=11, column=0, padx=2, pady=2, sticky="s")
Button( text="8", width=5, height=2, font=fontBotao).grid(row=11, column=1, padx=2, pady=2, sticky="s")
Button( text="9", width=5, height=2, font=fontBotao).grid(row=11, column=2, padx=2, pady=2, sticky="s")

Label( text="INS", fg="orange", font=fontMini).grid(row=10, column=3, sticky="s", padx=2, pady=2)
Button( text="DEL", width=5, height=2, font=fontBotao, bg="red", fg="white").grid(row=11, column=3, padx=2, pady=2, sticky="s")

Button( text="AC", width=5, height=2, font=fontBotao, bg="red", fg="white").grid(row=11, column=4, padx=2, pady=2, sticky="s")

#  Linha 7: 4 5 6 × ÷ 

Label( text=" ").grid(row=12, column=0, sticky="s", padx=2, pady=2)
Button( text="4", width=5, height=2, font=fontBotao).grid(row=13, column=0, padx=2, pady=2)
Button( text="5", width=5, height=2, font=fontBotao).grid(row=13, column=1, padx=2, pady=2)
Button( text="6", width=5, height=2, font=fontBotao).grid(row=13, column=2,padx=2, pady=2)
Button( text="×", width=5, height=2, font=fontBotao).grid(row=13, column=3,padx=2, pady=2)
Button( text="÷", width=5, height=2, font=fontBotao).grid(row=13, column=4, padx=2, pady=2)

#  Linha 8: 1 2 3 - + 
Label( text="S-SUM", fg="orange", font=fontMini).grid(row=14, column=0, sticky="s", padx=2, pady=2)
Button( text="1", width=5, height=2, font=fontBotao).grid(row=15, column=0, sticky="s", padx=2, pady=2)

Label( text="S-VAR", fg="orange", font=fontMini).grid(row=14, column=1, sticky="s", padx=2, pady=2)
Button( text="2", width=5, height=2, font=fontBotao).grid(row=15, column=1, sticky="s", padx=2, pady=2)

Button( text="3", width=5, height=2, font=fontBotao).grid(row=15, column=2, sticky="s", padx=2, pady=2)
Button( text="-", width=5, height=2, font=fontBotao).grid(row=15, column=3, sticky="s", padx=2, pady=2)
Button( text="+", width=5, height=2, font=fontBotao).grid(row=15, column=4, sticky="s", padx=2, pady=2)

#  Linha 9: 0 . EXP Ans = 
Label( text="Rnd", fg="orange", font=fontMini).grid(row=16, column=0, sticky="s", padx=2, pady=2)
Button( text="0", width=5, height=2, font=fontBotao).grid(row=17, column=0, padx=2, pady=2, sticky="s")

Label( text="Ran#", fg="orange", font=fontMini).grid(row=16, column=1, sticky="s", padx=2, pady=2)
Button( text=".", width=5, height=2, font=fontBotao).grid(row=17, column=1, padx=2, pady=2, sticky="s")

Label( text="π", fg="orange", font=fontMini).grid(row=16, column=2, sticky="s", padx=2, pady=2)
Button( text="EXP", width=5, height=2, font=fontBotao).grid(row=17, column=2, padx=2, pady=2, sticky="s")

Label( text="DRG►", fg="orange", font=fontMini).grid(row=16, column=3, sticky="s", padx=2, pady=2)
Button( text="Ans", width=5, height=2, font=fontBotao).grid(row=17, column=3, sticky="s", padx=2, pady=2)

Label( text="%", fg="orange", font=fontMini).grid(row=16, column=4, sticky="s", padx=2, pady=2)
Button( text="=", width=5, height=2, font=fontBotao).grid(row=17, column=4, sticky="s", padx=2, pady=2)

root.mainloop()