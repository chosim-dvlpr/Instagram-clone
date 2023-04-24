from django.shortcuts import render
from rest_framework.views import APIView


# 클래스 == 하나의 기능
# APIView : 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와줌
class Main(APIView):    # APIView의 기능을 사용하겠다는 의미
    def get(self, request):     # Main 클래스를 get방식으로 실행했을 때를 의미
        return render(request, 'apps/main.html')