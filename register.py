import json
import random

class CashRegister:
    def __init__(self, name):
        self.sharedSpace = 'sharedSpace.json'
        self.name = name

    def __addSharedSpace(self, code, amount):
        existing_data = self.__getSharedSpace()
        
        existing_data['data'][code] = amount
        
        with open(self.sharedSpace, 'w') as mon_fichier:
            json.dump(existing_data, mon_fichier)

    def __getSharedSpace(self):
        with open(self.sharedSpace) as mon_fichier:
            data = json.load(mon_fichier)
        return data

            
    def acheteTicket(self, fuel, amout):
        #generate a random code
        code = random.randint(10000, 99999)
        self.__addSharedSpace(code, amout)
        return code
        
        
    

# main = CashRegister()
# main.addSharedSpace({'12345': 10})
# main.addSharedSpace('69000', 69)
