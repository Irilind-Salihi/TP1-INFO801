import json

from functools import reduce
from operator import or_

class Station():
    def __init__(self, name):
        self.sharedSpace = 'sharedSpace.json'
        self.name = name
        
    def __getSharedSpace(self):
        with open(self.sharedSpace) as mon_fichier:
            data = json.load(mon_fichier)
        return data
    
    def __addSharedSpace(self, code, amount):
        existing_data = self.__getSharedSpace()
        
        existing_data['data'][code] = amount
        
        with open(self.sharedSpace, 'w') as mon_fichier:
            json.dump(existing_data, mon_fichier)
            
            
    def __removeSharedSpace(self, id_to_remove): 
        try :
            existing_data = self.__getSharedSpace()
                
            existing_data['data'].pop(id_to_remove)
            
            with open(self.sharedSpace, 'w') as mon_fichier:
                json.dump(existing_data, mon_fichier)
        except KeyError:
            print('Ce code n\'existe pas')
            
    def passeALaPompe(self, codeWanted, amountWanted):
        existing_data = self.__getSharedSpace()
        try:
            amount = existing_data['data'][codeWanted] 
            if amountWanted < amount:
                existing_data['data'][codeWanted] = amount - amountWanted
                with open(self.sharedSpace, 'w') as mon_fichier:
                    json.dump(existing_data, mon_fichier)
                print('Vous avez pris {} litres'.format(amountWanted))
                print('Il reste {} litres avec ce code'.format(amount - amountWanted))
            elif amountWanted == amount:
                self.__removeSharedSpace(codeWanted)
                print('Vous avez pris {} litres'.format(amountWanted))
                print('Il ne reste plus de carburant avec ce code')
            else:
                print('Pas assez de carburant avec ce code')
                print('Il reste {} litres avec ce code'.format(amount))
        except KeyError:
            print('Ce code n\'existe pas')
            
        
        
            

        
        
# main = Station()
# main.addSharedSpace('123456', 20)
# main.passeALaPompe('123456', 20)
# main.addSharedSpace('56789', 30)
# main.removeSharedSpace('123456')
