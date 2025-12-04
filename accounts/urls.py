from django.urls import path
from .views import SignUpView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    
]
