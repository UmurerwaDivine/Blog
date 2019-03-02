from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email
from wtforms.fields.html5 import DateField
from wtforms import ValidationError
from ..models import User,Blog,Comment,Subscribe
class BlogForm(FlaskForm):

    username = StringField('username', validators=[Required()])
    # category = SelectField('choose category',choices=[('pick-up-lines','pick-up-lines'),('Interview-pitch','Interview-pitch'),('other-pitch','other-pitch')])
    description = TextAreaField('Blogs ', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
      username = StringField('username', validators=[Required()])
      posted = DateField('date and time')
      description = TextAreaField('your comment ', validators=[Required()])
      submit = SubmitField('Submit')
class SubscribeForm(FlaskForm): 
     email = StringField('Your Email Address',validators=[Required(),Email()]) 
     submit = SubmitField('Subscribe')
     def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')
