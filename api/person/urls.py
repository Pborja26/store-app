from django.urls import path
from person import views

urlpatterns = [
    path('login/', views.CookieLoginView.as_view()),
    path('logout/', views.CookieLogoutView.as_view()),
    path('refresh/', views.CookieRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),
]