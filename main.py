from customer import Customer

def main():
    print("Hello World!")
    #create a customer from the customer class
    Pierro = Customer('Pierro', 'Le Rigolo')
    #add a code to the customer
    Pierro.add_code('123456')

    #get the full name of the customer
    print(Pierro.get_full_name())

    

if __name__ == "__main__":
    main()
