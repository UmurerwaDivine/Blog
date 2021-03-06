from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quote
from .forms import BlogForm,UpdateProfile,CommentForm,SubscribeForm,UpdateForm
from .. import db
from ..models import User,Blog,Comment,Subscribe
from flask_login import login_required,current_user
from .. import db,photos
from ..sender_mail import mail_message



# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     message = 'Hello World'
#     return render_template('index.html',message = message)

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blog.get_blogs()
    quote=get_quote()
    # comments = Comment.get_comments()
    title = 'Home - Welcome to The best Blogs Review Website Online'

    return render_template('index.html', title = title,quote=quote,blogs=blogs)
@main.route('/subscribe',methods = ["GET","POST"])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():
        subscribe = Subscribe(email = form.email.data)
        db.session.add(subscribe)
        db.session.commit()

        mail_message("Welcome","email/welcome_user",subscribe.email)

        return redirect(url_for('main.index'))
        
    return render_template('sender.html',subscribe_form = form)
# @main.route('/quotes/<int:id>')
# def quotes(quote):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('index.html',quote = quote)
@main.route('/blog/new',methods= ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        username = form.username.data
        description = form.description.data
    #     pic_path = form.pic_path.data
       
    #     blogs = Blog.query.all()
    # if 'photo' in request.files:
    #     filename = photos.save(request.files['photo'])
    #     path = f'photos/{filename}'
    #     blogs.pic_path = path
    #     db.session.commit()
        # Updated review instance
        new_blog = Blog(description=description,username=username,user_id=current_user.id)
    
 
        # save pitch method
        new_blog.save_blogs()
        subscribes=Subscribe.query.all()
        for subscribe in subscribes:

          mail_message("New Post","sender_mail/sender_mail",subscribe.email,new_blog=new_blog)


   
        return redirect(url_for('.index',description=description,username=username))
    return render_template('new_blog.html', blog_form=form)
@main.route('/blog')
def show_blog():
 blogs = Blog.get_blogs()
 print(blogs)
 return render_template('new_blog.html', blogs=blogs)

@main.route('/update/blog',methods = ['GET','POST'])
@login_required
def update_blog(id):
    blogs = Blog.query.filter_by(id = id).all()
    if blogs is None:
        abort(404)

    form = UpdateForm()

    if form.validate_on_submit():
        username = form.username.data
        description = form.description.data
        pic_path = form.pic_path.data
        db.session.add(blogs)
        db.session.commit()

        return redirect(url_for('.index',blogs=blogs))

    return render_template('update_file.html',update_form=form)


@main.route('/comment/new/<int:id>',methods= ['GET','POST'])

def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        username = form.username.data
        description = form.description.data
        posted = form.posted.data
        # comments = Comment.query.filter_by(id=id).all()
 

        # Updated review instance
        new_comment = Comment(username=username,description=description,posted=posted,user_id=current_user.id)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.index',description=description,posted=posted ))

 
    return render_template('new_comment.html',comment_form=form)
# @main.route('/blog/<int:id>')
# def one_blog(id):
#    blogs = Blog.query.filter_by(id = id).first()
#    comments = Comment.query.filter_by(id=id)
#    return render_template('new_blog.html',comments=comments, blogs=blogs)
@main.route('/comment/<int:id>',methods= ['GET','POST'])
def show_comment():

 comments = Comment.get_comments()
 
 print(comments)
 return render_template('comments.html', comments=comments)
   
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))