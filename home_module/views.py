from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

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
        return context

class AboutUsView(View):
    def get(self, request):
        setting : SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        return render(request, "about_us.html", context={
            'setting': setting
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