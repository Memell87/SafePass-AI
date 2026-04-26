import customtkinter as ctk
import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choices(caracteres, k=16))
    entry_senha.delete(0, "end")
    entry_senha.insert(0, senha)

# Configuração da Janela
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("SafePass AI")
app.geometry("400x300")

# Elementos da Interface
ctk.CTkLabel(app, text="SafePass", font=("Arial", 30, "bold")).pack(pady=20)

entry_senha = ctk.CTkEntry(app, width=300, placeholder_text="Sua senha aparecerá aqui")
entry_senha.pack(pady=10)

btn = ctk.CTkButton(app, text="GERAR SENHA", command=gerar_senha, fg_color="green", hover_color="darkgreen")
btn.pack(pady=20)

app.mainloop()



# python app.py executar programa 