# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, render_template, request, flash, redirect, url_for
import logging
from logging import Formatter, FileHandler

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from forms import *
import os

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# Set your classes here.
# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#
class Post(Base):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content


# Create tables.
Base.metadata.create_all(bind=engine)


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/', methods=['GET', 'POST'])
def home():
    posts = Post.query.all()
    form = PostForm(request.form) or None
    if request.method == 'POST':
        if not request.form['title'] or not request.form['content']:
            flash('Please enter all the fields', 'error')
        else:
            objPost = Post(request.form['title'], request.form['content'])

            db.session.add(objPost)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('home'))
    return render_template('pages/placeholder.home.html', form=form, posts=posts)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    postObj = db.session.query(Post).filter_by(id=post_id).first()
    if not postObj:
        flash('Not found post_id: %d' % post_id, 'error')
        return redirect(url_for('home'))

    form = PostForm(request.form)
    form.title.default = postObj.title
    form.content.default = postObj.content
    form.process()
    if request.method == 'POST':
        if not request.form['title'] or not request.form['content']:
            flash('Please enter all the fields', 'error')
        else:
            postObj.title = request.form['title']
            postObj.content = request.form['content']
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('home'))
    return render_template('forms/post.html', form=form)


# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
