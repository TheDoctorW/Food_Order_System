from abc import ABC, abstractmethod

class ParseError(Exception):
    
    pass

    
class ManagingInventoryForm():
    
    def __init__(self, form):
        self._food_id = Field('food_id', [InputRequired('Food name cannot be empty!')])
        self._fields = [attr for attr in self.__dict__.values() if isinstance(attr, Field)]
        self._other_errors = {}
        self._parse(form)
        
    def _parse(self, form):
        for field in self._fields:
            field.parse(form.get(field.name, None))        
        if self._food_id.is_valid:
            if (self._food_id.data != 'fish_patties') and (self._food_id.data != 'chicken_patties') and (self._food_id.data != 'tomato') and (self._food_id.data != 'buns') and (self._food_id.data != 'lettuce') and (self._food_id.data != 'salad') and (self._food_id.data != 'fries') and (self._food_id.data != 'coca') and (self._food_id.data != 'orangejuice') and (self._food_id.data != 'sprite') and (self._food_id.data != 'chocolate') and (self._food_id.data != 'strawberry'):
                self._other_errors['food_id_type'] = 'Please enter a valid food name!'
                    
    def get_raw_data(self, field_name):
        field = self._field(field_name)
        if not field:
            return ''
        return field.raw_data or ''
 
    def get_error(self, field_name):
        field = self._field(field_name)
        if not field:
            return self._other_errors.get(field_name) or ''
        return field.error or ''

    def has_error(self, field_name):
        return self.get_error(field_name) is not ''

    def _field(self, field_name):
        return next((field for field in self._fields if field.name == field_name), None)

    @property
    def is_valid(self):
        if len(self._other_errors) > 0:
            return False
        return all(field.is_valid for field in self._fields)
        
    @property
    def food_id(self):
        return self._food_id.data
            
    
class Field():
    
    def __init__(self, name, validators = None):
        self._name = name
        self._validators = validators or []
        self._error     = None
        self._raw_data  = None
        self._data      = None

    def parse(self, raw_data):
        self._raw_data = raw_data
        try:
            for v in self._validators:  
                v.validate(raw_data)
            self._transform(raw_data)   

        except ParseError as pe:
            self._error = str(pe)

    def _transform(self, raw_data):
        self._data = raw_data

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error

    @property
    def raw_data(self):
        return self._raw_data
    
    @property
    def is_valid(self):
        return self._error is None

        
class Validator(ABC):

    def __init__(self, error_msg=''):
        self._error_msg = error_msg

    @abstractmethod
    def validate(self, raw_data):
        pass


class InputRequired(Validator):

    def __init__(self, error_msg='This field cannot be empty'):
        super().__init__(error_msg)

    def validate(self, raw_data):
        if raw_data is None or raw_data == '':
            raise ParseError(self._error_msg)
