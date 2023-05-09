from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from rest_framework.response import Response
import os
from .settings import MEDIA_ROOT
from uuid import uuid4



# 클래스 == 하나의 기능
# APIView : 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와줌
class Main(APIView):    # APIView의 기능을 사용하겠다는 의미
    def get(self, request):     # Main 클래스를 get방식으로 실행했을 때를 의미
        feed_list = Feed.objects.all() # feed_list 안에 Feed 모델의 모든 데이터를 넣음
        return render(request, 'apps/main.html', context=dict(feed_list=feed_list))


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)


