from flask import render_template
from sqlalchemy.orm import joinedload

from app.models.post import Post
from app.posts import bp


@bp.route('/<slug>/')
def post_detail(slug):
    post = Post.query.options(joinedload(Post.author)).filter_by(slug=slug, is_draft=False).first_or_404()
    return render_template('posts/detail.html', post=post)
