class Details:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.abc()
    def abc(self):
        print(f'the first name {self.first_name}')
        print(f'the last name {self.last_name}')
d1 = Details('Abhishek','Chauhan')
d2 = Details('Abhinav','chauhan')