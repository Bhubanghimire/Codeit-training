from django.urls import path,include
from accounts.views import home, user_login, user_logout

urlpatterns = [
    path("", home, name="home"),
    path("profile/", home),
    path('login/',user_login, name="login"),
    path('logout/',user_logout, name="logout"),
    # user_logout

]