
from tesla.auth.decorators import login_required
from tesla.auth.views import login
from tesla.response import HttpResponse, Redirect, Render, JsonResponse
from tesla.pyhtml import CT
from tesla.views import View, DetailView,  RetrieveAllView
from tesla.admin.models import User
from doc.models import Post
# from faker import Faker
# fake = Faker(['it_IT', 'en_US', 'ja_JP'])
# your views


class TestDetaitlView(DetailView):
    model = User
    template = 'doc/index.html'
    lookup = 'username'
    response = JsonResponse


class TestRetriveAllView(RetrieveAllView):
    model = User
    template = 'doc/index.html'
    response = JsonResponse
    pagination = True
    pagination_count = 10


class HomePage(View):

    def get(self, request, *args, **kwargs):
        # print(request.user.email)
        return Render(request, 'doc/index.html')

    def post(self, request, *args, **kwargs):
        return Render(request, 'doc/docs-page.html')


def documentation(request):
    return Render(request, 'doc/docs-page.html')
