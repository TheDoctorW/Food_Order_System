from item import *
from customer import customer

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

    @property
    def Mains(self):
        Mains_str = []
        for item in self._item:
            if item._foodtype == "mains":
                Mains_str.append(item.__str__())
        return Mains_str
    @property
    def Drinks(self):
        Drinks_str = []
        for item in self._item:
            if item._foodtype == "drinks":
                Drinks_str.append(item.__str__())
        return Drinks_str
    @property
    def Sides(self):
        Sides_str = []
        for item in self._item:
            if item._foodtype == "sides":
                Sides_str.append(item.__str__())
        return Sides_str
    @property
    def Sundaes(self):
        Sundaes_str = []
        for item in self._item:
            if item._foodtype == "sundaes":
                Sundaes_str.append(item.__str__())
        return Sundaes_str

    def __str__(self):
        return "Mains order:\n{0}\n\nDrinks order:\n{1}\n\nSides order:\n{2}\n\nSundaes order:\n{3}\n\n-->Total Price:\n{4}\n".format(self.Mains[0:],self.Drinks[0:],self.Sides[0:],self.Sundaes[0:],self.total_price)
    









    # @property
    # def display_order(self):
    #     mains = []
    #     drink = []
    #     sides = []
    #     sundae = []
    #     for item in self._item:
    #         if item._foodtype == "mains":
    #             mains.append(item)
    #         elif item._foodtype == "drinks":
    #             drink.append(item)
    #         elif item._foodtype == "sides":
    #             sides.append(item)
    #         elif item._foodtype == "sundaes":
    #             sundae.append(item)
    #     '''
    #     display mains
    #     '''
    #     if len(mains) == 0:
    #             print("No mains order")
    #     for item in mains:
    #         print(item)
    #     '''
    #     display drinks
    #     '''
    #     print("Drinks : ",end = "")
    #     if len(drink) == 0:
    #             print("No drinks order")
    #     for item in drink:
    #         print("\n")
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("--------------")
    #     '''
    #     display sides
    #     '''
    #     print("Sides : ",end = "")
    #     if len(sides) == 0:
    #             print("No sides order")
    #     for item in sides:
    #         print("\n")
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("--------------")
    #     '''
    #     display sundaes
    #     '''
    #     print("Sundaes: ",end = "")
    #     if len(sundae) == 0:
    #         print("No sundae order")
    #     for item in sundae:
    #         print("\n")
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("--------------")
    #     '''
    #     display total price
    #     '''
    #     print("*Toal price for customer < {0} > : {1}".format(self._customer_id,self.total_price),end = "")
    #     print("\n",end = "")
