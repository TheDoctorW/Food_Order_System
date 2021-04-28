class UpdatingError(Exception):
    def  __init__(self, errors, message = None):
        if message is None:
            message = "Ordering validation error occurred with fields: %s"%(','.join(errors.keys()))
            super().__init__(message)
            self.errors = errors
            
def check_inventory(food_id, number):
    errors = {}
    if (food_id != 'fish_patties') and (food_id != 'chicken_patties') and (food_id != 'tomato') and (food_id != 'buns') and (food_id != 'lettuce') and (food_id != 'salad') and (food_id != 'fries') and (food_id != 'coca') and (food_id != 'orangejuice') and (food_id != 'sprite') and (food_id != 'chocolate') and (food_id != 'strawberry') and (food_id != 'pork_patties') and (food_id != 'onions') and (food_id != 'springroll') and (food_id != 'lift') and (food_id != 'caramel'):
        errors['food_id'] = 'Please enter a valid food name!'
    if number == '':
        errors['number'] = 'Please enter a valid number!'
    if errors:
        raise UpdatingError(errors)
