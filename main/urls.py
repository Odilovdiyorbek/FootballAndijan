from django.urls import path
from .views import *

urlpatterns = [
    path('new/', NewView.as_view()),
    path('video/', VideoView.as_view()),
    path('table/', TableView.as_view()),
    path('player/', PlayerView.as_view()),
    path('product/', ProductView.as_view()),
    path('photo/', PhotoView.as_view()),
    path('arena/', ArenaView.as_view()),
    path('sponsor/', SponsorView.as_view()),
    path('info/', InfoView.as_view()),
    path('new-objectsDetail/', NewObjectsDetailView.as_view()),
    path('press/', PressView.as_view()),
    path('post/', PostView.as_view()),
    path('training/', TrainingView.as_view()),
    path('bobur-arena/', BoburArenaView.as_view()),
]