from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="places/images")
    place = models.CharField(max_length=200)
    catogory = models.ForeignKey("places.Catogory", on_delete=models.CASCADE)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = "places_place"
    def __str__(self):
        return self.name

class Catogory(models.Model):
    featured_image = models.ImageField(upload_to="catogories/images/")
    name = models.CharField(max_length=200)
    class Meta:
        db_table = "category"
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Gallery(models.Model):
    place = models.ForeignKey("places.Place", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="places/images")
    class Meta:
        db_table = "places_gallery"
        verbose_name_plural = "gallery"
    def __str__(self):
        return str(self.id)

class Login_Users(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Login_Users"

    def __str__(self):
        return self.name
    

class Posts(models.Model):
    post = models.TextField(max_length=399)
    date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey("places.Login_Users", on_delete=models.CASCADE)
    is_submitted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
       
        return self.username.name


class Like(models.Model):
    like_button = models.BooleanField(default=False)
    
    class Meta:
        db_table = "like_function" 

    def __str__(self):
        return str(self.id)

    