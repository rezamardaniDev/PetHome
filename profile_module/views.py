from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from .forms import EditeProfileForm, ChangePasswordForm


# Create your views here.
class UserProfileView(TemplateView):
    template_name = "user_profile.html"


class UserEditProfile(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form: EditeProfileForm = EditeProfileForm(instance=current_user)

        return render(request, "edite_profile.html", context={
            'edit_form': edit_form,
            'user': current_user
        })

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form: EditeProfileForm = EditeProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return redirect('user:edit_profile')
        return render(request, "edite_profile.html", context={
            'edit_form': edit_form,
        })


class ChangePasswordView(View):
    def get(self, request):
        change_password: ChangePasswordForm = ChangePasswordForm()
        return render(request, "change_password.html", context={
            'change_password': change_password
        })

    def post(self, request):
        change_password: ChangePasswordForm = ChangePasswordForm(request.POST)
        if change_password.is_valid():
            user = User.objects.filter(id=request.user.id).first()
            is_correct_password = user.check_password(change_password.cleaned_data.get('old_password'))

            if is_correct_password:
                user.set_password(change_password.cleaned_data.get('confirm_password'))
                user.save()
                return redirect('account:login')
            else:
                change_password.add_error('old_password', 'رمزعبور فعلی اشتباه میباشد')
        else:
            change_password.add_error('new_password', 'خطایی در تغییر رمز عبور پیش آمده است')

        return render(request, "change_password.html", context={
            'change_password': change_password
        })


def profile_menu(request):
    return render(request, "components/profile_menu.html", context={

    })
