from django.urls import path
from.import views
app_name='seller'
urlpatterns=[
    path('',views.home),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('sellerdashboard/',views.sellerdashboard,name='sellerdashboard'),
    path('addpdt/',views.addpdt,name='addpdt'),
    path('viewpdt/',views.viewpdt,name='viewpdt'),
    path('updatepdt/<int:pid>',views.updatepdt,name='updatepdt'),
    path('deletepdt/<int:pid>',views.deletepdt,name='deletepdt'),
    path('logout/',views.logout,name='logout'),
    path('category',views.category,name='category'),
    path('viewcat/',views.viewcat,name='viewcat'),
    path('updatecat/<int:cat>',views.updatecat,name='updatecat'),
    path('deletecat/<int:cid>',views.deletecat,name='deletecat')


]
    

