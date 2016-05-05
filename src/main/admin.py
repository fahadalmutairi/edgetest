from django.contrib import admin
from .models import Level, Subject, Video
# Register your models here.

class VideoInLine(admin.StackedInline):
    model = Video

class SubjectAdmin(admin.ModelAdmin):
    inlines = [VideoInLine,]
admin.site.register(Level)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Video)
