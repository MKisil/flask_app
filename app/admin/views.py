from flask_admin import AdminIndexView
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.is_admin:
                return True
        return False
