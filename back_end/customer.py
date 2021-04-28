
class customer():
    def __init__(self,customer_id):
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    def __str__(self):
        return "Customer id: < {0} >".format(self._id)

