from django.conf.urls import include, url
from django.contrib import admin



from appdjango.views import home, index

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home),
    url(r'^index/$', index),
    
]
