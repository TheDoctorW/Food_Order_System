class ServicingError(Exception):
    def  __init__(self, errors, message = None):
        if message is None:
            message = "Ordering validation error occurred with fields: %s"%(','.join(errors.keys()))
            super().__init__(message)
            self.errors = errors
            
def check_service(customer_id, update_status):
    errors = {}
    if customer_id == '':
        errors['customer_id'] = 'Please enter a valid customer id!'
    if (update_status != 'Preparing') and (update_status != 'Pickup') and (update_status != 'Finish'):
        errors['update_status'] = 'Please enter a valid status!'
    if errors:
        raise ServicingError(errors)
