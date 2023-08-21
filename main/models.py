from django.db import models
from ckeditor.fields import RichTextField


class New(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)


class Video(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    video = models.FileField()


class Table(models.Model):
    logo = models.ImageField()
    team = models.CharField(max_length=255)
    o = models.IntegerField()
    g = models.IntegerField()
    d = models.IntegerField()
    m = models.IntegerField()
    t_f = models.CharField(max_length=255)
    b = models.IntegerField()


class Player(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=(
        (1, "Darvozabon"),
        (2, "Himoyachi"),
        (3, "Markaz"),
        (4, "Hujumchi"),
    ))
    games = models.IntegerField(default=0)
    minutes_game = models.IntegerField(default=0)
    start = models.IntegerField(default=0)
    sub_off = models.IntegerField(default=0)


class Product(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Photo(models.Model):
    photo = models.ImageField(upload_to="photo/")


class Arena(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    kvm = models.IntegerField()
    place = models.IntegerField()
    sector = models.IntegerField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.ManyToManyField(Photo)


class Sponsor(models.Model):
    logo = models.ImageField(upload_to="sponsor/")


class Info(models.Model):
    logo = models.ImageField()
    text = models.CharField(max_length=255)
    instagram = models.URLField()
    telegram = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()
    twitter = models.URLField()
    phono = models.CharField(max_length=255)
    email = models.EmailField()


class NewObjectsDetail(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Press(models.Model):
    photo = models.ImageField(upload_to="press/")
    name = models.CharField(max_length=255)
    text = models.TextField()


class Post(models.Model):
    history = RichTextField()


class Training(models.Model):
    training = RichTextField()

    
class BoburArena(models.Model):
    history = RichTextField()




