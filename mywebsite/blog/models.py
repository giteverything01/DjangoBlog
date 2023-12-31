from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Img = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Title

    class Meta:
        db_table = 'Blog'