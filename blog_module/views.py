from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Blog, BlogCategory, BlogComment


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginate_by = 1
    context_object_name = "blog"

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name).all()
        return query

class BlogDetailView(View):
    def get(self,request, post_id):
        post: Blog = Blog.objects.filter(is_active=True, id=post_id).first()
        categories = BlogCategory.objects.all()[0:3]
        comments = post.comments.filter(parent=None).prefetch_related('blogcomment_set')
        post.view += 1
        post.save()

        return render(request, 'blog_detail.html', context={
        'post': post,
        'categories': categories,
        'comments': comments
    })

def blog_categories_component(request):
    blog_categories = BlogCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'components/blog_categories_component.html', context={
    'categories': blog_categories
    })
