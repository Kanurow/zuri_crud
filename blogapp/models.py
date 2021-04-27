# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    class NewManger(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    post_status = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null = True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=10, choices=post_status, default= 'draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    objects = models.Manager() # default manager
    newmanager = NewManger() # custom manager

    def get_absolute_url(self):
        return reverse('blogapp:post_single', args=[self.slug])



    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
