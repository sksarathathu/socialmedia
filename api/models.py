from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="liked_by")


    def __str__(self):
        return self.title


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="likedby")

    def __str__(self):
        return self.comment
    
    



