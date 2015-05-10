from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'olivia3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gallery.views.gallery', name='gallery'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/(?P<title>.*)/$', 'gallery.views.big', name='big'),
    url(r'^artists/(?P<artist>.*)/$', 'gallery.views.artist_view', name='artist'),

    url(r'^language/(?P<language>[a-z\-]+)/$', 'gallery.views.language'),

    url(r'^about/$', 'gallery.views.aboutme'),
    url(r'^login/$', 'gallery.views.login'),
    url(r'^auth$', 'gallery.views.auth_view'),
    url(r'^logout$', 'gallery.views.logout'),
    url(r'^loggedin$', 'gallery.views.gallery'),
    url(r'^invalid$', 'gallery.views.invalid_login'),

    url(r'^register$', 'gallery.views.register_user'),
    url(r'^register_success$', 'gallery.views.register_success'),


    # url(r'^accounts/login$', login),
    # url(r'^accounts/logout$', logout),

)
