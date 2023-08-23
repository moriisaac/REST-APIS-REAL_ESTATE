from django.urls import path
from . import views

urlpatterns = [
    path('api/listings/', views.index, name='index'),
    path('api/listings/<int:listing_id>/', views.listing, name='listing'),
    path('api/search/', views.search, name='search'),

]