from flask import render_template, request, flash, redirect, url_for
from sqlalchemy.orm import joinedload

from app import db
from app.auth.utils import is_valid_email
from app.main import bp
from app.main.utils import is_valid_contact_name, is_valid_phone_number, is_valid_contact_message
from app.models.main import Contact
from app.models.post import Post


@bp.route('/')
def index():
    full_list = request.args.get('all_posts', 'n')
    if full_list == 'y':
        posts = Post.query.options(joinedload(Post.author)).filter_by(is_draft=False).all()
    else:
        posts = Post.query.options(joinedload(Post.author)).filter_by(is_draft=False).limit(10).all()

    return render_template('main/index.html', posts=posts, full_list=full_list)


@bp.route('/about/')
def about():
    return render_template('main/about.html')


@bp.route('/contact/')
def contact():
    return render_template('main/contact.html')


@bp.route('/contact/', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    is_valid_contact_form = all([
        is_valid_contact_name(name),
        is_valid_email(email),
        is_valid_phone_number(phone),
        is_valid_contact_message(message)
    ])

    if is_valid_contact_form:
        new_contact = Contact(name=name, email=email, phone=phone, message=message)
        db.session.add(new_contact)
        db.session.commit()

        flash('Your message has been sent successfully! Thank You!', 'success')
        return redirect(url_for('.contact'))

    flash('Invalid input.', 'error')
    return redirect(url_for('.contact'))
