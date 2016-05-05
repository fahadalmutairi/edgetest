from __future__ import unicode_literals

from django.utils import timezone

from django.db import models
from django.utils.http import urlquote
from django.core.mail import send_mail



# Create your models here.


class Level(models.Model):
    level_name = models.CharField(null=True, blank=True, max_length=255)
    level_description = models.TextField()

    def __unicode__(self):
        return '%s' % self.level_name


class Subject(models.Model):
    level = models.ForeignKey('main.Level', null=True, blank=True)
    subject_name = models.CharField(max_length=255)
    subject_description = models.TextField()

    def __unicode__(self):
        return '%s' % self.subject_name


class Video(models.Model):
    subject_name = models.ForeignKey('main.subject', max_length=255)
    video_id = models.CharField(max_length=255)
    video_name = models.CharField(max_length=255)
    video_order = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['video_order',]

    def __unicode__(self):
        return '%s - %s - %s' % (self.subject_name, self.video_order, self.video_name)


class Comment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey('main.CustomUser', null=True)
    video = models.ForeignKey('main.Video', null=True)

    def __unicode__(self):
        return '%s' % self.author
