from django.db import models

class Articles(models.Model):
    titre= models.CharField(max_length=150)
    contenu= models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(default="default.jpg")
    


    def __str__(self):
        return self.titre
