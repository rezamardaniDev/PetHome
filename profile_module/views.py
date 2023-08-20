from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class UserProfileView(TemplateView):
    template_name = "user_profile.html"

class UserEditProfile(View):
    def get(self, request):
        ...

    def post(self, request):
        ...

