import json

from functools import reduce
from operator import or_

class Station():
    def __init__(self):
        self.sharedSpace = 'sharedSpace.json'
        
    def getSharedSpace(self):
        with open(self.sharedSpace) as mon_fichier:
            data = json.load(mon_fichier)
        return data
    
    def addSharedSpace(self, code, amount):
        with open(self.sharedSpace) as mon_fichier:
            existing_data = json.load(mon_fichier)
        
        existing_data['data'][code] = amount
        
        with open(self.sharedSpace, 'w') as mon_fichier:
            json.dump(existing_data, mon_fichier)
            
            
    def removeSharedSpace(self, id_to_remove): 
        try :
            with open(self.sharedSpace) as mon_fichier:
                existing_data = json.load(mon_fichier)
                
            existing_data['data'].pop(id_to_remove)
            
            with open(self.sharedSpace, 'w') as mon_fichier:
                json.dump(existing_data, mon_fichier)
        except KeyError:
            print('Ce code n\'existe pas')
            
    def passeALaPompe(self, codeWanted, amountWanted):
        existing_data = self.getSharedSpace()
        try:
            amount = existing_data['data'][codeWanted]
            if amountWanted < amount:
                existing_data['data'][codeWanted] = amount - amountWanted
                with open(self.sharedSpace, 'w') as mon_fichier:
                    json.dump(existing_data, mon_fichier)
            elif amountWanted == amount:
                self.removeSharedSpace(codeWanted)
            else:
                print('Pas assez de carburant avec ce code')
                print('Il reste {} litres avec ce code'.format(amount))
                
        except KeyError:
            print('Ce code n\'existe pas')
            

        
        
main = Station()
main.addSharedSpace('123456', 20)
main.passeALaPompe('123456', 20)
# main.addSharedSpace('56789', 30)
# main.removeSharedSpace('123456')
print(main.getSharedSpace())