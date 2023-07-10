import customtkinter

def clique():
    print("Logado!")
    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("300x200")

login = customtkinter.CTkEntry(janela, placeholder_text="Login")
login.pack(padx=10, pady=10)
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)
lembrar = customtkinter.CTkCheckBox(janela, text="Lembrar")
lembrar.pack(padx=5, pady=5)


botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)
janela.mainloop()
