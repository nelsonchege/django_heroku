from django.urls import path
from .views import Userprofileav , CakeVariety
urlpatterns=[
    path('users/',Userprofileav.as_view()),
    path('us/', CakeVariety.as_view())
]