from datetime import datetime

from slugify import slugify
from sqlalchemy import event

from app.extensions import db
from app.models.main import User


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150), unique=True)
    content = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_draft = db.Column(db.Boolean, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = self.create_slug()

    def __repr__(self):
        return f'<Post "{self.title}">'

    def create_slug(self):
        return slugify(self.title)

    @staticmethod
    def before_insert(mapper, connection, target):
        target.slug = target.create_slug()

    @staticmethod
    def before_update(mapper, connection, target):
        target.slug = target.create_slug()


event.listen(Post, 'before_insert', Post.before_insert)
event.listen(Post, 'before_update', Post.before_update)
