# from .views import main_banner
# from django.urls import path

# urlpatterns = [
#     path("", main_banner),
# ]

from django.urls import path
from .views import main_banner


urlpatterns = [
    path("", main_banner, name="main_banner"),
]
