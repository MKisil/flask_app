from flask_admin.contrib.sqla import ModelView

from app.extensions import db, admin
from app.models.main import User, Contact

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Contact, db.session))
