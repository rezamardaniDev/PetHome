from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import Blog, BlogCategory, BlogComment


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blog_list.html"
    paginate_by = 3
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['new_post']: Blog = Blog.objects.all().order_by('-created_date')[0:3]
        return context

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name).all()
        return query


class BlogDetailView(View):
    def get(self, request, post_id):
        post: Blog = Blog.objects.filter(is_active=True, id=post_id).first()
        categories = BlogCategory.objects.all()[0:3]
        comments = post.comments.all()
        post.view += 1
        post.save()

        return render(request, 'blog_detail.html', context={
            'post': post,
            'categories': categories,
            'comments': comments
        })

    def post(self, request, post_id):
        comment_form: CommentForm = CommentForm(request.POST)
        post: Blog = Blog.objects.filter(is_active=True, id=post_id).first()
        user = request.user
        if comment_form.is_valid():
            new_comment = BlogComment()
            new_comment.message = comment_form.cleaned_data.get('message')
            new_comment.user = user
            new_comment.post = post
            new_comment.save()
            return redirect('blog:blog_detail', post.id)
        else:
            comment_form.add_error('message', "مشکلی در ثبت کامنت شما پیش آمده است")
        return render(request, 'blog_detail.html', context={
            'post': post,
        })


def blog_categories_component(request):
    blog_categories = BlogCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'components/blog_categories_component.html', context={
        'categories': blog_categories
    })
