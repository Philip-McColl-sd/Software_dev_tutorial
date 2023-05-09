import json
import os
import time as tm
from UI import image
from sign_in import sign_in


def main():
    """

    """
    # Load Images
    #Pros: al cargar todas las imagenes a un diccionario se tienen todas las imagenes a disposici[on mas rapido.
    #Cons: se ocupa mas ram.
    images = image()
    user_db = sign_in()
    # Check User
                        # with open('example.json') as f:
                        #     players_db = json.load(f)
    # Enter name
    name = input("Say the name warrior:")
    if name in user_db.db.keys():
        password = ''
        while password != user_db.db[name]:
            password = input("Say the password:")
        clear_output()
        print(f'welcome back {name}!')
    else:
        print(f'{name} lets write your name in to the books!')
        images.show("wizard")
        tm.sleep(2)
        clear_output()
        name = input("Say the name warrior:")
        password = input("wisper the your secret words:")
        user_db.add_player(name, password)
    action = ""
    while action != "exit":
        action = input("What do you want to do?\n")
        images.show(action)




def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()