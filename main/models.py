from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return 'author ' + self.name + self.surname

class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return 'tag ' + self.name

class Manga(models.Model):
    title = models.ImageField(upload_to='mangas/titles')
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    data_reliz = models.DateField()
    name = models.CharField(max_length=20, default="manga default name")
    tag = models.ManyToManyField(Tags, related_name='manga')

    def __str__(self):
        return 'Manga ' + self.name

class Glava(models.Model):
    name = models.CharField(max_length=20)
    num_tom = models.IntegerField()
    manga = models.ForeignKey(Manga,on_delete=models.CASCADE)
    def __str__(self):
        return 'Glava ' + self.name

def get_image_filename(instance, filename):
    title = instance.glava.name
    slug = slugify(title)
    return "mangas/manga/%s/%s" % (slug,filename)

class Pics(models.Model):
    pic = models.ImageField(upload_to=get_image_filename)
    glava = models.ForeignKey(Glava,on_delete=models.CASCADE)

