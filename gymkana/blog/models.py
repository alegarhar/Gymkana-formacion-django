from django.db import models


class BaseItems(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=100, blank=False, null=False)
    body = models.TextField(blank=False)

    class Meta:
        abstract = True

class New(BaseItems):
    publish_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='blog/images', default='blog/images/default.jpg', null=True
    )
    def __str__(self):
        return self.title + ',' + self.subtitle

class Event(BaseItems):
    start_date = models.DateTimeField('started at', blank=False, null=False)
    end_date = models.DateTimeField('finished at', blank=False, null=False)
    list_display = ('title', 'subtitle', 'start_date', 'end_date')
    def __str__(self):
        return self.title + ',' + self.subtitle

