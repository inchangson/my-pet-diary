from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BulletinFeed
# Create your views here.
def board(request):
    feeds = BulletinFeed.objects.all().order_by('-id')
    page      = int(request.GET.get('page', 1))
    paginator = Paginator(feeds, 6)
    try:
        boards = paginator.page(page)
    except PageNotAnInteger:
        #N/A input, deliver first page
        boards = paginator.page(1)
    except EmptyPage:
        #larger than range, deliver last page
        boards = paginator.page(paginator.num_pages)
    return render(request, 'bulletin/board.html',{'boards':boards})


def feed(request, feed_id):
    feed = BulletinFeed.objects.get(id = feed_id)
    return render(request, 'bulletin/feed.html', {'feed':feed})