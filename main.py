import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Aqui, você pode adicionar lógica para verificar o login
    # Por exemplo, você pode verificar se o usuário e a senha correspondem a um conjunto predefinido.

    if usuario == "pedro" and senha == "silva":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos")

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Login")

# Criar widgets (rótulos, entradas, botões)
label_usuario = tk.Label(janela, text="Usuário:")
label_senha = tk.Label(janela, text="Senha:")
entry_usuario = tk.Entry(janela)
entry_senha = tk.Entry(janela, show="*")  # A opção show="*" oculta os caracteres da senha

botao_login = tk.Button(janela, text="Login", command=verificar_login)

# Organizar widgets na janela usando o gerenciador de geometria grid
label_usuario.grid(row=0, column=0, padx=10, pady=10)
label_senha.grid(row=1, column=0, padx=10, pady=10)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)
entry_senha.grid(row=1, column=1, padx=10, pady=10)
botao_login.grid(row=2, column=1, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
