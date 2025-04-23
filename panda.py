import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lê os dados do CSV
df = pd.read_csv('dados.csv')

# Dados processados
vendas = np.array(df['vendas'])
vendedores = np.array(df['vendedor'])

# Funções para exibir gráficos
def grafico_linha():
    plt.figure("Gráfico de Linha")
    plt.plot(vendedores, vendas, marker='o')
    plt.title('Vendas por Vendedor - Linha')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_barra():
    plt.figure("Gráfico de Barra")
    plt.bar(vendedores, vendas, color='skyblue')
    plt.title('Vendas por Vendedor - Barra')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_pizza():
    plt.figure("Gráfico de Pizza")
    plt.pie(vendas, labels=vendedores, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Vendas')
    plt.tight_layout()
    plt.show()

def grafico_dispersao():
    plt.figure("Gráfico de Dispersão")
    plt.scatter(vendedores, vendas, color='green')
    plt.title('Dispersão de Vendas por Vendedor')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def mostrar_estatisticas():
    media = np.mean(vendas)
    mediana = np.median(vendas)
    soma = np.sum(vendas)
    mensagem = f"Média das vendas: {media:.2f}\nMediana das vendas: {mediana:.2f}\nSoma total das vendas: {soma:.2f}"
    messagebox.showinfo("Estatísticas", mensagem)

# Interface Gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Gráficos de Vendas")
janela.geometry("400x300")

frame = ttk.Frame(janela, padding=20)
frame.pack(fill='both', expand=True)

btn1 = ttk.Button(frame, text="Gráfico de Linha", command=grafico_linha)
btn2 = ttk.Button(frame, text="Gráfico de Barra", command=grafico_barra)
btn3 = ttk.Button(frame, text="Gráfico de Pizza", command=grafico_pizza)
btn4 = ttk.Button(frame, text="Gráfico de Dispersão", command=grafico_dispersao)
btn5 = ttk.Button(frame, text="Mostrar Estatísticas", command=mostrar_estatisticas)

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)
btn5.pack(pady=5)

janela.mainloop()