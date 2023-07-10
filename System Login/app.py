import customtkinter as ctk



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_janela_inicial()

    # Configuração da janela inicial - Tamanho, Título, Bloqueio do Maximizar,
    def config_janela_inicial(self):
        self.geometry("700x400")
        self.title("System Login")
        self.resizable(False, False) # Maximizar bloquedo para deixar o app no tamanho pré-definido. (False=largura, False=altura)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark") # Modo de Aparência
    ctk.set_default_color_theme("dark-blue") #  Cor padrão do tema
    
    app = App()
    app.mainloop()
