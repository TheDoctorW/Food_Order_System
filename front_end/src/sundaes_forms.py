from abc import ABC, abstractmethod

class ParseError(Exception):
    
    pass

    
class OrderingSundaesForm():
    
    def __init__(self, form):
        self._sundaesname = Field('sundaes_name', [InputRequired('Name cannot be empty!')])
        self._sundaesnumber = Field('sundaes_number', [InputRequired('Quantity cannot be empty!')])
        self._sundaessize = Field('sundaes_size', [InputRequired('Size cannot be empty!')])
        self._fields = [attr for attr in self.__dict__.values() if isinstance(attr, Field)]
        self._other_errors = {}
        self._parse(form)
        
    def _parse(self, form):
        for field in self._fields:
            field.parse(form.get(field.name, None))        
        if self._sundaesname.is_valid:
            if (self._sundaesname.data != 'chocolate') and (self._sundaesname.data != 'strawberry'):
                self._other_errors['sundaes_name_type'] = 'Sorry, we do not have this type of sundaes!'             
        if self._sundaessize.is_valid:
            if (self._sundaessize.data != 'large') and (self._sundaessize.data != 'medium') and (self._sundaessize.data != 'small'):
                self._other_errors['sundaes_size_type'] = 'Please enter a valid size!'
        if self._sundaesnumber.is_valid:
            if (self._sundaesnumber.data).isdigit() == False:
                self._other_errors['sundaes_number_type'] = 'Please enter a valid number!'
        if self._sundaesnumber.is_valid and (self._sundaesnumber.data).isdigit() == True:
            if (int(self._sundaesnumber.data) > 5):
                self._other_errors['sundaes_limit'] = 'Please enter a reasonable quantity!'
                    
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
    def sundaesname(self):
        return self._sundaesname.data
        
    @property
    def sundaesnumber(self):
        return self._sundaesnumber.data
        
    @property
    def sundaessize(self):
        return self._sundaessize.data
            
    
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
