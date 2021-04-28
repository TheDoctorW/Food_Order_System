from abc import ABC, abstractclassmethod

class Item(ABC):
    def __init__(self,foodid,unitprice,avanum,foodtype,quantity = 0):
        self._avanum = avanum
        self._unitprice = unitprice
        self._foodid = foodid
        self._foodtype = foodtype
        self._quantity = quantity
    
    @property
    def avanum(self):
        return self._avanum
    
    @avanum.setter
    def avanum(self,number):
        self._avanum = number
    
    @property
    def unitprice(self):
        return self._unitprice
    
    @unitprice.setter
    def unitprice(self,price):
        self._unitprice = price
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self,num):
        self._quantity = num
    
    @property
    def foodid(self):
        return self._foodid
    
    @property
    def foodtype(self):
        return self._foodtype
    
    @property
    def total_price(self):
        return self._unitprice * self._quantity
    
    def __str__(self):
        return "{0} < unitprice:{1},foodtype:{2} >".format(self._foodid,self._unitprice,self._foodtype)

class Bottle_drink(Item):
    def __init__(self,foodid,unitprice,avanum,foodtype):
        super().__init__(foodid,unitprice,avanum,foodtype)

class Can_drink(Item):
    def __init__(self,foodid,unitprice,avanum,foodtype):
        super().__init__(foodid,unitprice,avanum,foodtype)

class Patties(Item):
    def __init__(self,foodid,unitprice,avanum,foodtype):
        super().__init__(foodid,unitprice,avanum,foodtype)

class Buns(Item):
    def __init__(self,foodid,unitprice,avanum,foodtype):
        super().__init__(foodid,unitprice,avanum,foodtype)

class Ingredient(Item):
    def __init__(self,foodid,unitprice,avanum,foodtype):
        super().__init__(foodid,unitprice,avanum,foodtype)



