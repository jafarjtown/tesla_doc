
from tesla.router import Path
from . import views

# your urls path should be here
patterns = [
    Path('', views.home, name='home')
]
                  