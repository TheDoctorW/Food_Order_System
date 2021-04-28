from customer import customer
from order_errors import *
from service_errors import *
from order_system import order_system

import pytest

@pytest.fixture
def system():
    return order_system()
    
def test_invalid_customer_id_test(system):
    print('test invalid customer id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns(2)
    errors = system.add_mains
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    errors = system.staff_serivce('', 'Preparing')
    assert 'customer_id' in errors
    assert errors['customer_id'] == 'Please enter a valid customer id!'
    
def test_invalid_updated_status_test(system):
    print('test invalid updated status test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns(2)
    errors = system.add_mains
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    errors = system.staff_serivce(666, '')
    assert 'update_status' in errors
    assert errors['update_status'] == 'Please enter a valid status!'
    
def test_successful_service_order_test(system):
    print('test successful service order test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns(2)
    errors = system.add_mains
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    errors = system.staff_serivce(666, 'Finish')
    print(type(system.customer))
    assert errors == {}
    assert len(system.totalorder) == 0
