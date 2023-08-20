from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class UserProfileView(TemplateView):
    template_name = "user_profile.html"


class EditProfileForm:
    pass


class UserEditProfile(View):
    def get(self, request):
        edit_form: EditProfileForm = EditProfileForm()
        return render(request,"edite_profile.html", context={
            'edit_form': edit_form,
        })

    def post(self, request):
        ...

def profile_menu(request):
    return render(request,"components/profile_menu.html", context={

    })