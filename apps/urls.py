from django.urls import path
from .views import Main

urlpatterns = [
    path('', Main.as_view())    # views의 Main 클래스를 가져와 보여줌
]
