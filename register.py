import json


class CashRegister:
    def __init__(self):
        self.sharedSpace = 'sharedSpace.json'
        self.name = 'cashRegister'

    def addSharedSpace(self, code, amount):

        with open(self.sharedSpace) as mon_fichier:
            existing_data = json.load(mon_fichier)
        
        existing_data['data'][code] = amount
        
        with open(self.sharedSpace, 'w') as mon_fichier:
            json.dump(existing_data, mon_fichier)

    def getSharedSpace(self):
        with open(self.sharedSpace) as mon_fichier:
            data = json.load(mon_fichier)
        return data
    
    def updateSharedSpace(self, code ,amount):
        with open(self.sharedSpace) as mon_fichier:
            existing_data = json.load(mon_fichier)
        existing_data['data'][code] = amount
        print(existing_data['data'][code])
        with open(self.sharedSpace, 'w') as mon_fichier:
            json.dump(existing_data, mon_fichier)

main = CashRegister()
# main.addSharedSpace({'12345': 10})
main.addSharedSpace('69000', 69)
main.updateSharedSpace('123456', 109999)
