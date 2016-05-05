from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^subject_list/$', 'main.views.subject_list'),
    url(r'^subject_detail/(?P<pk>.+)/$', 'main.views.subject_detail'),
    url(r'^video_view/(?P<pk>.+)/$', 'main.views.video_view'),
    url(r'^video_list/$', 'main.views.video_list'),
    url(r'^levels/$', 'main.views.level_list'),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
