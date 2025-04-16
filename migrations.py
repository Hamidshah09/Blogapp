from flaskblog import app, db
from flaskblog.models import User, Post
def create_db():
    with app.app_context():
        db.create_all()
def insert_record(model):
    with app.app_context():
        db.session.add(model)
        db.session.commit()
def run_query():
    with app.app_context():
    #     print(db.query.get(1))
        post = Post.query.first()
        print(post)
post_1 = Post(title='Blog 2', content='Second Post content', user_id=1)
insert_record(post_1)
run_query()
# create_db()