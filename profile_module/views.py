from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from account_module.models import User
from order_module.models import Order, OrderDetail
from .forms import EditeProfileForm, ChangePasswordForm


class UserProfileView(LoginRequiredMixin, TemplateView):
    login_url = "/account/login"
    template_name = "user_profile.html"


class UserEditProfile(LoginRequiredMixin, View):
    login_url = "/account/login"

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


class ChangePasswordView(LoginRequiredMixin, View):
    login_url = "/account/login"

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


@login_required(login_url="/account/login")
def user_basket(request):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(user_id=request.user.id,
                                                                                             is_paid=False)
    total_amoutn = 0

    for order_detail in current_order.orderdetail_set.all():
        total_amoutn += order_detail.product.price * order_detail.count

    return render(request, "user_basket.html", context={
        'order': current_order,
        'sum': total_amoutn
    })


def delete_order_datail_func(request):
    detail_id = request.GET.get('detail_id')

    if detail_id is None:
        return JsonResponse({
            'status': 'not found detail id'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        user_id=request.user.id, is_paid=False)
    detail = current_order.orderdetail_set.filter(id=detail_id).first()

    if detail is None:
        return JsonResponse({
            'status': 'detail not found'
        })
    detail.delete()

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        user_id=request.user.id, is_paid=False)
    total_amoutn = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amoutn += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amoutn
    }
    data = render_to_string('basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


def change_order_datail_count(request):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()


    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()


        else:
            order_detail.count -= 1
            order_detail.save()


    else:
        return JsonResponse({
            'status': 'state invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        user_id=request.user.id, is_paid=False)
    total_amoutn = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amoutn
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('basket_content.html', context)
    })


@login_required(login_url="/account/login")
def last_order_detail(request):
    last_order: Order = Order.objects.filter(user_id=request.user.id, is_paid=True).all()

    return render(request, 'last_order.html', context={
        'last_order': last_order
    })
