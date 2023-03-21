#Create a customer class with first name last name and a code list
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.code_list = []

    def add_code(self, code):
        self.code_list.append(code)

    def get_code_list(self):
        return self.code_list
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.code_list)