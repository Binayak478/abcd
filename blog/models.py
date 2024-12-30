from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=200,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
