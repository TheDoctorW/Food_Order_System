from abc import ABC,abstractclassmethod
from src.item import *

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
    
    def __str__(self):
        Buns_str = ''
        Patties_str = ''
        Ingredient_str = ''
        for item in self._buns:
            Buns_str = Buns_str +  item.__str__() +'\n'
        for item in self._patties:
            Patties_str = Patties_str + item.__str__() +'\n'
        for item in self._ingredient:
            Ingredient_str = Ingredient_str +  item.__str__() +'\n'    
        return "mains: \n{0}{1}{2}||||".format(Buns_str,Patties_str,Ingredient_str)

        
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


