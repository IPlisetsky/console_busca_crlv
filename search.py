import os
from tkinter.filedialog import askdirectory
import pandas as pd
import shutil
import tkinter as tk
import time
import datetime
from tkinter import Button, Frame

hoje = datetime.datetime.today().strftime("%d_%m_%Y")
print(hoje)

dir1 = r"C:\Users\igor.gabriel\JSL SA"
dir2 = r"c:\Users\igor.gabriel\JSL SA(1)"
dir3 = r"C:\Users\igor.gabriel\OneDrive - JSL SA"

def buscar(filename):
    # Onde vai buscar
    print("BUSCAR")
    dir_pdf = askdirectory()
    lista_pdfs = os.listdir(dir_pdf)
    
    # Para onde os arquivos encontrados vão
    pasta_destino = r"C:\Backup - OneDrive\novo dnv\Área de Trabalho\BUSCA\PASTAS" + f"\{hoje}"
    
    def analisar_pastas(pasta_atual):
        try:
            global ultima_pasta
            cont = 0
            conteudo_pasta = os.listdir(pasta_atual)
            for arquivo in conteudo_pasta:
                try:
                    caminho_item = os.path.join(pasta_atual, arquivo) # caminho atual
                    print(caminho_item)
                    if os.path.isdir(caminho_item):
                        print(f"\nPASTA ATUAL SENDO LIDA: {caminho_item}\n")
                        ultima_pasta = arquivo
                        print(f"ULTIMA PASTA: {ultima_pasta}")
                        analisar_pastas(caminho_item)
                    elif ".pdf" in arquivo:
                        print(f"PASTA ATUAL: {pasta_atual}")
                        print(f"\nArquivos pasta atual: {len(conteudo_pasta)}")
                        caminho_item = os.path.join(pasta_atual, arquivo)
                        elementos_comuns = [x for x in conteudo_pasta if x in placas]
                        for arquivo in elementos_comuns:
                            print(f"IGUAL {elementos_comuns}")
                            caminho_item = f"{pasta_atual}\{arquivo}"
                            caminho_novo_arquivo = f"{pasta_destino}\{arquivo}"
                            if not os.path.exists(pasta_destino):
                                os.makedirs(pasta_destino)
                            shutil.copy(caminho_item, caminho_novo_arquivo)
                            print("=====PLACA ENCONTRADA!=====")
                            print(f"========{arquivo}========")
                            print("===========================")
                            placas.remove(arquivo)
                        break
                    else:
                        pass
                    
                except Exception as e:
                    print(f"ERRO NO CRLV: {arquivo} {e}")      
            os.system('cls' if os.name == 'nt' else 'clear')
    
        except Exception as e:
            print(f"\n\n\nErro analise: {e}\n\n\n")
            time.sleep(10)
    
    # Arquivo
    busca = filename
    dt = pd.read_excel(busca)
    
    placas = [] 
    for index, linha in dt.iterrows():
        try:
            placa = linha['PLACA']
            if ".pdf" in placa:
                pass
            else:
                placa = f"{placa}.pdf"
            placas.append(placa)
        except Exception as e:
            print(f"ERRO: {linha} {e}")
    
    analisar_pastas(dir_pdf)
    print(f"PLACAS NÃO ENCONTRADAS: {placas}")
    nf = pd.DataFrame(placas, columns=["PLACA"])
    nf.to_excel(busca, index=False)



def insert():

    def gera_xlsx(placas):
        try:

            # Convertendo a entrada para uma lista (assumindo que as placas são separadas por vírgula)
            #placas = placas.split(',')
            dt = pd.DataFrame(placas, columns=['PLACA'])  # Criando um DataFrame com uma coluna 'Placa'
            # Obtendo a data atual para o nome do arquivo
            dir = r"C:\Backup - OneDrive\novo dnv\Área de Trabalho\BUSCA"
            filename = dir + r"\busca_"+f"{hoje}"+".xlsx"
            dt.to_excel(filename, index=False)  # Salvando sem o índice


            buscar(filename)  # Chamada da função buscar (se existir)

        except Exception as e:
            print(f"Erro gerando Data Frame: {e}")

    def destroir_tela():
        tela.destroy()
        buscar(filename = r"C:\Backup - OneDrive\novo dnv\Área de Trabalho\BUSCA" + r"\busca_"+f"{hoje}"+".xlsx")

    try:
        tela = tk.Tk()
        tela.title("Insert")
        tela.geometry("250x100")  # Aumentando o tamanho para melhor visualização
        label = tk.Label(tela, text="Insira as placas separadas por vírgula:")
        label.pack()

        entry = tk.Entry(tela, width=30)  # Aumentando o tamanho do campo de entrada
        entry.pack()

        def criar_arquivo():
            placas = entry.get()
            placas = [placas[i:i+7] for i in range(0, len(placas), 7)]
            print(placas)
                
            tela.destroy()
            gera_xlsx(placas)

        enter = tk.Button(tela, text="Enter", command=criar_arquivo)
        enter.pack()
        search_button = tk.Button(tela, text= "Search", command= destroir_tela)
        search_button.pack()

        tela.mainloop()

    except Exception as e:
        print(f"Insert: {e}")

insert()