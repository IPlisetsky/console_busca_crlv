import os
import re
import pandas as pd

dir = r""
funciono = dir + r"\funcionando"

padrao = r"[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}"
padrao2 = r"[A-Z]{3}[0-9]{4}"

lista = os.listdir(dir)
for i in lista:
    try:
        if ".pdf" in i:
            try:
                novo = re.findall(padrao, i)
                novo = novo[0]
                print(novo)
                i = os.replace( f"{dir}\{i}", f"{dir}\{novo}.pdf")
            except:
                novo = re.findall(padrao2, i)
                novo = novo[0]
                print(novo)
                i = os.replace( f"{dir}\{i}", f"{dir}\{novo}.pdf")
        else:
            pass
    except Exception as e:
        print(f"Erro {i} {e}")
