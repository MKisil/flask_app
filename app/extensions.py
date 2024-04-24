from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from app.admin.views import MyAdminIndexView

db = SQLAlchemy()

admin = Admin(index_view=MyAdminIndexView())
csrf = CSRFProtect()
