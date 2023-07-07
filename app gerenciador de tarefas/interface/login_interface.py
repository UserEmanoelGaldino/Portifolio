from tkinter import *
from tkinter import ttk

# instanciação:
root = Tk()


# dimenções do app:
root.geometry("700x300")  # largura x Altura


# Nome da Janela:
root.title("MyTask's")



# Configuraçõe da Janela:
root.config(bg="#DCDCDC")  # bg (background)



# Adicionando botão:
field_nickname = Entry(root, foreground="#808080")
field_nickname.insert(0, "Usuário")

field_password = Entry(root, foreground="#808080")
field_password.insert(0, "Senha")

button_entry = Button(root, text="Entrar", bg="#404040", foreground="#FFFFFF")
button_sing_in = Button(root, text="Cadastre-se", bg="#404040", foreground="#FFFFFF")



# Posicionamento do botão na tela:
field_nickname.place(relx=0.39 ,rely=0.30)
field_password.place(relx=0.39 ,rely=0.46)


button_entry.place(relx=0.39, rely=0.61)
button_sing_in.place(relx=0.51, rely=0.61)



# Loop da Janela:
root.mainloop()
