"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
# url(r'/desired/url/', view, name='example'),

custom_patterns = [
    url( r'^character/', include('web.character.urls'))
]
# web/urls.py

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
