from django.urls import path
from . import views

app_name = 'bulletin'
urlpatterns = [
    path('', views.board, name='board'),
    path('<int:feed_id>/', views.feed, name='feed'),
    path('upload/', views.upload, name='upload'),
]