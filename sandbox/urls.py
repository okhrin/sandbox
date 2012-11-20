from django.conf.urls import patterns, include, url
from app.views import HomeView, ProfileView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),

    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
