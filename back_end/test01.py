from customer import customer
from order_errors import *
from order_system import order_system

import pytest

@pytest.fixture
def system():
    return order_system()

def test_invalid_customer_id_test(system):
    print('test invalid customer id test')
    cus1 = customer('')
    errors = system.create_order('')
    assert len(system.customer) == 0
    assert len(system.totalorder) == 0
    assert 'customer_id' in errors
    assert errors['customer_id'] == 'Detected a invalid customer id!'

def test_invalid_drinks_id_test(system):
    print('test invalid drinks id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('', 'samll', 2)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'drinks_foodid' in errors
    assert errors['drinks_foodid'] == 'Sorry, we do not have this drinks'

def test_invalid_drinks_size_test(system):
    print('test invalid drinks size test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', '', 2)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'drinks_size' in errors
    assert errors['drinks_size'] == 'Please enter a correct size!'

def test_invalid_drinks_number_test(system):
    print('test invalid drinks number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', '')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'drinks_number' in errors
    assert errors['drinks_number'] == 'Please enter a correct number!'
    
def test_invalid_drinks_limit_test(system):
    print('test invalid drinks limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'drinks_limit' in errors
    assert errors['drinks_limit'] == 'Sorry, exceed the maximum number!'

def test_invalid_drinks_inventory_test(system):
    print('test invalid drinks inventory test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('lift', 'large', 2)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'drinks_inventory' in errors
    assert errors['drinks_inventory'] == 'Sorry, not enough inventory!'

def test_invalid_sides_id_test(system):
    print('test invalid sides id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('', 'large', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sides_foodid' in errors
    assert errors['sides_foodid'] == 'Sorry, we do not have this sides!'

def test_invalid_sides_size_test(system):
    print('test invalid sides size test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', '', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sides_size' in errors
    assert errors['sides_size'] == 'Please enter a correct size!'

def test_invalid_sides_number_test(system):
    print('test invalid sides number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', '')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sides_number' in errors
    assert errors['sides_number'] == 'Please enter a correct number!'
    
def test_invalid_sides_limit_test(system):
    print('test invalid sides limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sides_limit' in errors
    assert errors['sides_limit'] == 'Sorry, exceed the maximum number!'
    
def test_invalid_sides_inventory_test(system):
    print('test invalid sides inventory test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('springroll', 'large', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sides_inventory' in errors
    assert errors['sides_inventory'] == 'Sorry, not enough inventory!'
    
def test_invalid_sundaes_id_test(system):
    print('test invalid sundaes id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_sundaes('', 'large', 2)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sundaes_foodid' in errors
    assert errors['sundaes_foodid'] == 'Sorry, we do not have this sundaes!'

def test_invalid_sundaes_size_test(system):
    print('test invalid sundaes size test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_sundaes('chocolate', '', 2)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sundaes_size' in errors
    assert errors['sundaes_size'] == 'Please enter a correct size!'

def test_invalid_sundaes_number_test(system):
    print('test invalid sundaes number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_sundaes('chocolate', 'large', '')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sundaes_number' in errors
    assert errors['sundaes_number'] == 'Please enter a correct number!'
    
def test_invalid_sundaes_limit_test(system):
    print('test invalid sundaes limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_sundaes('chocolate', 'large', 100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sundaes_limit' in errors
    assert errors['sundaes_limit'] == 'Sorry, exceed the maximum number!'
    
def test_invalid_sundaes_inventory_test(system):
    print('test invalid sundaes inventory test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_sundaes('caramel', 'large', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'sundaes_inventory' in errors
    assert errors['sundaes_inventory'] == 'Sorry, not enough inventory!'

def test_invalid_mains_type_test(system):
    print('test invalid mains type test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'mains_type' in errors
    assert errors['mains_type'] == 'Sorry, we do not have this mains!'

def test_invalid_patties_id_test(system):
    print('test invalid patties id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'patties_foodid' in errors
    assert errors['patties_foodid'] == 'Sorry, we do not have this patties!'

def test_invalid_patties_number_test(system):
    print('test invalid patties number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', '')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'patties_number' in errors
    assert errors['patties_number'] == 'Please enter a correct number!'
    
def test_invalid_patties_limit_test(system):
    print('test invalid patties limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_patties('fish_patties', 100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'patties_limit' in errors
    assert errors['patties_limit'] == 'Sorry, exceed the maximum number!'
    
def test_invalid_patties_inventory_test(system):
    print('test invalid patties inventory test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.add_patties('pork_patties', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'patties_inventory' in errors
    assert errors['patties_inventory'] == 'Sorry, not enough inventory!'

def test_invalid_ingredient_id_test(system):
    print('test invalid ingredient id test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'ingredient_foodid' in errors
    assert errors['ingredient_foodid'] == 'Sorry, we do not have this ingredient!'

def test_invalid_ingredient_number_test(system):
    print('test invalid ingredient number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', '')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'ingredient_number' in errors
    assert errors['ingredient_number'] == 'Please enter a correct number!'
    
def test_invalid_ingredient_limit_test(system):
    print('test invalid ingredient limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'ingredient_limit' in errors
    assert errors['ingredient_limit'] == 'Sorry, exceed the maximum number!'
    
def test_invalid_ingredient_inventory_test(system):
    print('test invalid ingredient inventory test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('onions', 1)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'ingredient_inventory' in errors
    assert errors['ingredient_inventory'] == 'Sorry, not enough inventory!'

def test_invalid_buns_number_test(system):
    print('test invalid buns number test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns('')
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'buns_number' in errors
    assert errors['buns_number'] == 'Please enter a correct number!'
    
def test_invalid_buns_limit_test(system):
    print('test invalid buns limit test')
    cus1 = customer(666)
    errors = system.create_order(666)
    errors = system.add_drinks('coca', 'small', 2)
    errors = system.add_sides('fries', 'large', 1)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns(100)
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert 'buns_limit' in errors
    assert errors['buns_limit'] == 'Sorry, exceed the maximum number!'

def test_successful_make_order1_test(system):
    print('test successful make order1 test')
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
    assert errors == {}

def test_successful_make_order2_test(system):
    print('test successful make order2 test')
    cus1 = customer(777)
    errors = system.create_order(777)
    errors = system.add_drinks('coca', 'large', 3)
    errors = system.add_sides('salad', 'small', 3)
    errors = system.order_a_mains('Buger')
    errors = system.add_patties('fish_patties', 1)
    errors = system.add_ingredient('tomato', 1)
    errors = system.add_buns(2)
    errors = system.add_mains
    assert len(system.customer) == 1
    assert len(system.totalorder) == 1
    assert errors == {}

