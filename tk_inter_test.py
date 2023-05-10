import tkinter as tk

def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)
    # Verificar si se han ingresado credenciales válidas
    if username != "" and password != "":
        # Deshabilitar campos de credenciales
        username_entry.configure(state='disabled')
        password_entry.configure(state='disabled')
        credentials_label.pack_forget()
        username_label.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()
        credentials_button.pack_forget()
        # Mostrar elementos de entrada de texto
        text_label.pack()
        text_entry.pack()
        text_button.pack()

def submit_text():
    text = text_entry.get("1.0", tk.END).strip()
    print("Text:", text)

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz de ejemplo")
window.geometry("300x300")

# Etiqueta para las credenciales
credentials_label = tk.Label(window, text="Ingrese sus credenciales:")
credentials_label.pack()

# Etiqueta y entrada para el nombre de usuario
username_label = tk.Label(window, text="Nombre de usuario:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Etiqueta y entrada para la contraseña
password_label = tk.Label(window, text="Contraseña:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Botón para enviar las credenciales
credentials_button = tk.Button(window, text="Enviar Credenciales", command=submit_credentials)
credentials_button.pack()

# Etiqueta y entrada para ingresar texto (inicialmente oculto)
text_label = tk.Label(window, text="Ingresar Texto:")
text_entry = tk.Text(window, height=5)

# Botón para enviar el texto (inicialmente oculto)
text_button = tk.Button(window, text="Enviar Texto", command=submit_text)

# Iniciar el bucle principal de la ventana
window.mainloop()
