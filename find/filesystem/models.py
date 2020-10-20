from django.db import models

# Create your models here.

class Startdir(models.Model):
    root_path = models.CharField(max_length=255, default='.')

    def __str__(self):
        return self.root_path


class File(models.Model):
    relative_to_startdir = models.ForeignKey(Startdir, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=18)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.file_path


