from rest_framework import serializers
from .models import *


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class ArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arena
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class NewObjectsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewObjectsDetail
        fields = "__all__"


class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class BoburArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoburArena
        fields = "__all__"
