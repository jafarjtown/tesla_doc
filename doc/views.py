
from tesla.auth.decorators import login_required
from tesla.auth.views import login
from tesla.response import HttpResponse, Redirect, Render, JsonResponse
from tesla.pyhtml import CT

# your views
                  

def index(request):
    return Render(request, 'doc/index.html')                  


def documentation(request):
    return Render(request, 'doc/docs-page.html')                  