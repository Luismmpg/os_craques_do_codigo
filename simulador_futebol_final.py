import tkinter as tk
from PIL import ImageTk, Image


def abrir_janela_config():
    janela_config = tk.Toplevel(menu)
    janela_config.title("Configuração do Jogo")
    janela_config_width = 800
    janela_config_height = 600

    screen_width = janela_config.winfo_screenwidth()
    screen_height = janela_config.winfo_screenheight()

    pos_x = (screen_width - janela_config_width) // 2
    pos_y = (screen_height - janela_config_height) // 2

    janela_config.geometry(
        f"{janela_config_width}x{janela_config_height}+{pos_x}+{pos_y}"
    )

    imagem_config_pil = Image.open("imagens/campo_futebol_01.jpg")
    largura_config, altura_config = imagem_config_pil.size

    largura_minima = 800
    altura_minima = 600

    fator_escala = min(
        1.0,
        float(janela_config_width) / max(largura_config, largura_minima),
        float(janela_config_height) / max(altura_config, altura_minima),
    )
    nova_largura_config = max(int(largura_config * fator_escala), largura_minima)
    nova_altura_config = max(int(altura_config * fator_escala), altura_minima)
    imagem_config_pil = imagem_config_pil.resize(
        (nova_largura_config, nova_altura_config), Image.LANCZOS
    )

    imagem_config_tk = ImageTk.PhotoImage(imagem_config_pil)

    canvas_config = tk.Canvas(
        janela_config, width=nova_largura_config, height=nova_altura_config
    )
    canvas_config.create_image(0, 0, anchor=tk.NW, image=imagem_config_tk)
    canvas_config.pack()

    # Adicionar o título "Simulador de Futebol"
    titulo_config = tk.Label(
        janela_config,
        text="Convocatória",
        font=("Arial", 20),
        fg="yellow",
        bg="darkgreen",
        highlightbackground=janela_config.cget("background"),
    )
    titulo_config.place(relx=0.5, rely=0.09, anchor=tk.CENTER)

    # Adicionar informação para seleção de jogadores e equipa
    titulo_config_escolha = tk.Label(
        janela_config,
        text="Selecione os jogadores que\n deseja convocar para a partida.\n\nEscolha depois a equipa\ncom que pretende jogar.",
        font=("Arial", 13),
        fg="yellow",
        bg="darkgreen",
        highlightbackground=janela_config.cget("background"),
    )
    titulo_config_escolha.place(relx=0.5, rely=0.29, anchor=tk.CENTER)

    # Informação de número de jogadores convocados
    label_contagem = tk.Label(
        janela_config,
        text="Total de convocados: 0",
        font=("Arial", 11),
        fg="yellow",
        bg="darkgreen",
    )
    label_contagem.place(relx=0.78, rely=0.08, anchor=tk.CENTER)

    label_equipa_escolhida = tk.Label(
        janela_config,
        font=("Arial", 13),
        fg="yellow",
        bg="darkgreen",
    )
    label_equipa_escolhida.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Criar Listbox com lista de jogadores disponíveis
    lista_jogadores = tk.Listbox(janela_config, width=25, height=22)
    lista_jogadores.place(relx=0.22, rely=0.4, anchor=tk.CENTER)

    lista_jogadores.insert(1, "Paulo Perneta")
    lista_jogadores.insert(2, "Cristiano McDonald")
    lista_jogadores.insert(3, "Marco Orelhas")
    lista_jogadores.insert(4, "Luis Abêbera")
    lista_jogadores.insert(5, "Pepe Rápido")
    lista_jogadores.insert(6, "João Feliz")
    lista_jogadores.insert(7, "Ricardo Hortícola")
    lista_jogadores.insert(8, "Nelsom Sem Medo")
    lista_jogadores.insert(9, "João Canudinho")
    lista_jogadores.insert(10, "Leandro Pessi")
    lista_jogadores.insert(11, "Eussábio")
    lista_jogadores.insert(12, "Fernando Cabana")
    lista_jogadores.insert(13, "Diogo Cereais")
    lista_jogadores.insert(14, "José Chá")
    lista_jogadores.insert(15, "Fábio Pimentão")
    lista_jogadores.insert(16, "Diogo Kapa")
    lista_jogadores.insert(17, "Diogo Dasort")
    lista_jogadores.insert(18, "Dário Exulo")
    lista_jogadores.insert(19, "Acácio Mosquito")
    lista_jogadores.insert(20, "Alfredo das Baladas")
    lista_jogadores.insert(21, "Carlos Cebolinha")
    lista_jogadores.insert(22, "Peko")

    # Cria Listbox com lista de jogadores selecionados
    lista_jogadores_selecionados = tk.Listbox(janela_config, width=25, height=22)
    lista_jogadores_selecionados.place(relx=0.78, rely=0.4, anchor=tk.CENTER)

    jogadores_selecionados = {}

    def adicionar_jogador(lista_jogadores, lista_jogadores_selecionados):
        jogador_add = lista_jogadores.get(lista_jogadores.curselection())
        if jogador_add:
            lista_jogadores_selecionados.insert("end", jogador_add)
            lista_jogadores.delete(lista_jogadores.curselection())

            # Aumentar o contador do jogador selecionado
            if jogador_add in jogadores_selecionados:
                jogadores_selecionados[jogador_add] += 1
            else:
                jogadores_selecionados[jogador_add] = 1

            # Atualizar o contador
            atualizar_contagem()

    def remover_jogador(lista_jogadores_selecionados, lista_jogadores):
        jogador_del = lista_jogadores_selecionados.get(
            lista_jogadores_selecionados.curselection()
        )
        if jogador_del:
            lista_jogadores.insert("end", jogador_del)
            lista_jogadores_selecionados.delete(
                lista_jogadores_selecionados.curselection()
            )

            # Diminuir o contador
            if jogador_del in jogadores_selecionados:
                jogadores_selecionados[jogador_del] -= 1
            else:
                jogadores_selecionados[jogador_del] = 1

            atualizar_contagem()

    def atualizar_contagem():
        total = sum(jogadores_selecionados.values())
        label_contagem.config(text=f"Total de convocados: {total}")

    # Botão para adicionar jogador
    botao_esquerda = tk.Button(
        janela_config,
        text="Adicionar Jogador",
        command=lambda: adicionar_jogador(
            lista_jogadores, lista_jogadores_selecionados
        ),
    )
    botao_esquerda.place(relx=0.22, rely=0.73, anchor=tk.CENTER)

    # Botão para remover jogador
    botao_direita = tk.Button(
        janela_config,
        text="Remover Jogador",
        command=lambda: remover_jogador(lista_jogadores_selecionados, lista_jogadores),
    )
    botao_direita.place(relx=0.78, rely=0.73, anchor=tk.CENTER)

    janela_config.mainloop()


# Criar a janela principal
menu = tk.Tk()
menu.title("Menu Principal")
menu_width = 600
menu_height = 350

# Obter as dimensões do ecrã
screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()

# Calcular as coordenadas para centrar a janela no ecrã
pos_x = (screen_width - menu_width) // 2
pos_y = (screen_height - menu_height) // 2

# Definir geometria da janela para centrar
menu.geometry(f"{menu_width}x{menu_height}+{pos_x}+{pos_y}")

imagem_pil = Image.open("imagens/futebol_04.jpg")
largura, altura = imagem_pil.size

largura_minima = 600
altura_minima = 350

fator_escala = min(
    1.0,
    float(menu_width) / max(largura, largura_minima),
    float(menu_height) / max(altura, altura_minima),
)
nova_largura = max(int(largura * fator_escala), largura_minima)
nova_altura = max(int(altura * fator_escala), altura_minima)
imagem_pil = imagem_pil.resize((nova_largura, nova_altura), Image.LANCZOS)

imagem_tk = ImageTk.PhotoImage(imagem_pil)

canvas = tk.Canvas(menu, width=nova_largura, height=nova_altura)
canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)
canvas.pack()

titulo = tk.Label(
    menu,
    text="Simulador de Futebol",
    font=("Arial", 30),
    fg="yellow",
    bg="green",
    highlightbackground=menu.cget("background"),
)
titulo.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Adicionar o botão para iniciar a simulação
botao_iniciar = tk.Button(
    menu,
    text="Iniciar Simulação",
    font=("Arial", 14),
    fg="white",
    bg="blue",
    padx=10,
    pady=5,
    command=abrir_janela_config,
)
botao_iniciar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

menu.mainloop()