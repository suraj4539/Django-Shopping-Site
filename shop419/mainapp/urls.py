from django.urls import path
from .views import homeView, aboutView, contactView

urlpatterns = [
    path("", homeView, name="home"),
    path("about", aboutView, name="aboutpage"),
    path("contacts", contactView, name="contactpage")

]
