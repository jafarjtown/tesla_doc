
from tesla.admin.models import User
from tesla.modal import Model, ForeignKey, TextField, ManyToManyField



# class Comment(Model):
    

class Post(Model):
    
    user = ForeignKey(User)
    body = TextField()
    comments = ManyToManyField(User)

