#Create a customer class with first name last name and a code list
class Customer:
    def __init__(self, name):
        self.name = name
        self.code_list = []

    def add_code(self, code):
        self.code_list.append(code)

    def get_code_list(self):
        return self.code_list
    
    def get_last_code(self):
        if len(self.code_list) == 0:
            print('Le client n\'a pas de code')
            return None
        return '{}'.format(self.code_list[-1])
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.code_list)