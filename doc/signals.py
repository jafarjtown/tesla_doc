from tesla.signal import connect_post_save
from tesla.admin.models import User
from doc.models import Post

def handle(sender, instance, created, **kwargs):
    if created:
        print(created)
        p = Post.create(user__id = instance.id, body='new user is created')
    print(sender, instance)
    print('post')
    
    
connect_post_save(User, handle)    

