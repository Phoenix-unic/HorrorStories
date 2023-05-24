from .db import db
from sqlalchemy.sql import func


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def add_post(cls, title, content, user_id):
        new_post = cls(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()

    @staticmethod
    def update_post(id, title, content):
        post = Post.query.get_or_404(id)
        post.title = title
        post.content = content
        db.session.commit()

    @classmethod
    def delete_post(cls, id):
        post = cls.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()

    @classmethod
    def delete_all_user_posts(cls, id):
        posts = cls.query.filter_by(user_id=id).all()
        for post in posts:
            db.session.delete(post)
        db.session.commit()

    def __repr__(self):
        return f'<Post about {self.title}>'












