from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from utils.http_service import get_client_ip
from .forms import CommentForm
from .models import Blog, BlogCategory, BlogComment, BlogVisit


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


def blog_categories_component(request):
    blog_categories = BlogCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'components/blog_categories_component.html', context={
        'categories': blog_categories
    })


class BlogDetailView(View):
    def get(self, request, post_id):
        post: Blog = Blog.objects.filter(is_active=True, id=post_id).first()
        categories = BlogCategory.objects.all()[0:3]
        comments = post.comments.all().order_by('-create_date')
        post_visit = BlogVisit.objects.filter(post_id=post_id).count()
        # <------------- Visit Post ------------->
        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id

        has_been_visited = BlogVisit.objects.filter(ip__iexact=user_ip, post_id=post_id).exists()
        if not has_been_visited:
            new_visit = BlogVisit(ip=user_ip, user_id=user_id, post_id=post.id)
            new_visit.save()
        # <------------------Comment-------------------->
        comment_message = request.GET.get('message')
        if request.GET:
            new_comment = BlogComment()
            new_comment.message = comment_message
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()

            return render(request, 'comment_ajax.html', context={
                'post': post,
                'categories': categories,
                'comments': comments,
                'view': post_visit
            })


        return render(request, 'blog_detail.html', context={
            'post': post,
            'categories': categories,
            'comments': comments,
            'view': post_visit
        })
