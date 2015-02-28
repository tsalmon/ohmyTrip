from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

# Create your models here.
class Entry(models.Model):
	name = models.CharField(max_length=200)