from customer import customer
from generate_inventory import generate_inventory
from generate_menu import generate_menu
from order import order
from make_mains import *
from item import *
from order_errors import *
from service_errors import *
from inventory_errors import *

class order_system():
    def __init__(self):
        self._customer = []
        self._totalorder = []
        self._inventory = generate_inventory()
        self._menu = generate_menu()
        self._tmpmains = []
        self._orderid = -1
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def totalorder(self):
        return self._totalorder
    '''
    create order
    '''
    def create_order(self,customer_id):
        try:
            check_customer(customer_id)
        except OrderingError as error:
            return error.errors
        cus = customer(customer_id)
        self._orderid = self._orderid + 1
        self._totalorder.append(order(customer_id))
        self._customer.append(cus)
        return {}
    '''
    order drinks
    '''
    def add_drinks(self,foodid,drinktype,number):
        try:
            check_drinks(foodid, drinktype, number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable(foodid) == 0:
            errors = {}
            errors['drinks_inventory'] = 'Sorry, not enough inventory!'
            return errors
        order_no = self._orderid
        if drinktype == "bottle" or drinktype == "can":
            foodid = drinktype+"_"+foodid
            drinks = self._inventory.get_item(foodid)
            correct_num = drinks.avanum - number
        else:
            foodid_menu = drinktype + "_" + foodid
            drinks = self._menu.get_item(foodid_menu)
            drinks_inventory = self._inventory.get_item(foodid)
            if drinktype == "small":
                correct_num = drinks_inventory.avanum - (number*250)
            elif drinktype == "large":
                correct_num = drinks_inventory.avanum - (number*450)
            elif drinktype == "medium":
                correct_num = drinks_inventory.avanum - (number*350)
        
        self._inventory.unpdate_inventory(foodid,correct_num)
        drinks.quantity = number
        self._totalorder[order_no].add_item(drinks)
        return {}
    '''
    order sides
    '''
    def add_sides(self,foodid,size,number):
        try:
            check_sides(foodid, size, number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable(foodid) == 0:
            errors = {}
            errors['sides_inventory'] = 'Sorry, not enough inventory!'
            return errors
        order_no = self._orderid
        # Searching foodid in menu
        foodid_menu = size + "_" +foodid
        sides = self._menu.get_item(foodid_menu)
        # Searching foodid in inventory
        sides_inventory = self._inventory.get_item(foodid)
        # validate size
        if size == "large":
            correct_num = sides_inventory.avanum - number * 125
        elif size == "small":
            correct_num = sides_inventory.avanum - number * 70
        elif size == "medium":
            correct_num = sides_inventory.avanum - number * 100
        sides.quantity = number
        self._inventory.unpdate_inventory(foodid,correct_num)
        self._totalorder[order_no].add_item(sides)
        return {}
    '''
    order sundaes
    '''
    def add_sundaes(self,foodid,size,number):
        try:
            check_sundaes(foodid, size, number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable(foodid) == 0:
            errors = {}
            errors['sundaes_inventory'] = 'Sorry, not enough inventory!'
            return errors
        order_no = self._orderid
        # Searching foodid in menu
        foodid_menu = size + "_" +foodid
        sundae = self._menu.get_item(foodid_menu)
        # Searching foodid in inventory
        sundae_inventory = self._inventory.get_item(foodid)
        # validate size
        if size == "large":
            correct_num = sundae_inventory.avanum - number * 125
        elif size == "small":
            correct_num = sundae_inventory.avanum - number * 70
        elif size == "medium":
            correct_num = sundae_inventory.avanum - number * 100
        sundae.quantity = number
        self._inventory.unpdate_inventory(foodid,correct_num)
        self._totalorder[order_no].add_item(sundae)
        return {}
    '''
    order mains
    '''
    def order_a_mains(self,mains_type):
        try:
            check_mains(mains_type)
        except OrderingError as error:
            return error.errors
        mains = 0
        if mains_type == "Buger":
            mains = Buger()
        elif mains_type == "Wrap":
            mains = Wrap()
        self._tmpmains.append(mains)
        return {}
    
    def add_patties(self,foodid,number):
        try:
            check_patties(foodid, number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable(foodid) == 0:
            errors = {}
            errors['patties_inventory'] = 'Sorry, not enough inventory!'
            return errors
        patties = self._inventory.get_item(foodid)
        patties.quantity = number
        correct_num = patties.avanum - number
        self._inventory.unpdate_inventory(foodid,correct_num)
        self._tmpmains[0].add_patties(patties)
        return {}
    
    def add_ingredient(self,foodid,number):
        try:
            check_ingredient(foodid, number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable(foodid) == 0:
            errors = {}
            errors['ingredient_inventory'] = 'Sorry, not enough inventory!'
            return errors
        ingredient = self._inventory.get_item(foodid)
        ingredient.quantity = number
        correct_num = ingredient.avanum - number
        self._inventory.unpdate_inventory(foodid,correct_num)
        self._tmpmains[0].add_ingredient(ingredient)
        return {}
    
    def add_buns(self,number):
        try:
            check_buns(number)
        except OrderingError as error:
            return error.errors
        if self._inventory.check_ifavaliable('buns') == 0:
            errors = {}
            errors['buns_inventory'] = 'Sorry, not enough inventory!'
            return errors
        buns = self._inventory.get_item("buns")
        buns.quantity = number
        correct_num = buns.avanum - number
        self._inventory.unpdate_inventory("buns",correct_num)
        self._tmpmains[0].add_buns(buns)
        return {}
    
    @property
    def add_mains(self):
        order_no = self._orderid
        self._totalorder[order_no].add_item(self._tmpmains[0])
        self._tmpmains.pop()
        return {}
    '''
    staff service
    '''
    def staff_serivce(self,customer_id,updated_status):
        try:
            check_service(customer_id, updated_status)
        except ServicingError as error:
            return error.errors
        for order in self._totalorder:
            if order._customer_id == customer_id:
                order.status = updated_status
        if updated_status == "Finish":
            for item in self._totalorder:
                if item.customer_id == customer_id:
                    self._totalorder.remove(item)
                    self._orderid = self._orderid - 1
        return {}
    
    def staff_check_inventory(self,foodid):
        item = self._inventory.get_item(foodid)
        return item.avanum
    
    def staff_update_inventory(self,foodid,num):
        try:
            check_inventory(foodid, num)
        except UpdatingError as error:
            return error.errors
        self._inventory.unpdate_inventory(foodid,num)
        return {}
    '''
    display
    '''
    @property
    def staff_check_ifavalible(self,foodid):
        item = self._inventory.get_item(foodid)
        re = self._inventory.check_ifavaliable(item.foodid)
        return re
    
    @property
    def display_inventory(self):
        inventory = self._inventory
        output = ''
        for item in inventory.get_foodlist:
            output = output + "{0}----num:{1}|||".format(item.foodid,item.avanum)
        return output

    @property
    def display_menu(self):
        menu = self._menu
        output = ''
        for item in menu.get_foodlist:
            output = output + "{0} ---price:{1}\n".format(item.foodid,item.unitprice)
        return output

    def customer_order(self,customer_id):
        for order in self._totalorder:
            if order.customer_id == int(customer_id):
                return order

    def show_customer_order(self,customer_id):
        status = 0
        print("=============ID {0}=============".format(customer_id))
        for order in self._totalorder:
            if order.customer_id == customer_id:
                print(order)
                status = 1
        if status == 0:
            print("Customer currently have no order")
        print("============= END ==============\n")


system = order_system()
cus1 = customer(666)
system.create_order(666)
system.add_drinks("coca","bottle",20)
system.add_drinks("coca","can",2)
system.add_drinks("coca","small",1)
system.add_drinks("lift","large",5)
system.add_sides("fries","small",1)
system.add_sides("salad","large",4)
system.add_sides("fries","medium",5)
system.add_sides("fries","small",1)
system.add_sides("fries","large",1)
system.add_sundaes("chocolate","small",2)
system.add_sides("salad","small",1)
system.add_sides("salad","large",1)
system.add_sundaes("chocolate","small",2)
system.order_a_mains("Buger")
system.add_buns(3)
system.add_patties("fish_patties",1)
system.add_patties("chicken_patties",2)
system.add_ingredient("tomato",1)
system.add_ingredient("lettuce",3)
system.add_mains

system.show_customer_order(666)
# system.staff_serivce(666,"finish")
# system.show_customer_order(666)
# print("avaum: {0}".format(system.staff_check_inventory("chocolate"))
# print("avaum: {0}".format(system.staff_check_inventory("bottle_coca")))
