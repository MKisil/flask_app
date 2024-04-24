from flask_admin.contrib.sqla import ModelView

from app.extensions import db, admin
from app.models.post import Post


class PostAdmin(ModelView):
    form_columns = ['title', 'slug', 'content', 'published_date', 'author', 'is_draft']


admin.add_view(PostAdmin(Post, db.session))
