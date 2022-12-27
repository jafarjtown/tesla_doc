
from tesla.router import Path
from . import views

# your urls path should be here
patterns = [
    Path('', views.HomePage().as_view(), name='index'),
    Path('test/', views.TestRetriveAllView().as_view(), name='sdoc-page'),
    Path('test/{username}/', views.TestDetaitlView().as_view(), name='sdoc-page'),
    Path('documentation', views.documentation, name='doc-page'),
]
                  