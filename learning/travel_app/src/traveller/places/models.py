from django.db import models

# Create your models here.



class Place(models.Model):
    name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='places/images/', null=True, blank=True)
    place = models.CharField(max_length=200)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="places")
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "places_place"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(upload_to='categories/images/', null=True, blank=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "places_category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    place = models.ForeignKey(Place, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/gallery/', null=True, blank=True)

    class Meta:
        db_table = "places_gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return str(self.id)
