from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Blog, BlogCategory


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginate_by = 6
    context_object_name = "blog"

    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)
        context['categories'] = BlogCategory.objects.filter(is_active=True).all()
        return context

class BlogDetailView(View):
    def get(self,request, post_id):
        post: Blog = Blog.objects.filter(is_active=True, slug=post_id).first()
        # post = get_object_or_404(Blog, slug=post_id, is_active=True)
        post.view += 1
        post.save()

        return render(request, 'blog_detail.html', context={
        'post': post,
    })
