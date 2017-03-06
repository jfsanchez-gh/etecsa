from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'etecsa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^ajax_search/$', views.ajax_search, name='ajax_search'),
]
