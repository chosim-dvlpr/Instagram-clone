from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main.as_view()),    # views의 Main 클래스를 가져와 보여줌
    path('content/upload/', UploadFeed.as_view()),
]

# media 경로를 url에 포함 - /media/{file name} 으로 조회 가능하도록 함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
