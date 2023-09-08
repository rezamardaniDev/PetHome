from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from account_module.models import User
from blog_module.models import Blog
from home_module.models import AskQuestion
from product_module.models import Product
from site_module.models import SiteSettings


class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "index.html"
    ordering = ['-price']

    def get_context_data(self,**kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['setting'] : SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        context['article'] : Blog = Blog.objects.filter(is_active=True).order_by('created_date')[0:4]
        context['admin'] : User = User.objects.filter(is_superuser=True).first()
        return context


class AboutUsView(View):
    def get(self, request):
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        question: AskQuestion = AskQuestion.objects.all()
        admin : User = User.objects.filter(is_superuser=True).first()
        return render(request, "about_us.html", context={
            'setting': setting,
            'admin': admin,
            'question': question
        })


def site_header_component(request):
    setting : SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    return render(request, r"shared/header.html", context={
        'site_setting' : setting
    })

def site_footer_component(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    return render(request, r"shared/footer.html", context={
        'site_setting': setting
    })