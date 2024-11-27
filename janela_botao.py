import tkinter as tk

# Criação de janela principal
janela = tk.Tk()
janela.title("Minha primeira GUI")

# Tamanho da janela
janela.geometry("400x300")

# Criação de um botão
botao = tk.Button(janela, text="Clique Aqui")
botao.pack()

# Inicia o loop principal
janela.mainloop()