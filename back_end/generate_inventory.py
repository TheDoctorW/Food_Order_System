from inventory import Inventory
from item import *
from drink import *
from sides import *
from drink import *
from sundaes import *
def generate_inventory():
    '''
    init a inventory
    '''
    inventory = Inventory()
    '''
    mains
    '''
    fish_patties = Patties("fish_patties",2,40,"mains")
    chicken_patties = Patties("chicken_patties",1.5,50,"mains")
    pork_patties = Patties("pork_patties",1,0,"mains")
    tomato = Ingredient("tomato",0.5,300,"mains")
    buns = Buns("buns",0.5,400,"buns")
    lettuce = Ingredient("lettuce",0.5,100,"mains")
    onions = Ingredient("onions",0.5,0,"mains")
    '''
    sides
    '''
    salad = Sides_inventory("salad",10000,"sides",0,0,0)
    fries = Sides_inventory("fries",10000,"sides",0,0,0)
    springroll = Sides_inventory("springroll",0,"sides",0,0,0)
    '''
    drinks
    '''
    can_coca = Can_drink("can_coca",2.5,100,"drinks")
    bottle_coca = Bottle_drink("bottle_coca",3.5,100,"drinks")

    coca = Drinks_inventory("coca",30000,"drinks",0,0,0)
    orange = Drinks_inventory("orangejuice",20000,"drinks",0,0,0)
    sprite = Drinks_inventory("sprite",35000,"drinks",0,0,0)
    lift = Drinks_inventory("lift",0,"drinks",0,0,0)
    '''
    sundaes
    '''
    chocolate = Sundae_inventory("chocolate",10000,"sundaes",0,0,0)
    strawberry = Sundae_inventory("strawberry",10000,"sundaes",0,0,0)
    caramel = Sundae_inventory("caramel",0,"sundaes",0,0,0)
    '''
    add food item to inventory
    '''
    inventory.add_food(can_coca)
    inventory.add_food(salad)
    inventory.add_food(fries)
    inventory.add_food(fish_patties)
    inventory.add_food(chicken_patties)
    inventory.add_food(bottle_coca)
    inventory.add_food(tomato)
    inventory.add_food(lettuce)
    inventory.add_food(buns)
    inventory.add_food(coca)
    inventory.add_food(orange)
    inventory.add_food(sprite)
    inventory.add_food(chocolate)
    inventory.add_food(strawberry)
    '''
    empty food for test
    '''
    inventory.add_food(pork_patties)
    inventory.add_food(onions)
    inventory.add_food(springroll)
    inventory.add_food(lift)
    inventory.add_food(caramel)
    
    return inventory


