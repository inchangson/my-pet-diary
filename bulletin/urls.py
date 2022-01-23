from django.urls import path
from . import views

app_name = 'bulletin'
urlpatterns = [
    path('', views.board),
    path('feed/<int:feed_id>/', views.feed),
]