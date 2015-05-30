from django.conf.urls import include, url
from django.contrib import admin

import shoppinglistdata.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'shoppinglist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', shoppinglistdata.views.index, name='index'),
    url(r'^newitem/', shoppinglistdata.views.newitem, name='newitem'),
    url(r'^newuser/', shoppinglistdata.views.newuser, name='newuser'),
    url(r'^getlist/', shoppinglistdata.views.getlist, name='getlist'),
    url(r'^login/', shoppinglistdata.views.getlist, name='login')
]
#(?P<shoppingitem_id>[0-9]+)/