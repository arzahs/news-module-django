from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    title = models.CharField(max_length=255)
    article = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=25)

    def __str__(self):
        return u'%s %s' % (self.title, self.added_date)

    def get_absolute_url(self):
        return reverse('detail_news', args=[self.pk])


class Comment(models.Model):
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s %s' % (self.text, self.news.title)

    def get_absolute_url(self):
        return reverse('detail_news', args=[self.news.pk])