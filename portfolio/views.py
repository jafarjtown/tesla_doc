

from tesla.response import Render
from portfolio.models import Project, Testimonial


def home(request):
    proj = Project.all()
    tests = Testimonial.all()
    return Render(request, 'me/index.html', {'projects': proj, 'testimonials': tests})