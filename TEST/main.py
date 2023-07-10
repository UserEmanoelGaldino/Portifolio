import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Login")
texto.pack(padx=10, pady=10)

janela.mainloop()
