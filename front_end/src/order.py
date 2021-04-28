from src.item import *
from src.customer import customer

class order():
    def __init__(self,customer_id,status = "preparing"):
        self._item = []
        self._customer_id = customer_id
        self._status = "preparing"
    
    def add_item(self,item):
        self._item.append(item)
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def total_price(self):
        price = 0
        for item in self._item:
            price = item.total_price + price
        return price
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,updated_status):
        self._status = updated_status

   
    def __str__(self):
        Mains_str = ''
        Drinks_str = ''
        Sides_str = ''
        Sundaes_str = ''
        '''
        string for mains
        '''
        flag = 0
        for item in self._item:
            if item.foodtype == "mains":
                Mains_str = Mains_str +item.__str__() +'\n'
                flag = 1
        if flag == 0:
            Mains_str = "No Mains order"
        '''
        string for drinks
        '''
        flag = 0
        for item in self._item:
            if item.foodtype == "drinks":
                flag = 1
                Drinks_str = Drinks_str +item.__str__() +'\n'
        if flag == 0:
            Drinks_str = "No drinks order"
        '''
        string for sides
        '''
        flag = 0
        for item in self._item:
            if item.foodtype == "sides":
                flag = 1
                Sides_str = Sides_str +item.__str__() +'\n'
        if flag == 0:
            Sides_str = "No Sides order"
        '''
        sundaes
        '''
        flag = 0
        for item in self._item:
            if item.foodtype == "sundaes":
                Sundaes_str = Sundaes_str +item.__str__() +'\n'
                flag = 1
        if flag == 0:
            Sundaes_str ="No Sundae order"
        # '''
        # output string
        # '''
        # output = "Customer {0}'s Order: ".format(self._customer_id) + "\n"
        # output = output + "{0}".format(Mains_str) + '\n'
        # output = "Drinks order: \n"+output + "{0}".format(Drinks_str) + '\n'
        # output = "Sides order: \n"+output+"{0}".format(Sides_str)+'\n'
        # output = "Sundae order: \n"+output+"{0}".format

        return "Status({0})Customer {1}'s Order: \nMains order:\n{2}\nDrinks order:\n{3}\nSides order:\n{4}\nSundae order:\n{5}$Total price: {6}$".format(self._status,self._customer_id,Mains_str,Drinks_str,Sides_str,Sundaes_str,self.total_price)
