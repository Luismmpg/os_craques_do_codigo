import tkinter as tk
from tkinter import messagebox


def adicionar_jogador(lista_jogadores, lista_jogadores_selecionados):
    jogador_add = lista_jogadores.get(lista_jogadores.curselection())
    if jogador_add:
        lista_jogadores_selecionados.insert("end", jogador_add)
        lista_jogadores.delete(lista_jogadores.curselection())


def remover_jogador(lista_jogadores_selecionados, lista_jogadores):
    jogador_del = lista_jogadores_selecionados.get(
        lista_jogadores_selecionados.curselection()
    )
    if jogador_del:
        lista_jogadores.insert("end", jogador_del)
        lista_jogadores_selecionados.delete(lista_jogadores_selecionados.curselection())


# def remover_jogador(lista_jogadores, lista_jogadores_selecionados):
#     selecionar_jogador = lista_jogadores_selecionados.curselection()
#     if selecionar_jogador:
#         jogador = lista_jogadores_selecionados.get(selecionar_jogador)
#         lista_jogadores.insert("end", jogador)
#         lista_jogadores_selecionados.delete(selecionar_jogador)


janela = tk.Tk()
janela.title("Simulador de Futebol")
janela.geometry("600x400")

lista_jogadores = tk.Listbox(janela)
lista_jogadores.insert(1, "Paulo Perneta")
lista_jogadores.insert(2, "Cristiano McDonald")
lista_jogadores.insert(3, "Marco Orelhas")
lista_jogadores.insert(4, "Luis Abêbera")
lista_jogadores.insert(5, "Pepe Rápido")
lista_jogadores.insert(6, "João Feliz")
lista_jogadores.insert(7, "Ricardo Hortícola")
lista_jogadores.insert(8, "Nelsom Sem Medo")
lista_jogadores.insert(9, "João Canudinho")

lista_jogadores.pack()


lista_jogadores_selecionados = tk.Listbox(janela)
lista_jogadores_selecionados.pack()

botao_adicionar_jogador = tk.Button(
    janela,
    text="Adicionar Jogador",
    command=lambda: adicionar_jogador(lista_jogadores, lista_jogadores_selecionados),
)
botao_adicionar_jogador.pack()

botao_remover_jogador = tk.Button(
    janela,
    text="Remover Jogador",
    command=lambda: remover_jogador(lista_jogadores_selecionados, lista_jogadores),
)
botao_remover_jogador.pack()


janela.mainloop()
