from inventory_errors import *
from order_system import order_system

import pytest

@pytest.fixture
def system():
    return order_system()
    
def test_invalid_food_id_test(system):
    print('test invalid food id test')
    errors = system.staff_update_inventory('', 50000)
    assert 'food_id' in errors
    assert errors['food_id'] == 'Please enter a valid food name!'
    
def test_invalid_number_test(system):
    print('test invalid number test')
    errors = system.staff_update_inventory('coca', '')
    assert 'number' in errors
    assert errors['number'] == 'Please enter a valid number!'
    
def test_successful_update_inventory_test(system):
    print('test successful update inventory test')
    errors = system.staff_update_inventory('coca', 30000)
    assert errors == {}
