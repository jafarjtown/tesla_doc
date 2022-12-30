

 
from tesla.static import staticfiles
from tesla import TeslaApp

from tesla.admin.models import User
from tesla.admin import abs_path, register_collections
import os
from pathlib import Path as Pa

from doc.models import Post
import doc.signals
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Pa(__file__).resolve().parent.parent 

TeslaApp.middlewares.set_middlewares([])

TeslaApp.auth_model = User

TeslaApp.templates_folders = [
    os.path.join(BASE_DIR, 'doc/templates'),
    os.path.join(abs_path, 'templates'),
]


register_collections(User, Post)
TeslaApp.registered_models = [User, Post]
MIDDLEWARES = []

# print(abs_path)
# print(os.path.join(abs_path, 'static'))

staticfiles.paths = [ os.path.join(BASE_DIR, 'doc/statics'), os.path.join(abs_path, 'statics')]
        