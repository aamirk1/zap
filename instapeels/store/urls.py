from django.urls import path
from . import views
from store.controller import authview,cart,wishlist,checkout
urlpatterns = [
    path('',views.home,name='home'),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:slug>',views.collectionview,name='collectionview'),
    path('collection/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    path('shop/',views.shop,name='shop'),

    path('register/',authview.register, name='register'),
    path('login/',authview.loginpage, name='loginpage'),
    path('logout/',authview.logoutpage, name='logoutpage'),

    path('add_to_cart',cart.addtocart, name='addtocart'),
    path('cart',cart.viewcart, name='viewcart'),
    path('update-cart',cart.updatecart, name='updatecart'),
    path('deletecartitem',cart.deletecartitem, name='deletecartitem'),

    path('wishlist',wishlist.index, name='wishlist'),
    path('add_to_wishlist',wishlist.addtowishlist, name='addtowishlist'),
    path('deletewishlistitem',wishlist.deletewishlistitem, name='deletewishlistitem'),
    
    path('checkout',checkout.index, name='checkout'),
    path('placeorder',checkout.placeorder, name='placeorder'),


    
]
