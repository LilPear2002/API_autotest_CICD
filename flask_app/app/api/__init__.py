"""API蓝图"""
from flask import Blueprint

api_bp = Blueprint('api', __name__)

from app.api import auth, products, orders, files, query
