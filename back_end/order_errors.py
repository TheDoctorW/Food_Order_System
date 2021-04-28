class OrderingError(Exception):
    def  __init__(self, errors, message = None):
        if message is None:
            message = "Ordering validation error occurred with fields: %s"%(','.join(errors.keys()))
            super().__init__(message)
            self.errors = errors

def check_customer(customer_id):
    errors = {}
    if customer_id == '':
        errors['customer_id'] = 'Detected a invalid customer id!'
    if errors:
        raise OrderingError(errors)

def check_drinks(drinks_foodid, drinks_size, drinks_number):
    errors = {}
    if (drinks_foodid != 'coca') and (drinks_foodid != 'can_coca') and (drinks_foodid != 'bottle_coca') and (drinks_foodid != 'orange') and (drinks_foodid != 'sprite') and (drinks_foodid != 'lift'):
        errors['drinks_foodid'] = 'Sorry, we do not have this drinks'
    if (drinks_size != 'bottle') and (drinks_size != 'can') and (drinks_size != 'small') and (drinks_size != 'medium') and (drinks_size != 'large'):
        errors['drinks_size'] = 'Please enter a correct size!'
    if drinks_number == '':
        errors['drinks_number'] = 'Please enter a correct number!'
    if drinks_number != '' and drinks_number > 20:
        errors['drinks_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)

def check_sides(sides_foodid, sides_size, sides_number):
    errors = {}
    if (sides_foodid != 'fries') and (sides_foodid != 'salad') and (sides_foodid != 'springroll'):
        errors['sides_foodid'] = 'Sorry, we do not have this sides!'
    if (sides_size != 'small') and (sides_size != 'medium') and (sides_size != 'large'):
        errors['sides_size'] = 'Please enter a correct size!'
    if sides_number == '':
        errors['sides_number'] = 'Please enter a correct number!'
    if sides_number != '' and sides_number > 10:
        errors['sides_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)
        
def check_sundaes(sundaes_foodid, sundaes_size, sundaes_number):
    errors = {}
    if (sundaes_foodid != 'chocolate') and (sundaes_foodid != 'strawberry') and (sundaes_foodid != 'caramel'):
        errors['sundaes_foodid'] = 'Sorry, we do not have this sundaes!'
    if (sundaes_size != 'small') and (sundaes_size != 'medium') and (sundaes_size != 'large'):
        errors['sundaes_size'] = 'Please enter a correct size!'
    if sundaes_number == '':
        errors['sundaes_number'] = 'Please enter a correct number!'
    if sundaes_number != '' and sundaes_number > 5:
        errors['sundaes_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)

def check_mains(mains_type):
    errors = {}
    if (mains_type != 'Buger') and (mains_type != 'Warp'):
        errors['mains_type'] = 'Sorry, we do not have this mains!'
    if errors:
        raise OrderingError(errors)

def check_patties(patties_foodid, patties_number):
    errors = {}
    if (patties_foodid != 'fish_patties') and (patties_foodid != 'chicken_patties') and (patties_foodid != 'pork_patties'):
        errors['patties_foodid'] = 'Sorry, we do not have this patties!'
    if patties_number == '':
        errors['patties_number'] = 'Please enter a correct number!'
    if patties_number != '' and patties_number > 3:
        errors['patties_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)

def check_ingredient(ingredient_foodid, ingredient_number):
    errors = {}
    if (ingredient_foodid != 'tomato') and (ingredient_foodid != 'lettuce') and (ingredient_foodid != 'onions'):
        errors['ingredient_foodid'] = 'Sorry, we do not have this ingredient!'
    if ingredient_number == '':
        errors['ingredient_number'] = 'Please enter a correct number!'
    if ingredient_number != '' and ingredient_number > 5:
        errors['ingredient_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)

def check_buns(buns_number):
    errors = {}
    if buns_number == '':
        errors['buns_number'] = 'Please enter a correct number!'
    if buns_number != '' and buns_number > 2:
        errors['buns_limit'] = 'Sorry, exceed the maximum number!'
    if errors:
        raise OrderingError(errors)

