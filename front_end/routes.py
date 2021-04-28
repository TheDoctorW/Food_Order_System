from flask import render_template, request, redirect, url_for, abort
from server import app,system

'''
Initial page
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/',methods = ['POST','GET'])
def home_page():
    return render_template('Home_page.html')
'''
Create order
'''
@app.route('/home/order',methods = ['POST','GET'])
def create_order():
    customer_id = len(system.customer) + 100
    system.create_order(customer_id)
    return render_template('order_page.html',customer_id=customer_id)
'''
create base order
'''
@app.route('/home/order/base',methods = ['POST','GET'])
def create_base_order():
    customer_id = len(system.customer) + 100
    system.create_order(customer_id)
    return render_template('order_base_page.html',customer_id=customer_id)
'''
Base order
'''
@app.route('/home/order/base_burger/<customer_id>',methods = ['POST','GET'])
def base_burger(customer_id):
    system.order_a_mains("Burger")
    system.add_buns(2)
    system.add_patties("fish_patties",1)
    system.add_ingredient("tomato",1)
    system.add_ingredient("lettuce",3)
    system.add_mains
    system.add_drinks('coca','bottle',1)
    system.add_sides('fries','small',1)

    return redirect(url_for('home_page'))
@app.route('/home/order/base_wrap/<customer_id>',methods = ['POST','GET'])
def base_wrap(customer_id):
    system.order_a_mains("Wrap")
    system.add_buns(2)
    system.add_patties("fish_patties",1)
    system.add_ingredient("tomato",1)
    system.add_ingredient("lettuce",3)
    system.add_mains
    system.add_drinks('coca','bottle',1)
    system.add_sides('fries','small',1)
    return redirect(url_for('home_page'))
'''
Customlize mains
'''
from src.mains_forms import OrderingMainsForm
from src.buns_forms import OrderingBunsForm
from src.patties_forms import OrderingPattiesForm
from src.ingredients_forms import OrderingIngredientsForm
@app.route("/home/mains/<customer_id>",methods = ['POST','GET'])
def make_mains(customer_id):
    if request.method == "POST":
        if request.form.get('mains_name') != None:
            errors = {}
            form = OrderingMainsForm(request.form)
            if form.is_valid == False:
                if form.has_error('mains_name'):
                    errors['mains_name'] = form.get_error('mains_name') 
                if form.has_error('mains_name_type'):
                    errors['mains_name_type'] = form.get_error('mains_name_type')
                return render_template('make_mains.html',customer_id = customer_id, errors = errors)
            if form.is_valid == True:
                Type = request.form.get('mains_name')
                system.order_a_mains(Type)
        if (request.form.get('buns_number')) != None :
            errors = {}
            form = OrderingBunsForm(request.form)
            if form.is_valid == False:
                if form.has_error('buns_number'):
                    errors['buns_number'] = form.get_error('buns_number') 
                if form.has_error('buns_number_type'):
                    errors['buns_number_type'] = form.get_error('buns_number_type')
                if form.has_error('buns_limit'):
                    errors['buns_limit'] = form.get_error('buns_limit')
                return render_template('make_mains.html',customer_id = customer_id, errors = errors)
            if form.is_valid == True:
                Buns_num = int(request.form.get('buns_number'))
                system.add_buns(Buns_num)
        if request.form.get('patties_number') != None and request.form.get('patties_name') != None:
            errors = {}
            form = OrderingPattiesForm(request.form)
            if form.is_valid == False:
                if form.has_error('patties_name'):
                    errors['patties_name'] = form.get_error('patties_name') 
                if form.has_error('patties_name_type'):
                    errors['patties_name_type'] = form.get_error('patties_name_type')
                if form.has_error('patties_number'):
                    errors['patties_number'] = form.get_error('patties_number') 
                if form.has_error('patties_number_type'):
                    errors['patties_number_type'] = form.get_error('patties_number_type')
                if form.has_error('buns_limit'):
                    errors['patties_limit'] = form.get_error('patties_limit')
                return render_template('make_mains.html',customer_id = customer_id, errors = errors)
            if form.is_valid == True:
                Patty = request.form.get('patties_name')
                Patties_num = int(request.form.get('patties_number'))
                system.add_patties(Patty,Patties_num)
        if request.form.get('ingredients_number') != None and request.form.get('ingredients_name') != None:
            errors = {}
            form = OrderingIngredientsForm(request.form)
            if form.is_valid == False:
                if form.has_error('ingredients_name'):
                    errors['ingredients_name'] = form.get_error('ingredients_name') 
                if form.has_error('ingredients_name_type'):
                    errors['ingredients_name_type'] = form.get_error('ingredients_name_type')
                if form.has_error('ingredients_number'):
                    errors['ingredients_number'] = form.get_error('ingredients_number') 
                if form.has_error('ingredients_number_type'):
                    errors['ingredients_number_type'] = form.get_error('ingredients_number_type')
                if form.has_error('buns_limit'):
                    errors['ingredients_limit'] = form.get_error('ingredients_limit')
                return render_template('make_mains.html',customer_id = customer_id, errors = errors)
            if form.is_valid == True:
                ingredients = request.form.get('ingredients_name')
                ingredients_num = int(request.form.get('ingredients_number'))
                system.add_ingredient(ingredients,ingredients_num)
    return render_template('make_mains.html',customer_id = customer_id)

@app.route("/home/mains/add_mains/<customer_id>",methods = ['POST','GET'])
def add_mains(customer_id):
    system.add_mains
    return redirect(url_for('make_mains',customer_id = customer_id))
'''
Make other Order
'''
from src.drinks_forms import OrderingDrinksForm
@app.route("/home/drinks/<customer_id>",methods = ['POST','GET'])
def drinks(customer_id):
    if request.method == "POST":
        errors = {}
        form = OrderingDrinksForm(request.form)
        if form.is_valid == False:
            if form.has_error('drinks_name'):
                errors['drinks_name'] = form.get_error('drinks_name') 
            if form.has_error('drinks_name_type'):
                errors['drinks_name_type'] = form.get_error('drinks_name_type')
            if form.has_error('drinks_size'):
                errors['drinks_size'] = form.get_error('drinks_size')
            if form.has_error('drinks_size_type'):
                errors['drinks_size_type'] = form.get_error('drinks_size_type')
            if form.has_error('drinks_number'):
                errors['drinks_number'] = form.get_error('drinks_number')
            if form.has_error('drinks_number_type'):
                errors['drinks_number_type'] = form.get_error('drinks_number_type')
            if form.has_error('drinks_limit'):
                errors['drinks_limit'] = form.get_error('drinks_limit')   
            return render_template('drinks_order.html', customer_id=customer_id, errors = errors)
        if form.is_valid == True:
            drinks_name = request.form.get('drinks_name')
            drinks_size = request.form.get('drinks_size')
            drinks_number = request.form.get('drinks_number')
            system.add_drinks(drinks_name, drinks_size, int(drinks_number))
            #system.show_customer_order(customer_id)
            return render_template('drinks_order.html', customer_id=customer_id, errors = errors)
    return render_template('drinks_order.html',customer_id=customer_id)

from src.sides_forms import OrderingSidesForm
@app.route("/home/sides/<customer_id>",methods = ['POST','GET'])
def sides(customer_id):
    if request.method == "POST":
        errors = {}
        form = OrderingSidesForm(request.form)
        if form.is_valid == False:
            if form.has_error('sides_name'):
                errors['sides_name'] = form.get_error('sides_name') 
            if form.has_error('sides_name_type'):
                errors['sides_name_type'] = form.get_error('sides_name_type')
            if form.has_error('sides_size'):
                errors['sides_size'] = form.get_error('sides_size')
            if form.has_error('sides_size_type'):
                errors['sides_size_type'] = form.get_error('sides_size_type')
            if form.has_error('sides_number'):
                errors['sides_number'] = form.get_error('sides_number')
            if form.has_error('sides_number_type'):
                errors['sides_number_type'] = form.get_error('sides_number_type')
            if form.has_error('sides_limit'):
                errors['sides_limit'] = form.get_error('sides_limit')   
            return render_template('sides_order.html', customer_id=customer_id, errors = errors)
        if form.is_valid == True:
            sides_name = request.form.get('sides_name')
            sides_size = request.form.get('sides_size')
            sides_number = request.form.get('sides_number')
            system.add_sides(sides_name, sides_size, int(sides_number))
            #system.show_customer_order(customer_id)
            return render_template('sides_order.html', customer_id=customer_id, errors = errors)
    return render_template('sides_order.html',customer_id=customer_id)

from src.sundaes_forms import OrderingSundaesForm
@app.route("/home/sundae/<customer_id>",methods = ['POST','GET'])
def sundae(customer_id):
    if request.method == "POST":
        errors = {}
        form = OrderingSundaesForm(request.form)
        if form.is_valid == False:
            if form.has_error('sundaes_name'):
                errors['sundaes_name'] = form.get_error('sundaes_name')
            if form.has_error('sundaes_name_type'):
                errors['sundaes_name_type'] = form.get_error('sundaes_name_type')
            if form.has_error('sundaes_size'):
                errors['sundaes_size'] = form.get_error('sundaes_size')
            if form.has_error('sundaes_size_type'):
                errors['sundaes_size_type'] = form.get_error('sundaes_size_type')
            if form.has_error('sundaes_number'):
                errors['sundaes_number'] = form.get_error('sundaes_number')
            if form.has_error('sundaes_number_type'):
                errors['sundaes_number_type'] = form.get_error('sundaes_number_type')
            if form.has_error('sundaes_limit'):
                errors['sundaes_limit'] = form.get_error('sundaes_limit')   
            return render_template('sundae_order.html', customer_id=customer_id, errors = errors)
        if form.is_valid == True:
            sundaes_name = request.form.get('sundaes_name')
            sundaes_size = request.form.get('sundaes_size')
            sundaes_number = request.form.get('sundaes_number')
            system.add_sundaes(sundaes_name, sundaes_size, int(sundaes_number))
            #system.show_customer_order(customer_id)
            return render_template('sundae_order.html', customer_id=customer_id, errors = errors)
    return render_template('sundae_order.html',customer_id=customer_id)

'''
Customer view current order
'''
@app.route("/home/display_booking/<customer_id>",methods = ['POST','GET'])
def customer_booking(customer_id):
    order = system.customer_order(customer_id)
    return render_template("booking_detail.html",order = order,customer_id = customer_id)
'''
Customer search order
'''
from src.search_forms import SearchingForm
@app.route("/home/search",methods = ['POST','GET'])
def search_order():
    if request.method == 'POST':
        errors = {}
        form = SearchingForm(request.form)
        if form.is_valid == False:
            if form.has_error('customer_id'):
                errors['customer_id'] = form.get_error('customer_id')
            if form.has_error('customer_id_type'):
                errors['customer_id_type'] = form.get_error('customer_id_type')
            return render_template('search_id.html', errors = errors)
        if form.is_valid == True:
            customer_id = request.form.get('customer_id')
            return redirect(url_for('customer_booking',customer_id=customer_id))
    return render_template('search_id.html')
'''
Staff service
'''
@app.route("/home/staff_login",methods = ["POST",'GET'])
def staff_login():
    if request.method == 'POST':
        if request.form.get('password') == '111':
            return render_template('staff_channel.html')
    return render_template('login_page.html')

from src.manage_order_forms import ManagingOrderForm
@app.route("/home/manage_order",methods = ["POST",'GET'])
def manage_order():
    if request.method == 'POST':
        errors = {}
        form = ManagingOrderForm(request.form)
        if form.is_valid == False:
            if form.has_error('ID'):
                errors['ID'] = form.get_error('ID')
            if form.has_error('ID_type'):
                errors['ID_type'] = form.get_error('ID_type')
            if form.has_error('status'):
                errors['status'] = form.get_error('status')
            if form.has_error('status_type'):
                errors['status_type'] = form.get_error('status_type')
            return render_template('staff_service.html', errors = errors)
        if form.is_valid == True:
            status = request.form.get('status')
            ID = request.form.get('ID')
            system.staff_serivce(ID,status)
            return render_template('staff_service.html')
    return render_template('staff_service.html')

from src.manage_inventory_forms import ManagingInventoryForm
@app.route("/home/manage_inventory",methods = ["POST",'GET'])
def manage_inventory():
    if request.method == 'POST':
        errors = {}
        form = ManagingInventoryForm(request.form)
        if form.is_valid == False:
            if form.has_error('food_id'):
                errors['food_id'] = form.get_error('food_id')
            if form.has_error('food_id_type'):
                errors['food_id_type'] = form.get_error('food_id_type')
            return render_template('staff_inventory.html', errors = errors)
        if form.is_valid == True:
            food_id = request.form.get('food_id')
            avanum = system.staff_check_inventory(food_id)
            return render_template('display_inventory.html',food_id=food_id,avanum=avanum)
    return render_template('staff_inventory.html')

from src.update_inventory_forms import UpdatingInventoryForm
@app.route("/home/update_inventory",methods = ["POST",'GET'])
def update_inventory():
    if request.method == 'POST':
        errors = {}
        form = UpdatingInventoryForm(request.form)
        if form.is_valid == False:
            if form.has_error('food_name'):
                errors['food_name'] = form.get_error('food_name')
            if form.has_error('food_name_type'):
                errors['food_name_type'] = form.get_error('food_name_type')
            if form.has_error('number'):
                errors['number'] = form.get_error('number')
            if form.has_error('number_type'):
                errors['number_type'] = form.get_error('number_type')
            return render_template('update_inventory.html', errors = errors)
        if form.is_valid == True:
            foodid = request.form.get('food_name')
            num = request.form.get('number')
            system.staff_update_inventory(foodid,num)
    return render_template('update_inventory.html')

@app.route("/home/view_inventory",methods = ["POST",'GET'])
def display_allinventory():
    output = system.display_inventory
    return render_template('Inventory.html',output=output)

@app.route("/home/display_allorder",methods = ["POST",'GET'])
def display_allorder():
    totalorder = system.totalorder
    return render_template('all_bookingdetail.html',totalorder = totalorder)
'''
Menu
'''
@app.route("/home/menu",methods = ["POST","GET"])
def menu():
    output = system.display_menu
    return render_template("menu.html",output=output)
