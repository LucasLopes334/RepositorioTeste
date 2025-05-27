import tkinter as tk
from tkinter import messagebox

# Função para verificar o login
def verificar_login():
    usuario = entrada_usuario.get()  # Indentação corrigida
    senha = entrada_senha.get()  # Indentação corrigida
    
    # Aqui você colocaria a lógica para verificar o usuário e a senha
    # Em um sistema real, isso envolveria comparar com dados armazenados
    if usuario == "usuario" and senha == "senha":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        janela.destroy()  # Fecha a janela de login após o sucesso
        # Aqui você pode abrir a próxima janela do seu sistema
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Sistema de Login")

# Rótulo para o nome de usuário
rotulo_usuario = tk.Label(janela, text="Usuário:")
rotulo_usuario.grid(row=0, column=0, padx=40, pady=40, sticky="w")

# Campo de entrada para o nome de usuário
entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=40, pady=40, sticky="ew")

# Rótulo para a senha
rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.grid(row=1, column=0, padx=40, pady=40, sticky="w")

# Campo de entrada para a senha
entrada_senha = tk.Entry(janela, show="*")  # 'show="*"' oculta os caracteres digitados
entrada_senha.grid(row=1, column=1, padx=40, pady=40, sticky="ew")

# Botão de login
botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.grid(row=2, column=0, columnspan=2, padx=40, pady=40, sticky="ew")

# Configuração de peso das colunas para que os campos de entrada se expandam
janela.grid_columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
