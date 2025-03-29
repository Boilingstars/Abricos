from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
