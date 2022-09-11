
from django.urls import path
from . import views

# id = erve
# pwb = erve01

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
]