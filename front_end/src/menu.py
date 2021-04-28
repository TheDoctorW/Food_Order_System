
class Menu():
    def __init__(self):
        self._allfoodlist = []
    

    @property
    def get_foodlist(self):
        return self._allfoodlist
        
    def add_food(self,item):
        self._allfoodlist.append(item)

    def get_item(self,foodid):
        for item in self._allfoodlist:
            if item in self._allfoodlist:
                if item.foodid == foodid:
                    return item

    def show_item(self,foodid):
        for item in self._allfoodlist:
            if item.foodid == foodid:
                print(item)