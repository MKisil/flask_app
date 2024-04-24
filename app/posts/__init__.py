from flask import Blueprint

bp = Blueprint('posts', __name__)

from app.posts import routes
from app.posts import admin

