from abc import ABC, abstractclassmethod

class Sundae(ABC):
    def __init__(self,foodid,avanum,foodtype,unitprice,quantity,size):
        self._foodid = foodid
        self._avanum = avanum
        self._foodtype = foodtype
        self._unitprice = unitprice
        self._size = size
    

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        self._size = size

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
    def unitprice(self,unitprice):
        self._unitprice = unitprice

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
        return self._quantity * self._unitprice

    def __str__(self):
        return "{0} < unitprice:{1},foodtype:{2} >".format(self._foodid,self._unitprice,self._foodtype)


class Sundae_inventory(Sundae):
    def __init__(self,foodid,avanum,foodtype,unitprice,quantity,size):
        super().__init__(foodid,avanum,foodtype,unitprice,quantity,size)

class SmallSundae(Sundae):
    def __init__(self,foodid,avanum,foodtype,unitprice,quantity = 0,size = 0):
        super().__init__(foodid,avanum,foodtype,unitprice,quantity,size)

class MediumSundae(Sundae):
    def __init__(self,foodid,avanum,foodtype,unitprice,quantity = 0,size = 0):
        super().__init__(foodid,avanum,foodtype,unitprice,quantity,size)

class LargeSundae(Sundae):
    def __init__(self,foodid,avanum,foodtype,unitprice,quantity = 0,size = 0):
        super().__init__(foodid,avanum,foodtype,unitprice,quantity,size)