from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponse

def mysum(request, x, y):
    result = x + y
    return HttpResponse('result = {}'.format(result))


def mymul(request, x, y):
    result = int(x) * int(y)
    return HttpResponse(f"result = {{{result}}}")

        
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysum/<int:x>/<int:y>', mysum ),
    re_path(r'^mymul/(?P<x>\d+)/(?P<y>\d+$)', mymul, name = "곱하기 테스트"),
    path('shop/', include('shop.urls')), # shop app의 urls.py 참조
    path('fileIO/', include('fileIO.urls')),
    path('blog/', include('blog.urls')),

]

