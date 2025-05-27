import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os usuários cadastrados
usuarios_cadastrados = {}

# Função para cadastrar o usuário
def cadastrar_usuario():
    usuario = entrada_usuario_cadastro.get()
    senha = entrada_senha_cadastro.get()
    
    if usuario in usuarios_cadastrados:
        messagebox.showerror("Erro", "Usuário já cadastrado.")
    else:
        usuarios_cadastrados[usuario] = senha
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        limpar_campos_cadastro()

# Função para verificar o login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Verifica se o usuário está cadastrado e a senha está correta
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        janela_login.destroy()  # Fecha a janela de login após o sucesso
        # Aqui você pode abrir a próxima janela do seu sistema
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função para limpar os campos de cadastro
def limpar_campos_cadastro():
    entrada_usuario_cadastro.delete(0, tk.END)
    entrada_senha_cadastro.delete(0, tk.END)

# Criação da janela de login
def abrir_janela_login():
    global janela_login
    janela_login = tk.Tk()
    janela_login.title("Sistema de Login")
    
    # Alterando a cor de fundo da janela de login
    janela_login.config(bg="black")  # Altere para qualquer cor que desejar, como "lightblue", "gray", "#f0f0f0", etc.

    # Rótulo para o nome de usuário
    rotulo_usuario = tk.Label(janela_login, text="Usuário:", bg="white")  # Cor de fundo também no rótulo
    rotulo_usuario.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    # Campo de entrada para o nome de usuário
    global entrada_usuario
    entrada_usuario = tk.Entry(janela_login)
    entrada_usuario.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Rótulo para a senha
    rotulo_senha =tk.Label(janela_login, text="Senha:", bg="white")  # Cor de fundo também no rótulo
    rotulo_senha.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    # Campo de entrada para a senha
    global entrada_senha
    entrada_senha = tk.Entry(janela_login, show="*")
    entrada_senha.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    # Botão de login
    botao_login = tk.Button(janela_login, text="Login", command=verificar_login)
    botao_login.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    # Botão para abrir a tela de cadastro
    botao_cadastro = tk.Button(janela_login, text="Cadastre-se", command=abrir_janela_cadastro)
    botao_cadastro.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    # Configuração de peso das colunas para que os campos de entrada se expandam
    janela_login.grid_columnconfigure(1, weight=1)

    # Inicia o loop principal da interface gráfica
    janela_login.mainloop()

# Criação da janela de cadastro
def abrir_janela_cadastro():
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro de Usuário")

    # Rótulo para o nome de usuário
    rotulo_usuario_cadastro = tk.Label(janela_cadastro, text="Usuário:")
    rotulo_usuario_cadastro.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    # Campo de entrada para o nome de usuário
    global entrada_usuario_cadastro
    entrada_usuario_cadastro = tk.Entry(janela_cadastro)
    entrada_usuario_cadastro.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Rótulo para a senha
    rotulo_senha_cadastro = tk.Label(janela_cadastro, text="Senha:")
    rotulo_senha_cadastro.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    # Campo de entrada para a senha
    global entrada_senha_cadastro
    entrada_senha_cadastro = tk.Entry(janela_cadastro, show="*")
    entrada_senha_cadastro.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    # Botão de cadastro
    botao_cadastro = tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar_usuario)
    botao_cadastro.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    # Inicia o loop principal da interface gráfica
    janela_cadastro.mainloop()

# Chama a função para abrir a janela de login
abrir_janela_login()
