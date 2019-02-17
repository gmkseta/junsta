from django.db import models

# Create your models here.



class TimeStampedModel(models.Model):

    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)


    class Meta:
        abstract = True



class Image(TimeStampedModel):

    file = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField( max_length=50)
    caption = models.TextField()

    
class Comment(TimeStampedModel):

    message = models.TextField()


