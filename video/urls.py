from django.urls import path
from video.views import(
    create_video_view,
    detail_video_view
)

app_name = 'video'

urlpatterns = [
    path('feltolt/', create_video_view, name='video'),
    path('<slug>/', detail_video_view, name="detail"),
]