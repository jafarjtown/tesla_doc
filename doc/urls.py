
from tesla.router import Path
from . import views

# your urls path should be here
patterns = [
    Path('', views.index, name='index'),
    Path('documentation', views.documentation, name='doc-page'),
]
                  