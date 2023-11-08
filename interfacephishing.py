import tkinter as tk
from tkinter import messagebox
import urllib.parse

def is_phishing_url(url):
    # Divide a URL em partes
    parsed_url = urllib.parse.urlparse(url)

    # Obtém o domínio da URL
    domain = parsed_url.netloc

    # Lista de palavras-chave suspeitas em URLs de phishing
    phishing_keywords = ["phishing", "login", "account", "secure", "verification"]

    # Verifica se o domínio contém palavras-chave suspeitas
    for keyword in phishing_keywords:
        if keyword in domain:
            return True

    return False

def check_phishing():
    url = entry.get()
    if is_phishing_url(url):
        messagebox.showinfo("Detecção de Phishing", "Este link parece ser de phishing.")
    else:
        messagebox.showinfo("Detecção de Phishing", "Este link parece ser legítimo.")

# Cria a janela principal
window = tk.Tk()
window.title("Detector de Phishing")

# Defina a largura e a altura da janela
window.geometry("400x200")  # Largura x Altura

# Cria um rótulo e uma entrada para inserir o URL
label = tk.Label(window, text="Digite o URL:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Cria um botão para verificar o URL
check_button = tk.Button(window, text="Verificar", command=check_phishing)
check_button.pack()

# Inicia a janela
window.mainloop()
