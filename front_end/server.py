from flask import Flask
from src.order_system import order_system

app = Flask(__name__)
app.secret_key = 'very-secret-123' 

system = order_system()