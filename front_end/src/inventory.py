class Inventory():
    def __init__(self):
        self._allfoodlist = []
    
    def add_food(self,item):
        self._allfoodlist.append(item)
    
    def check_avaliablenum(self,foodid):
        for item in self._allfoodlist:
            if item.foodid == foodid:
                return item.avanum


    @property
    def get_foodlist(self):
        return self._allfoodlist
    
    def get_item(self,foodid):
        for item in self._allfoodlist:
            if item in self._allfoodlist:
                if item.foodid == foodid:
                    return item
    
    def unpdate_inventory(self,foodid,number):
        for item in self._allfoodlist:
            if item.foodid == foodid:
                item.avanum = number
    
    def show_item(self,foodid):
        for item in self._allfoodlist:
            if item.foodid == foodid:
                print(item)
    
    def check_ifavaliable(self,foodid):
        # print("I herererererer")
        for item in self._allfoodlist:
            if item.foodid == foodid:
                if item.avanum > 0:
                    return 1
                else:
                    return 0


