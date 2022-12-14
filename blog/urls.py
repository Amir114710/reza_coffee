from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('ourmenu' , views.OurMenu.as_view() , name='ourmenu'),
    path('shop' , views.ShopView.as_view() , name='shop'),
    path('details/<slug:slug>' , views.PostDetailView.as_view() , name='detail'),
    path('like/<slug:slug>/<int:pk>' , views.like , name='like'),
    path('search' , views.SearchBox.as_view() , name='search'),
    path('add_cart' , views.CartView.as_view() , name='cart'),
]