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
    username = models.ForeignKey(Login_Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_submitted = models.BooleanField(default=False)

    class Meta:
        db_table="Create_Post"
    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="replies")
    username = models.ForeignKey(Login_Users, on_delete=models.CASCADE)
    replay_text = models.TextField()
    is_submitted = models.BooleanField(default=False)
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.post.title} by {self.username.username}"
    

class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(Login_Users, on_delete=models.CASCADE)
    like_button = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
