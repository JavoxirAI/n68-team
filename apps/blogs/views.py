from django.views.generic import ListView, DetailView
from django.shortcuts import render
from apps.blogs.models import PostModel, CategoryModel, TagModel


class BlogListView(ListView):
    model = PostModel
    template_name = 'blogs/blog-list-sidebar-left.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        return context


class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        context['categories'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['related_posts'] = (
            PostModel.objects.filter(tags__in=post.tags.all())
            .exclude(id=post.id)
            .distinct()
        )
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.get_object():
            return render(self.request, 'pages/404.html', context)
        return super().render_to_response(context, **response_kwargs)
