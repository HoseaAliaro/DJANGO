from django.urls import path
from.import views


urlpatterns = [
    path('',views.Home,name="home"),
    path('create', views.stdForm, name="std"),
    path('regstd/', views.regStudent, name="regStudent"),
    path('fetch_std',views.retrieveStd, name="fetch_std"),
    path('updatestd/<int:pk>', views.updateStd, name="updateStd"),
    path('signup/',views.userRegistration,name="sign up"),
    path('login/',views.login_view,name="signin"),
    path('logout/',views.logout,name="signout"),
    path('deleteStd/<int:pk>',views.deleteStd,name="deleteStd")


]
