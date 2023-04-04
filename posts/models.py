from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'posts'

    name = models.CharField(
        'Name', blank=False, null=False , max_length= 55, db_index=True, default='Anonymous' 
    )
    body = models.CharField(
        'body', blank=True, null=True , max_length=140, db_index=True, default='Tell us about yourself'
    )
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True 
    )
    image= CloudinaryField('image', blank=True , db_index=True)
    like = models.IntegerField('Like', default=0, blank=True, null=True)

