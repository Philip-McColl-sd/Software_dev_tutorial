import json

class sign_in:
    def __init__(self):
        with open('users_db.json', 'r') as f:
            self.db = json.load(f)
        # self.name = name
        # self.password = password
        #self.forward() 
    
    def add_player(self,name, password ):
        self.db[name] = password
        with open('users_db.json', 'w') as f:
            json.dump(self.db, f)
