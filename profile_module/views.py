from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order_module.models import Discount
from product_module.models import Product
from utils.offer import percent_maker
from django.contrib import messages
from account_module.models import User
from order_module.models import Order, OrderDetail, OrderCheckout, UserDescount
from .forms import EditeProfileForm, ChangePasswordForm


class UserProfileView(View):
    def get(self, request):
        return render(request, 'user_profile.html', context={

        })


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
    total = current_order.total_amount

    if request.method == 'POST':
        code = request.POST.get('discount')
        exists_code: Discount = Discount.objects.filter(code=code).first()
        useable = UserDescount.objects.filter(user=request.user, code=code).exists()
        if exists_code:
            if not useable:
                current_order.total_amount = percent_maker(current_order.total_amount, exists_code.percent)
                current_order.save()
                UserDescount.objects.get_or_create(user=request.user, code=code)
                messages.success(request, "کد تخفیف اعمال شد")
            else:
                messages.error(request, "این کد را قبلا استفاده کرده اید")
        else:
            messages.error(request, "کد تخفیف وجود ندارد یا ظرفیت آن به پایان رسیده")

    return render(request, "user_basket.html", context={
        'order': current_order,
        'sum': current_order.total_amount
    })


def change_order_detail_count(request):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        user_id=request.user.id, is_paid=False)

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
        current_order.total_amount += order_detail.product.price
        current_order.save()


    elif state == 'decrease':
        if order_detail.count == 1:
            current_order.total_amount -= (order_detail.product.price * order_detail.count)
            current_order.save()
            if current_order.total_amount <= 0:
                current_order.total_amount = 0
                current_order.save()
            order_detail.delete()


        else:
            order_detail.count -= 1
            order_detail.save()
            current_order.total_amount -= order_detail.product.price
            current_order.save()
            if current_order.total_amount <= 0:
                current_order.total_amount = 0
                current_order.save()



    else:
        return JsonResponse({
            'status': 'state invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
        user_id=request.user.id, is_paid=False)
    total_amount = current_order.total_amount

    context = {
        'order': current_order,
        'sum': total_amount
    }

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('basket_content.html', context)
    })


@login_required(login_url="/account/login")
def last_order_detail(request):
    last_order: OrderCheckout = OrderCheckout.objects.select_related('order').select_related('user').filter(
        order__user_id=request.user.id, order__is_paid=True)
    return render(request, 'last_order.html', context={
        'last_order': last_order,
    })
