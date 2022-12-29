from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:slug>',views.collectionview,name='collectionview'),
    path('collection/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    path('shop/',views.shop,name='shop'),
]
