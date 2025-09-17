from django.urls import path

from apps.pages.views import UserWishlistPageView, AboutUsPageView, NotFoundPageView, ContactPageView, HomePageView

app_name = 'pages'

urlpatterns = [
    path('user-wishlist/', UserWishlistPageView.as_view(), name='user-wishlist'),
    path('about-us/', AboutUsPageView, name='about'),
    path('404/', NotFoundPageView.as_view(), name='404'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home')
]
