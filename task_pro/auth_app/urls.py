from django.urls import path
from .views import UserRegister, UserList


urlpatterns = [
    path('create/', UserRegister.as_view()),
    path('list/', UserList.as_view()),
]
