from django.urls import path
from .views import view1
urlpatterns = [
path("", view1, name = "index")

]