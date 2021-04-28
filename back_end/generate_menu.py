from item import *
from drink import *
from sides import *
from drink import *
from sundaes import *
from menu import Menu
def generate_menu():
    '''
    ini menu
    '''
    menu = Menu()
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
    drinks
    '''
    can_coca = Can_drink("can_coca",2.5,100,"drinks")
    bottle_coca = Bottle_drink("bottle_coca",3.5,100,"drinks")

    small_coca = SmallDrink("small_coca",0,"drinks",2)
    medium_coca = MediumDrink("medium_coca",0,"drinks",2.75)
    large_coca = LargeDrink("large_coca",0,"drinks",3.75)
    large_lift = LargeDrink("large_lift",0,"drinks",3.75)
    '''
    sides
    '''
    small_fries = SmallSides("small_fries",0,"sides",1.5)
    large_fries = LargeSides("large_fries",0,"sides",2.5)
    medium_fries = MediumSides("medium_fries",0,"sides",3.5)

    small_salad = SmallSides("small_salad",0,"sides",1,75)
    medium_salad = MediumSides("medium_salad",0,"sides",2)
    large_salad = LargeSides("large_salad",0,"sides",4)
    large_springroll = LargeSides("large_springroll",0,"sides",5)

    '''
    sundae
    '''
    small_chocolate = SmallSundae("small_chocolate",0,"sundaes",2.5)
    medium_chocolate = MediumSundae("medium_chcoclate",0,"sundaes",3.5)
    large_chocolate = LargeSundae("large_chcoclate",0,"sundaes",4.5)
    large_caramel = LargeSundae("large_caramel",0,"sundaes",5)
    medium_strawberry = MediumSundae("medium_strawberry",0,"sundaes",2.5)
    small_strawberry = SmallSundae("small_strawberry",0,"sundaes",3.5)
    '''
    add food to menu
    '''
    menu.add_food(small_chocolate)
    menu.add_food(medium_chocolate)
    menu.add_food(large_chocolate)
    menu.add_food(medium_strawberry)
    menu.add_food(small_strawberry)

    menu.add_food(small_coca)
    menu.add_food(large_coca)
    menu.add_food(medium_coca)
    menu.add_food(fish_patties)
    menu.add_food(chicken_patties)
    menu.add_food(tomato)
    menu.add_food(buns)
    menu.add_food(lettuce)
    menu.add_food(can_coca)
    menu.add_food(bottle_coca)
    menu.add_food(small_fries)
    menu.add_food(large_salad)
    menu.add_food(large_fries)
    menu.add_food(medium_fries)
    menu.add_food(small_salad)
    menu.add_food(medium_salad)
    menu.add_food(large_salad)
    '''
    empty food for test
    '''
    menu.add_food(pork_patties)
    menu.add_food(onions)
    menu.add_food(large_springroll)
    menu.add_food(large_lift)
    menu.add_food(large_caramel)
    return menu
