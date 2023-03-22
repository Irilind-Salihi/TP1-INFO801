from customer import Customer
from register import CashRegister
from station import Station

def main():
    # Faire une gestion de menu
    choix = ""
    while(choix != "q"):
        print("1 - Créer un client")
        print("2 - Créer une caisse")
        print("3 - Créer une pompe")
    
    
    print("Hello World!")
    #create a customer from the customer class
    pierro = Customer('Pierro Le Rigolo')
    
    #create a register from the register class
    caisse = CashRegister('Caisse')
    
    #add a code to the customer
    pierro.add_code(caisse.acheteTicket('Essence', 10))

    pompe = Station('Pompe1')
    
    print(pierro.get_last_code())
    pompe.passeALaPompe(pierro.get_last_code(), 10)

    

if __name__ == "__main__":
    main()
