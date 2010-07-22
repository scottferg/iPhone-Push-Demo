from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^push_demo/', include('push_demo.foo.urls')),
	(r'^register/$', 'push_demo.demo.views.registerDevice'),
	(r'^send/$', 'push_demo.demo.views.sendNotificationToDevice'),
	(r'^all/$', 'push_demo.demo.views.sendNotificationToAllDevices'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
