from django.urls import path
from . import views
urlpatterns = [
    path("home",views.home,name='home'),
    path("result",views.result,name='result'),
    path("about",views.about,name="about"),
    path("feedback",views.feed,name="feedback"),
    path("send",views.send,name="feedback"),
]