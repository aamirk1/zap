from django.urls import path
from . import views
from main.controller import pages,authview,cart,wishlist,checkout
urlpatterns = [
    path('',views.home,name='home'),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:slug>',views.collectionview,name='collectionview'),
    path('collection/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),

    # authview.py page data link
    path('register/',authview.register, name='register'),
    path('login/',authview.loginpage, name='loginpage'),
    path('logout/',authview.logoutpage, name='logoutpage'),

    # cart.py page data link
    path('add_to_cart',cart.addtocart, name='addtocart'),
    path('cart',cart.viewcart, name='viewcart'),
    path('update-cart',cart.updatecart, name='updatecart'),
    path('deletecartitem',cart.deletecartitem, name='deletecartitem'),

    # wishlist.py page data link
    path('wishlist',wishlist.index, name='wishlist'),
    path('add_to_wishlist',wishlist.addtowishlist, name='addtowishlist'),
    path('deletewishlistitem',wishlist.deletewishlistitem, name='deletewishlistitem'),
    
    # checkout.py page data link
    path('checkout',checkout.index, name='checkout'),
    path('placeorder',checkout.placeorder, name='placeorder'),

    #pages
    path('aboutus',pages.aboutus,name='aboutus'),
    path('gallery',pages.gallery,name='gallery'),
    path('tpm',pages.ThirdPartyManufac,name='tpm'),
    path('contactus',pages.contactus,name='contactus'),
]

