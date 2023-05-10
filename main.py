import tkinter as tk
import json
import os
import time as tm
from UI import image
from sign_in import sign_in

def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)
    # Verificar si se han ingresado credenciales válidas
    if username != "" and password != "" and username in user_db.db.keys() and password != user_db.db[username]:# La credencial es valida pero la contraseña es incorrecta
        username = username_entry.get()
        password = password_entry.get()
        print("Username:", username)
        print("Password:", password)
    if username != "" and password != "" and username not in user_db.db.keys():
        user_db.add_player(username, password)
    if username != "" and password != "" and username in user_db.db.keys() and password == user_db.db[username]:
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

if __name__ == '__main__':
    # main()
    """
    Main loop
    """
        # Crear la ventana principal
    # images = image()
    user_db = sign_in()
    window = tk.Tk()
    window.title("Log in")
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











#     # Load Images
#     #Pros: al cargar todas las imagenes a un diccionario se tienen todas las imagenes a disposici[on mas rapido.
#     #Cons: se ocupa mas ram.
#     images = image()
#     user_db = sign_in()
#     # Check User
#                         # with open('example.json') as f:
#                         #     players_db = json.load(f)
#     # Enter name
#     name = input("Say the name warrior:")
#     if name in user_db.db.keys():
#         password = ''
#         while password != user_db.db[name]:
#             password = input("Say the password:")
#         clear_output()
#         print(f'welcome back {name}!')
#     else:
#         print(f'{name} lets write your name in to the books!')
#         images.show("wizard")
#         tm.sleep(2)
#         clear_output()
#         name = input("Say the name warrior:")
#         password = input("wisper the your secret words:")
#         user_db.add_player(name, password)
#     action = ""
#     while action != "exit":
#         action = input("What do you want to do?\n")
#         images.show(action)




# def clear_output():
#     os.system('cls' if os.name == 'nt' else 'clear')

