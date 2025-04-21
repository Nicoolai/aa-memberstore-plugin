"""App URLs"""

# Django
from django.urls import path

# AA memberstore App
from memberstore import views

app_name: str = "memberstore"

urlpatterns = [
    path("", views.index, name="index"),
]
