from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Quote:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,author,id,quote):
        self.author =author
        self.id = id
        self.quote = quote
       
       


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    
    
    # Flask-Login integration
    def is_authenticated(self):
       return True

    def is_active(self):
       return True

    def is_anonymous(self):
       return False

    def get_id(self):
       return self.id

   
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    username = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'blog',lazy = "dynamic")
    subscribes = db.relationship('Subscribe',backref = 'blog',lazy = "dynamic")
    def __repr__(self):
        return f'User {self.description}'
    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(id):
        blogs = Blog.query.all()
        return blogs      
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    description =db.Column(db.String(255))
    username = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    def __repr__(self):
        return f'User {self.description}'

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(id):
        comments = Comment.query.all()
        return comments

class Subscribe(db.Model):
    __tablename__ = 'subscribes'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

# class VoteUp(db.Model):
#      __tablename__ = 'voteups'

#      id = db.Column(db.Integer,primary_key = True)
#      up =db.Column(db.Integer(255))
#      pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

#      def save_voteUp(self):
#         db.session.add(self)
#         db.session.commit()
    #  @classmethod
    #  def get_voteUp(cls,id):
    #      voteup= VoteUp.query.filter_by(pitch_id=id).all()