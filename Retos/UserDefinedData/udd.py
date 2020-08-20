class Client:
    '''
    Common base class for all clients
    '''
    def __init__(self,name,id,credit,address):
        '''
        Class constructor
        '''        
        self.name = name
        self.id= id
        self.credit= credit
        self.address=address
    def displayClient(self):
      print(f'The Client name is: {self.name} \nThe Client Id is: {self.id} \nThe Client credit is: {self.credit}\nThe Client address is: {self.address}')

if __name__ == "__main__":
    client = Client('Homero Simpson', '00000001', '$100000.00', '742 Evergreen Terrace')
    client.displayClient()
