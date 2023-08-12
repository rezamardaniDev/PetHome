from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from site_module.models import SiteSettings


# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

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