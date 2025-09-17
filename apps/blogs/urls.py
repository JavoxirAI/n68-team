from django.urls import path

from apps.blogs.views import BlogDetailView, BlogListView

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>', BlogDetailView.as_view, name='detail'),
    path('', BlogListView.as_view(), name='list')
]