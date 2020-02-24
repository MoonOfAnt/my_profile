from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(default='我的博客的标题', max_length=50)
    date = models.DateField()
    imag = models.ImageField(default='default.png', upload_to='image/')
    text = models.TextField(default='博客正文')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:100] + '......'