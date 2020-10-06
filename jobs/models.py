from django.db import models

# Create your models here.
class Job(models.Model):
    #Images
    #image field type accept png jpegs etc, () means put in new folder when image added to job object by admin on site
    image=models.ImageField(upload_to='images/')
    #summary
    #() contains size of char field -affects how things saved in db
    summary=models.CharField(max_length=200)

    def __str__(self): #makes summary appear in jobs list instead of job 1 etc
        return self.summary
