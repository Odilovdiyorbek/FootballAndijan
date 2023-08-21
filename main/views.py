from rest_framework.generics import *
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializer import *
from .models import *


class NewView(ListAPIView):
    queryset = New.objects.last()
    serializer_class = NewSerializer


class VideoView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class TableView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class PlayerView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PhotoView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class ArenaView(ListAPIView):
    queryset = Arena.objects.all()
    serializer_class = ArenaSerializer


class SponsorView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class InfoView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class NewObjectsDetailView(ListAPIView):
    queryset = NewObjectsDetail.objects.all()
    serializer_class = NewObjectsDetailSerializer


class PressView(ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TrainingView(ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class BoburArenaView(ListAPIView):
    queryset = BoburArena.objects.all()
    serializer_class = BoburArenaSerializer
























