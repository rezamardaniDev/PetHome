from django.shortcuts import render
from .models import Gallery

# Create your views here.
def test(request):
    image = Gallery.objects.filter(is_active=True).all()
    return render(request, "animal_gallery.html", context={
        'imgae': image
    })