from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('Now we have extra stuff: '
                                'date created', auto_now_add=True)
    extra_field = models.CharField(max_length=50, default = "hello")
    my_field = models.TextField(max_length=50, default="bjarne")
    # my_text = models.TextField()
    # def publish(self):
    #     self.save()


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

