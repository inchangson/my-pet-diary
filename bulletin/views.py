from django.http import HttpResponse
from django.shortcuts import render
from .models import BulletinFeed
# Create your views here.
def board(request):
    feed_list = BulletinFeed.objects.all()
    pages = [1,2,3,4,5]
    return render(request, 'bulletin/board.html',{'feed_list':feed_list, 'pages':pages})


# def feed(request, feed_id):
#     dest = f'{feed_id}' + '의 게시물'
#     return HttpResponse(dest)