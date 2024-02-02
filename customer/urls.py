from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name='dashboard'),
   
   
    path('logout/',views.logout,name='logout'),
    path('error/',views.Errorpage,name='errorpage'),
    path('contactus/',views.ContactUs,name='contactus'),
    path('bagcategory/',views.bagcategory,name='bagcategory'),
    path('dresscategory/',views.dresscategory,name='dresscategory'),
    path('footwearcategory/',views.footwearcategory,name='footwearcategory'),
    path('cart/',views.cart,name='cart'),
    path('payment/',views.payment,name='payment'),
    path('add_to_cart/<int:p_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('wishlist/',views.wish,name='wishlist'),
    path('add_wishlist/<int:pid>',views.add_wishlist,name='add_wishlist'),
    path('remove_from_wish/<int:product_id>',views.remove_from_wish,name='remove_from_wish'),
]
