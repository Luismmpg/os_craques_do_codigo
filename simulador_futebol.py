import tkinter as tk
import random
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

frame_lista_jogadores = tk.Frame(janela)
frame_lista_jogadores.pack(side=tk.LEFT)

lista_jogadores = tk.Listbox(frame_lista_jogadores, width=25, height=20)
lista_jogadores.insert(1, "Paulo Perneta")
lista_jogadores.insert(2, "Cristiano McDonald")
lista_jogadores.insert(3, "Marco Orelhas")
lista_jogadores.insert(4, "Luis Abêbera")
lista_jogadores.insert(5, "Pepe Rápido")
lista_jogadores.insert(6, "João Feliz")
lista_jogadores.insert(7, "Ricardo Hortícola")
lista_jogadores.insert(8, "Nelsom Sem Medo")
lista_jogadores.insert(9, "João Canudinho")
lista_jogadores.insert(10, "João Cancelado")
lista_jogadores.insert(11, "Toti Fruti")
lista_jogadores.insert(12, "Diogo DaLota")
lista_jogadores.insert(13, "João Cancelado")
lista_jogadores.insert(14, "Vitinha Maria")~
lista_jogadores.insert(15, "Otávivo")
lista_jogadores.insert(16, "Rafael Miau")
lista_jogadores.insert(17, "Diogo Kefir")
lista_jogadores.insert(18, "Ruben Degelo")
lista_jogadores.insert(19, "Goncalo Galho")
lista_jogadores.insert(20, "Ruben Mensal")
lista_jogadores.insert(21, "Diogo Coxinha")
lista_jogadores.insert(22, "Rui Patricinho")

lista_jogadores.pack(side=tk.TOP)

frame_botao_adicionar_jogador = tk.Frame(frame_lista_jogadores)
frame_botao_adicionar_jogador.pack(side=tk.BOTTOM)

botao_adicionar_jogador = tk.Button(
    frame_botao_adicionar_jogador,
    text="Adicionar Jogador",
    command=lambda: adicionar_jogador(lista_jogadores, lista_jogadores_selecionados),
)
botao_adicionar_jogador.pack()

frame_lista_jogadores_selecionados = tk.Frame(janela)
frame_lista_jogadores_selecionados.pack(side=tk.RIGHT)


lista_jogadores_selecionados = tk.Listbox(frame_lista_jogadores_selecionados, width=25, height=20)
lista_jogadores_selecionados.pack(side=tk.TOP)


frame_botao_remover_jogador = tk.Frame(frame_lista_jogadores_selecionados)
frame_botao_remover_jogador.pack(side=tk.BOTTOM)

botao_remover_jogador = tk.Button(
    frame_botao_remover_jogador,
    text="Remover Jogador",
    command=lambda: remover_jogador(lista_jogadores_selecionados, lista_jogadores),
)
botao_remover_jogador.pack()

def abrir_janela_jogo():
    janela_jogo = tk.Tk()
    janela_jogo.title("Janela de Partida")
    janela_jogo.geometry("600x400")

    equipa1 = "benfica"
    equipa2 = "porto"
    def simulador_jogo(self):
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        tk.Label(self, text=f"Resultado do jogo: {resultado}")

    janela_jogo.mainloop()


botao_jogar = tk.Button(janela, text="Jogar Partida", command=abrir_janela_jogo)
botao_jogar.pack()



janela.mainloop()
