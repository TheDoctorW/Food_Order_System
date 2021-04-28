from abc import ABC,abstractclassmethod
from item import *

class mains_order(ABC):
    def __init__(self):
        self._buns = []
        self._patties = []
        self._ingredient = []
        self._foodtype = "mains"
    
    @property
    def foodtype(self):
        return self._foodtype
    
    def add_buns(self,item):
        self._buns.append(item)
    
    def add_patties(self,item):
        self._patties.append(item)
    
    def add_ingredient(self,item):
        self._ingredient.append(item)
    
    @property
    def get_buns(self):
        return self._buns
    
    @property
    def get_patties(self):
        return self._patties
    
    @property
    def get_ingredient(self):
        return self._ingredient
    
    @property
    def total_price(self):
        buns_price = 0
        patties_price = 0
        ingredient_price = 0
        for item in self._buns:
            buns_price = buns_price + item.total_price
        
        for item in self._patties:
            patties_price = patties_price + item.total_price
        
        for item in self._ingredient:
            ingredient_price = ingredient_price + item.total_price
        
        return buns_price + patties_price + ingredient_price
    
    # @property
    # def display_mains(self):
    #     print("Current Mains order:")
    #     print("Buns: ",end = "")
    #     for item in self._buns:
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("Patties: ",end = "")
    #     for item in self._patties:
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("Ingredient: ",end = "")
    #     for item in self._ingredient:
    #         print(item,end = "")
    #     print("\n",end = "")
    #     print("Toal pirce for mains: {0}".format(self.total_price))
    #     print("--------------")
    @property
    def Buns(self):
        Buns_str = []
        for item in self._buns:
            Buns_str.append(item.__str__())
        return Buns_str
    @property
    def Patties(self):
        Patties_str = []
        for item in self._patties:
           Patties_str.append(item.__str__())
        return Patties_str
    @property
    def Ingredient(self):
        Ingredient_str = []
        for item in self._ingredient:
            Ingredient_str.append(item.__str__())
        return Ingredient_str
    def __str__(self):
        return "{0} {1} {2} Total price for mains: {3}".format(self.Buns[0:],self.Patties[0:],self.Ingredient[0:],self.total_price)


        
class Buger(mains_order):
    def __init__(self):
        self._buns = []
        self._patties = []
        self._ingredient = []
        self._foodtype = "mains"

class Wrap(mains_order):
    def __init__(self):
        self._buns = []
        self._patties = []
        self._ingredient = []
        self._foodtype = "mains"



