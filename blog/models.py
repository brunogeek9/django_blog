from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    sumary = RichTextField()
    content = models.CharField(max_length=800)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __srt__(self):
        return 'The post {} has your creation in {}'\
            .format(self.title, self.created_at)
