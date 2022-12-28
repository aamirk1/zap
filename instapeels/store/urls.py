from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:slug>',views.collectionview,name='collectionview'),
    path('shop/',views.shop,name='shop'),
]
