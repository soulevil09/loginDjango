from django.urls import path
from .views import HomeView, cadastro, Login

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', Login.as_view(), name='login'),
]